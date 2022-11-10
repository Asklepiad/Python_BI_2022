#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil


# # Pandas intersect


# Functions for reading .GFF and .BED files

def read_gff(path_to_file):
    gff = pd.read_csv(path_to_file, sep="\t", names=["chrom", "source", "type", "start", "end", "score", "strand", "phase", "attributes"], header=0)
    return gff

def read_bed(path_to_file):
    bed = pd.read_csv(path_to_file, sep="\t", names=["chrom", "chromStart", "chromEnd", "name", "bed_score", "bed_strand"])
    return bed



# Example of standard reading of .GFF file. Cutting long string around type of RNA

rgff = read_gff("/home/asklepiad/bioinf/python/git_projects_BI_2022/hw6/rrna_annotation.gff")
rgff["attributes"] = rgff["attributes"].str.removeprefix("Name=").str.replace("_rRNA.*", "")
rgff


# Table of RNA types number per chromosome

number_of_rnas = rgff.groupby(["chrom", "attributes"], as_index=False).size()
number_of_rnas["chrom"] = number_of_rnas["chrom"].str.removeprefix("Reference_")
number_of_rnas


# Creating barplot by previously-described data

sns.barplot(number_of_rnas, x=number_of_rnas.iloc[:, 0], y=number_of_rnas.iloc[:, 2], hue=number_of_rnas.iloc[:, 1])


# Reading .BED file

rbed = read_bed("/home/asklepiad/bioinf/python/git_projects_BI_2022/hw6/alignment.bed")
rbed


# Bedtools intersect without bedtools

inter_before = pd.merge(rgff, rbed, on="chrom")
inter_before




# # Volcano plot


# Downloading data

difexpr = pd.read_csv("/home/asklepiad/bioinf/python/git_projects_BI_2022/hw6/diffexpr_data.tsv.gz", sep="\t")
difexpr['quater'] = "0"
difexpr


# Subseting data

df1 = difexpr[(difexpr['pval_corr'] > 0.05) & (difexpr['logFC'] >= 0)]
df1['quater'] = "Non-significantly upregulated"

df2 = difexpr[(difexpr['pval_corr'] > 0.05) & (difexpr['logFC'] < 0)]
df2['quater'] = "Non-significantly downregulated"

df3 = difexpr[(difexpr['pval_corr'] <= 0.05) & (difexpr['logFC'] < 0)]
df3['quater'] = "Significantly upregulated"

df4 = difexpr[(difexpr['pval_corr'] <= 0.05) & (difexpr['logFC'] >= 0)]
df4['quater'] = "Significantly downregulated"


# Preparing extremal values for annotation

df4_max = df4['logFC'].nlargest(2)
df3_min = df3['logFC'].nsmallest(2)
for i in df4_max:
    print(df4.query('logFC == @i')[['Sample', 'logFC', 'log_pval']])
for j in df3_min:
    print(df3.query('logFC == @j')[['Sample', 'logFC', 'log_pval']])
point_min1 = [-10.661093, 52.117378, 'UMOD']
point_min2 = [-9.196481, 2.171498, 'MUC7']
point_max1 = [4.571915, 3.075183, 'ZIC2']
point_max2 = [4.276745, 4.121027, 'ZIC5']


# Combining separated data

difexpr2 = pd.concat((df1, df2, df3, df4))
difexpr2


# rcParams is simply the best

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams["mathtext.bf"] = 'sans:bold:italic'
plt.rcParams['legend.markerscale'] = 0.7
plt.rcParams['legend.shadow'] = True
plt.rcParams['legend.fontsize'] = 'medium'
plt.rcParams['legend.framealpha'] = 1.0
plt.rcParams['legend.handleheight'] = 0.2
plt.rcParams['legend.labelspacing'] = 0.4


# Computing some additional information for beautiful axises.

x_lim_tick = ceil(max(abs(min(difexpr2['logFC'])), abs(max(difexpr2['logFC']))))


# Volcano plot

volcano_plot = plt.figure(figsize=(9.0, 5.8))
volcan = sns.scatterplot(data=difexpr2, x=difexpr2['logFC'], y=difexpr2['log_pval'],  hue=difexpr2['quater'], s=8, linewidth=0,                         hue_order=['Significantly upregulated', 'Significantly downregulated', 'Non-significantly downregulated', 'Non-significantly upregulated'])


# Axises and title

volcan.axhline(1.301, linestyle="--", color="grey", linewidth=1)
volcan.axvline(0, linestyle="--", color="grey", linewidth=1)
volcan.text(x=8, y=1.5, s="p_value=0.05", size=8, color="grey")
volcan.set_xlabel('$\mathbf{log_2}$(fold change)', weight='bold', style='italic', fontsize='12')
volcan.set_ylabel('$\mathbf{-log_{10}}$(p value corrected)', weight='bold', style='italic', fontsize='12')
volcan.set_title('Volcano plot', weight='bold', style='italic', fontsize='17')
volcan.set_xticks(ticks = np.arange(-x_lim_tick, x_lim_tick + 1, 1), minor=True)
volcan.set_yticks(ticks = np.arange(-5, max(difexpr2['log_pval']) + 5, 5), minor=True)
volcan.set_xlim(-x_lim_tick - 1, x_lim_tick + 1)


# Legend

legend = volcan.legend(loc = "upper right")
plt.setp(volcan.get_legend().get_texts(), fontsize='8', weight="bold")


# Annotations

volcan.annotate(point_max1[2], xy=(point_max1[0], point_max1[1]), xytext=(point_max1[0] - 1, point_max1[1] + 10,),                fontsize=8, weight="bold", arrowprops=dict(arrowstyle="simple", fc="red", linewidth=0.5))
volcan.annotate(point_max2[2], xy=(point_max2[0], point_max2[1]), xytext=(point_max2[0] - 1, point_max2[1] + 10,),                fontsize=8, weight="bold", arrowprops=dict(arrowstyle="simple", fc="red", linewidth=0.5))
volcan.annotate(point_min1[2], xy=(point_min1[0], point_min1[1]), xytext=(point_min1[0] - 1, point_min1[1] + 10,),                fontsize=8, weight="bold", arrowprops=dict(arrowstyle="simple", fc="red", linewidth=0.5))
volcan.annotate(point_min2[2], xy=(point_min2[0], point_min2[1]), xytext=(point_min2[0] - 1, point_min2[1] + 10,),                fontsize=8, weight="bold", arrowprops=dict(arrowstyle="simple", fc="red", linewidth=0.5))


volcano_plot.savefig("volcano_plot_sotnikov.png", bbox_inches="tight", dpi=600)

