import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns  # hanya ditambah seaborn untuk warna dan legend

df = pd.read_csv("food_sales_dataset.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

sales_by_category = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
sales_by_month = df.resample("M", on="Order_Date")["Total_Sales"].sum()

def format_juta(x, _):
    return f"{x/1e6:.1f} jt"

def format_juta_tanpa_koma(x, _):
    return f"{x/1e6:.0f} jt"

def format_ribuan(x, _):
    return f"{int(x):,}".replace(",", ".")

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Analisis Penjualan Toko By Lesmana", fontsize=27, fontweight="bold")

axs[0, 0].bar(sales_by_category.index, sales_by_category.values, color="skyblue", edgecolor="black")
axs[0, 0].set_title("Total Penjualan per Kategori")
axs[0, 0].set_xlabel("Kategori")
axs[0, 0].set_ylabel("Total Penjualan (Juta Rp)")
axs[0, 0].grid(axis="y", linestyle="--", alpha=0.7)
axs[0, 0].yaxis.set_major_formatter(mticker.FuncFormatter(format_juta_tanpa_koma))

colors = ["#4ddf20", "#2fbaf6", "#e2f727", "#db1f1f"]
explode = [0.25 if cat == "Dessert" else 0 for cat in sales_by_category.index]
axs[0, 1].pie(
    sales_by_category.values,
    labels=sales_by_category.index,
    autopct="%1.1f%%",
    colors=colors,
    shadow=True,
    explode=explode,
    startangle=140,
    textprops={'fontsize': 10, 'fontweight': 'bold'}
)
axs[0, 1].set_title("Persentase Penjualan per Kategori")

axs[1, 0].plot(sales_by_month.index, sales_by_month.values, marker="o", linestyle="-", color="green")
axs[1, 0].set_title("Tren Penjualan per Bulan")
axs[1, 0].set_xlabel("Bulan")
axs[1, 0].set_ylabel("Total Penjualan (Juta Rp)")
axs[1, 0].grid(True, linestyle="--", alpha=0.7)
axs[1, 0].yaxis.set_major_formatter(mticker.FuncFormatter(format_juta))

sns.set_palette("bright")  # warna tajam
sns.scatterplot(
    data=df,
    x="Price",
    y="Total_Sales",
    hue="Category",         # warna berdasarkan kategori
    s=70,
    alpha=0.8,
    edgecolor="black",
    ax=axs[1, 1]
)
axs[1, 1].set_title("Harga vs Total Penjualan per Transaksi")
axs[1, 1].set_xlabel("Harga Produk (Rp)")
axs[1, 1].set_ylabel("Total Penjualan (Rp)")
axs[1, 1].grid(True, linestyle="--", alpha=0.7)
axs[1, 1].xaxis.set_major_formatter(mticker.FuncFormatter(format_ribuan))
axs[1, 1].yaxis.set_major_formatter(mticker.FuncFormatter(format_ribuan))
axs[1, 1].legend(title="Kategori Produk", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

