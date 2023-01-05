###

import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys
import chocolate
import sys
sys.path.insert(0, '../src')
sys.path.insert(0, '../data')

###

# Read in dataset.
def read_file(csv_file):

    df = pd.read_csv(csv_file)
    return df

###

# Grab the top ten countires containing the most chocolate ratings after counting values by company location and sorting the counts in descending order.
def top_ten_count_chocolate_ratings(choco_df):
     company_location = choco_df["Company Location"].value_counts().sort_values(ascending=False)
     top_ten_countries = company_location[0:10]

     fig, ax = plt.subplots()
     c = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
     '#bcbd22', '#17becf']
     ax.bar(top_ten_countries.index, top_ten_countries.values, color = c)

     ax.set_title("Top 10 # of Chocolate Ratings by Country")
     ax.set_ylabel("# of Chocolate Ratings")
     ax.set_xlabel("Countries")
     united_states_legend = mpatches.Patch(color= 'blue', label='U.S.A: 1168')
     france_legend = mpatches.Patch(color= 'orange', label='France: 179')
     canada_legend = mpatches.Patch(color= 'green', label='Canada: 178')
     uk_legend = mpatches.Patch(color= 'red', label='U.K.: 134')
     italy_legend = mpatches.Patch(color= 'purple', label='Italy: 79')
     belguim_legend = mpatches.Patch(color= 'brown', label='Belgium: 72')
     ecuador_legend = mpatches.Patch(color= 'pink', label='Ecuador: 58')
     australia_legend = mpatches.Patch(color= 'grey', label='Australia: 53')
     switzerland_legend = mpatches.Patch(color= 'yellow', label='Switzerland: 44')
     germany_legend = mpatches.Patch(color= 'teal', label='Germany: 43')
     plt.legend(handles=[united_states_legend, france_legend, canada_legend, uk_legend, italy_legend, belguim_legend, ecuador_legend, australia_legend, switzerland_legend, germany_legend])
     fig.set_size_inches(16, 10)
     plt.savefig("images/top_ten_bar_plot.png")
     return top_ten_countries

###

# Plot a % breakdown of the top ten countires containing the most chocolate ratings.
def top_ten_count_chocolate_ratings_percent(choco_df):
     company_location = choco_df["Company Location"].value_counts().sort_values(ascending=False)
     top_ten_countries = company_location[0:10]

     fig, ax = plt.subplots(figsize = (10,6))

     sizes = top_ten_countries.values
     labels = top_ten_countries.index.tolist()
     explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
     c = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
     '#bcbd22', '#17becf']
     plt.pie(sizes, explode=explode, colors=c, 
        autopct='%1.1f%%', shadow=True, startangle=140)
     ax.legend( labels, title="Country",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
     ax.set_title("Chocolate Location by Country: Top Ten")
     plt.tight_layout()
     plt.axis('equal')
     plt.savefig("images/top_ten_pie_chart.png")
     return top_ten_countries
     
###

# Bin data into 4 groups based on cocoa percent and rating.
def cocoa_percent_and_rating(choco_df):
    chocolate_data['Remove Cocoa Percentage'] = chocolate_data['Cocoa Percent'].astype(str).str.replace('%', '')
    chocolate_data['Cocoa Percentage as Float'] = chocolate_data['Remove Cocoa Percentage'].astype('float') / 100.0
    chocolate_data_high_both = choco_df[(choco_df['Cocoa Percentage as Float'] >= 0.70) & (choco_df['Rating'] >= 4.00)].shape[0]
    chocolate_data_high_cocoa = choco_df[(choco_df['Cocoa Percentage as Float'] >= 0.70) & (choco_df['Rating'] < 4.00)].shape[0]
    chocolate_data_mixed = choco_df[(choco_df['Cocoa Percentage as Float'] < 0.70) & (choco_df['Rating'] >= 4.00)].shape[0]
    chocolate_data_low_both = choco_df[(choco_df['Cocoa Percentage as Float'] < 0.70) & (choco_df['Rating'] < 4.00)].shape[0]
    chocolate_bins = {"Chocolate Data High Both":chocolate_data_high_both, "Chocolate Data High Cocoa":chocolate_data_high_cocoa,"Chocolate Data Mixed":chocolate_data_mixed, "Chocolate Data Low Both":chocolate_data_low_both}

    # Bar plot of data.
    fig, ax = plt.subplots(figsize = (10,6))
    c = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    cocoa_and_rating_comparison_sorted = dict(sorted(chocolate_bins.items(), key=lambda item: item[1]))
    cocoa_bins = list(cocoa_and_rating_comparison_sorted.keys())
    cocoa_bin_counts = list(cocoa_and_rating_comparison_sorted.values())

    plt.bar(range(len(cocoa_and_rating_comparison_sorted)), cocoa_bin_counts, tick_label=cocoa_bins, align = 'center', color = c)

    ax.set_title("Binned Chocolate Analysis")
    ax.set_ylabel("Chocolate Counts by Bin")
    ax.set_xlabel("Cocoa Percent & Rating Comparisons")
    chocolate_data_mixed_legend = mpatches.Patch(color= 'blue', label='Chocolate Data Mixed: 16')
    chocolate_data_high_both_legend = mpatches.Patch(color= 'orange', label='Chocolate Data High Both: 99')
    chocolate_data_low_both_legend = mpatches.Patch(color= 'green', label='Chocolate Data Low Both: 381')
    chocolate_data_high_cocoa_legend = mpatches.Patch(color= 'red', label='Chocolate Data High Cocoa.: 2,092')
    plt.legend(handles=[chocolate_data_mixed_legend, chocolate_data_high_both_legend, chocolate_data_low_both_legend,chocolate_data_high_cocoa_legend])
    fig.tight_layout()
    plt.savefig("images/binned_cocoa_analysis.png")
    
# Respective functions listed below to test outputs to terminal and images directory.

if __name__ == "__main__":
    
    chocolate_data = read_file("data/Chocolate_bar_ratings_2022.csv")
    
    # top_ten_chocolate_by_country = top_ten_count_chocolate_ratings(chocolate_data)
    
    # top_ten_chocolate_by_country_percentage = top_ten_count_chocolate_ratings_percent(chocolate_data)

    # cocoa_and_rating_comparison = cocoa_percent_and_rating(chocolate_data)