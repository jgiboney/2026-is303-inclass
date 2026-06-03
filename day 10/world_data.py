import pandas as pd
df = pd.read_csv("day 9/world_development_data.csv")
df["region"] = df["region"].str.title().str.strip()
df["gdp_per_capita"] = pd.to_numeric(
    df["gdp_per_capita"].astype(str).str.replace(",", ""), errors="coerce"
)


print(df.groupby("region")["life_expectancy"].mean())

# 1
print(df.groupby("region")["literacy_rate"].mean())
print(df.groupby("region")["literacy_rate"].mean().idxmin())

# 2
print(df.groupby("region")["population_thousands"].sum().sort_values(ascending=False))

# 3
print(df.groupby("region")["country"].count())

# 4
print(df.groupby("region")["life_expectancy"].max())
print(df.loc[df["life_expectancy"].idxmax()])

# 5
gtr_70 = df[df["life_expectancy"] > 70]
ls_60 = df[df["life_expectancy"] < 60]
print(f"{gtr_70["gdp_per_capita"].mean():.2f}")
print(f"{ls_60["gdp_per_capita"].mean():.2f}")
print(gtr_70[["country", "gdp_per_capita"]])

# 6
df["total_gdp"] = df["gdp_per_capita"] * df["population_thousands"]
print(df.groupby("region")["total_gdp"].sum().max())
print(df.groupby("region")["total_gdp"].sum().idxmax())