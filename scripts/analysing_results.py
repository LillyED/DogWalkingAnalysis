import pandas as pd

# Load the combined data
combined_data = pd.read_csv('combined_dog_data.csv')

# Sorting by Services Available (Descending)
sorted_by_services = combined_data.sort_values(by='Services Available', ascending=False)
print("Towns with most services:\n", sorted_by_services)

# Sorting by Dogs (Descending)
sorted_by_dogs = combined_data.sort_values(by='Dogs Available', ascending=False)
print("Towns with most dogs:\n", sorted_by_dogs)

# Save the sorted results
sorted_by_services.to_csv('sorted_by_services.csv', index=False)
sorted_by_dogs.to_csv('sorted_by_dogs.csv', index=False)

"""results

Towns with most services:
                Town  Dogs Available  Services Available
1           bromley        0.311382                 112
0         beckenham        0.126331                  35
4         sevenoaks        2.300107                  31
8          dartford        2.648599                  31
9   tunbridge Wells       20.150082                  31
10       bellingham        0.106726                  30
11              lee        0.116801                  30
3        mottingham        0.157699                  21
7            sidcup        1.002327                  21
6       chislehurst        0.172330                  20
5         orpington        0.577376                  17
2           bickley        0.000000                   5

Towns with most dogs:
                Town  Dogs Available  Services Available
9   tunbridge Wells       20.150082                  31
8          dartford        2.648599                  31
4         sevenoaks        2.300107                  31
7            sidcup        1.002327                  21
5         orpington        0.577376                  17
1           bromley        0.311382                 112
6       chislehurst        0.172330                  20
3        mottingham        0.157699                  21
0         beckenham        0.126331                  35
11              lee        0.116801                  30
10       bellingham        0.106726                  30
2           bickley        0.000000                   5
"""
