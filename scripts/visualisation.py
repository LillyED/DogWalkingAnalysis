#Installing and importing libraries
!pip install matplotlib seaborn
import matplotlib.pyplot as plt
import seaborn as sns

#Visualisations

#Bar plot for Services Available 
plt.figure(figsize=(10, 6))
sns.barplot(x=combined_data['Town'], y=combined_data['Services Available'], palette='viridis')
plt.title('Services Available in Each Town')
plt.xlabel('Town')
plt.ylabel('Number of Services')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Bar plot for Dogs Per Town
plt.figure(figsize=(10, 6))
sns.barplot(x=combined_data['Town'], y=combined_data['Dogs Available'], palette='coolwarm')
plt.title('Dogs per Town')
plt.xlabel('Town')
plt.ylabel('Number of Dogs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Scatterplot for Dogs and Towns
plt.figure(figsize=(10, 6))
plt.scatter(combined_data['Town'], combined_data['Dogs Available'], color='blue', label='Dogs Available', alpha=0.7)
plt.title('Number of Dogs per Town')
plt.xlabel('Town')
plt.ylabel('Number of Dogs')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

#Scatterplot for Services Available and Towns
plt.figure(figsize=(10, 6))
plt.scatter(combined_data['Town'], combined_data['Services Available'], color='green', label='Services', alpha=0.7)
plt.title('Services Available per Town')
plt.xlabel('Town')
plt.ylabel('Number of Services')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

#Combined scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(combined_data['Town'], combined_data['Dogs Available'], color='blue', label='Dogs Available', alpha=0.7)
plt.scatter(combined_data['Town'], combined_data['Services Available'], color='green', label='Services', alpha=0.7)
plt.title('Dogs and Services per Town')
plt.xlabel('Town')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
