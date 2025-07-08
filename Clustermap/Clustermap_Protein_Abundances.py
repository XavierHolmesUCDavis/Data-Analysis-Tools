import pandas as pd
import seaborn as sns
import numpy as np
from scipy.cluster.hierarchy import fcluster

def col_to_letter(letter):
    letter = letter.upper()
    index = 0
    for char in letter:
        index = index * 26 + (ord(char) - ord('A'))
    return index

excel_path = "Z:/Xavier/Second Year/November_2022/Cyt_1_R2/Adjpoint2/After_GoodQC_11_28/Cytokine_Experiment_Proteins/Combined_Protein_Abundance_Cytokine_1_Test.xlsx"


df = pd.read_excel(excel_path)
df.rename(columns={df.columns[0]: "Protein_Name"}, inplace=True)
df.set_index(df.columns[0], inplace=True)

# only keep user input rows after ther first columns as a list
# Prompt user input for example from the excel file keep columns 1-6


#user_input = input("Enter the column letters to keep (e.g., A-F): ")
#start_letter, end_letter = user_input.split('-')
#start = col_to_letter(start_letter) - 1
#end = col_to_letter(end_letter)
#df = df.iloc[:, start:end]
df = df[df.std(axis=1) != 0]

# log2 transform the abundances
df = df.applymap(lambda x: np.log2(x + 1) if x > 0 else 0)

map = sns.clustermap(df, cmap="mako", figsize=(10, 10), z_score=0, center = 0 ,metric = 'correlation')
labels = fcluster(map.dendrogram_row.linkage, t=6, criterion='maxclust')
cluster_labels = pd.Series(labels, index=df.index, name='Cluster')
# Have to plot again with labels 
num_labels = len(np.unique(labels))
colormap = sns.color_palette("mako", num_labels)
label_to_color = {label: colormap[i] for i, label in enumerate(np.unique(labels))}
row_colors = cluster_labels.map(label_to_color)

map = sns.clustermap(df, cmap="mako", figsize=(10, 10), z_score=0,center = 0, metric='correlation', row_colors=row_colors)

output_cluster_data_excel = f"{excel_path.split('.')[0]}_clustered.xlsx"
with pd.ExcelWriter(output_cluster_data_excel) as writer:
    for cluster_label in sorted(cluster_labels.unique()):
        cluster_df = df[cluster_labels == cluster_label]
        cluster_label = str(cluster_label)
        cluster_df.to_excel(writer, sheet_name=f"Cluster_{cluster_label}")