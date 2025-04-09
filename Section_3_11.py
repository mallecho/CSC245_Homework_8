import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV files.
pop_df = pd.read_csv("state-population.csv")
areas_df = pd.read_csv("state-areas.csv")
abbrevs_df = pd.read_csv("state-abbrevs.csv")

# 2. Filter and prepare the population data.
# Use only rows where ages is "total" (note lowercase) and year is 2013.
pop_filtered = pop_df[(pop_df["ages"] == "total") & (pop_df["year"] == 2013)].copy()
# Rename the state abbreviation column so that it can merge with the abbrevs file.
pop_filtered.rename(columns={"state/region": "abbreviation"}, inplace=True)
pop_filtered["abbreviation"] = pop_filtered["abbreviation"].str.strip().str.lower()

# Standardize the abbreviations DataFrame.
abbrevs_df["abbreviation"] = abbrevs_df["abbreviation"].str.strip().str.lower()
abbrevs_df["state"] = abbrevs_df["state"].str.strip().str.lower()

# Merge population with abbreviations to obtain full state names.
pop_full = pd.merge(pop_filtered, abbrevs_df, on="abbreviation", how="inner")

# 3. Prepare the areas data.
areas_df["state"] = areas_df["state"].str.strip().str.lower()
areas_df.rename(columns={"area (sq. mi)": "area"}, inplace=True)

# Merge the full population data with the areas data on state.
state_df = pd.merge(pop_full, areas_df, on="state", how="inner")

# 4. Compute population density.
state_df["density"] = state_df["population"] / state_df["area"]

# Filter the top 10 most densely populated states.
top10_dense = state_df.sort_values(by="density", ascending=False).head(10)
print("Top 10 Most Densely Populated States:")
print(top10_dense[["state", "density"]])

# 5. Add a categorical column based on population size.
def pop_category(pop):
    if pop < 5_000_000:
        return "small"
    elif pop < 10_000_000:
        return "medium"
    else:
        return "large"

state_df["pop_category"] = state_df["population"].apply(pop_category)
print("\nSample Population Categories:")
print(state_df[["state", "population", "pop_category"]].head())

# 6. Visualize state population vs. area using a scatter plot.
plt.figure(figsize=(10, 6))
# Highlight states with population > 10 million in red.
pop_mask = state_df["population"] > 10_000_000
plt.scatter(state_df.loc[~pop_mask, "area"], state_df.loc[~pop_mask, "population"],
            color="blue", alpha=0.7, label="Population <= 10M")
plt.scatter(state_df.loc[pop_mask, "area"], state_df.loc[pop_mask, "population"],
            color="red", alpha=0.7, label="Population > 10M")
plt.xlabel("Area (sq. mi)")
plt.ylabel("Population")
plt.title("State Population vs. Area")
plt.legend()
plt.grid(True)
plt.show()
