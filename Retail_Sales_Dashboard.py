import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df=pd.read_excel("retail_sales_matplotlib_minor_project.xlsx")


# # # # Data inspection -Display shape, columns, data types, first 10 rows, summary statistics, missing values, 
# # # # and duplicate Order_ID count. Clean missing or duplicate records if found.
print("========================================================")
print("----------------------Data inspection--------------------- ")
print("========================================================")
print(df.shape)
print(df.columns.tolist())
print(df.info())
print(df.head(10))
print(df.describe())
print(df.isna().sum())
print(df.duplicated("Order_ID").sum())
print("========================================================")

# # # #Q2 — Feature engineering - 
# # # # Prepare useful analysis columns
# # # #   Convert Order_Date to datetime if needed. Create Profit_Margin_Pct = Profit_INR / Net_Sales_INR * 100, 
# # # #   handling zero denominators safely. Create Month_Number to preserve calendar order.
Short_months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}
print("=================================================")
print("----------------Feature engineering ---------------")
print("=================================================")



Profit_Margin_percentage=df["Profit_INR"]/df["Net_Sales_INR"]*100.
print("Profit_Margin_percentage  =  ",Profit_Margin_percentage)

df["Month_Number"] = pd.to_datetime(df["Month"], format="%b").dt.month
print(df["Month_Number"])
print("=================================================")


# # # Q3 — KPI summary
# # # Calculate business KPIs
# # #  Calculate total Net Sales, total Profit, total Orders, total Units, average Order Value, 
# # # average Customer Rating, and Return Rate. Show a neat Pandas summary.
print("=================================================")
print("----------------KPI summary----------------------")
print("=================================================")

Total_Net_sales =df["Net_Sales_INR"].sum()
print("Total_Net_sales  =  ",Total_Net_sales)

Total_profit = df["Profit_INR"].sum()
print("Total_profit  =  ",Total_profit)

Total_orders=df["Order_ID"].nunique()
print("Total_orders  =  ",Total_orders)

total_Units=df["Units"].sum()
print("total_Units  =  ",total_Units)

average_order=df["Units"].mean()
print("average_order  =  ",average_order)

Average_customer_rating=df["Customer_Rating"].mean()
print(" Average_customer_rating  =  ",Average_customer_rating)

Total_return=df["Returned"].count()
print("Total_return  =  ",Total_return)

Return_Rate=(Total_return)/(Total_orders)*100
print("Return_Rate  =  ",Return_Rate)

print("=================================================")

# # Q4 — Monthly trend
# # Analyze monthly sales and profit
# # Group by month and calculate Net_Sales_INR and Profit_INR totals. Plot sales and profit
# # as two lines in one chart or separate subplots. Add title, labels, markers, colors, grid, and legend.

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Total = ["2L", "7L", "12L", "17L", "22L", "27L", "32L", "37L", "42L", "47L","50L"]


Sales_inr=df.groupby("Month_Number")["Net_Sales_INR"].sum()



Profit_inr=df.groupby("Month_Number")["Profit_INR"].sum()
print(Profit_inr)
plt.figure(figsize=(10,6))
plt.plot(Sales_inr.index,Sales_inr.values,marker="*",color="Blue",label="Sales")
plt.xticks(range(1,13),labels=month_names,weight=12,color="#2D3748",fontsize=10)

plt.text(1,4400000," ₹ 4356892",fontsize=9)
plt.text(2,4200000," ₹ 4128793",fontsize=9)
plt.text(3,3200000," ₹ 3114912",fontsize=9)
plt.text(4,4700000," ₹ 4648282",fontsize=9)
plt.text(5,2200000," ₹ 2138591",fontsize=9)
plt.text(6,4700000," ₹ 4639741",fontsize=9)
plt.text(7,3700000," ₹ 3823858",fontsize=9)
plt.text(8,4600000," ₹ 4505341",fontsize=9)
plt.text(9,2600000," ₹ 2541882",fontsize=9)
plt.text(10,4800000," ₹ 4734604",fontsize=9)
plt.text(11,3700000," ₹ 3621247",fontsize=9)
plt.text(12,5000000," ₹ 4978264",fontsize=9)

plt.plot(Sales_inr.index,Profit_inr.values,marker="o",color="Green",label="Profit")

plt.text(1 ,800000 ,"₹ 1160602",fontsize=9)
plt.text(2 ,1200000,"₹ 1128130",fontsize=9)
plt.text(3,700000,"₹ 858289",fontsize=9)
plt.text(4,1300000,"₹ 1236440",fontsize=9)
plt.text(5,400000,"₹ 595579",fontsize=9)
plt.text(6,1400000,"₹ 1351547",fontsize=9)
plt.text(7,800000,"₹ 1003400",fontsize=9)
plt.text(8,1200000,"₹ 1169098",fontsize=9)
plt.text(9,500000,"₹ 685203",fontsize=9)
plt.text(10,1400000,"₹ 1331549",fontsize=9)
plt.text(11,800000,"₹ 911942",fontsize=9)
plt.text(12,1400000,"₹ 1325369",fontsize=9)


plt.yticks(range(100000,5100000,300000),color="#1A365D")
plt.xlabel("Month",color="#1A365D",weight="bold")
plt.ylabel("Rupees in Lakhs  ",color="#1A365D",weight="bold")
plt.title("Monthly Sales & Profit Performance", color="#0F2B52", fontweight="bold", pad=15)
plt.grid(True, linestyle="--", alpha=0.5, color="#CBD5E0")
plt.legend(facecolor="#FFFFFF", edgecolor="#CBD5E0", loc="upper left")
plt.ticklabel_format(style="plain",axis="y")
plt.savefig("Monthly_trend.png")
plt.show()

# # #Q5 — Product analysis
# #Find best-selling products
# #Group by Product and calculate total net sales, profit, units sold, and average rating. Sort by net sales descending. 
# # Plot top 8 products in a bar chart. Use plt.text() to show values above bars.

b = df.groupby("Product").agg({
    "Net_Sales_INR": "sum",
    "Profit_INR": "sum",
    "Units": "sum",
    "Customer_Rating": "mean"
})


top_8 = b.sort_values("Net_Sales_INR", ascending=False).head(8)
print(top_8)


colors = plt.cm.Blues(np.linspace(0.8, 0.3, len(top_8)))


plt.figure(figsize=(10, 8))
bars = plt.bar(top_8.index, top_8["Net_Sales_INR"], color=colors, edgecolor="black")
plt.bar_label(bars, fmt="%.0f")

plt.title("Top 8 Best-Selling Products by Net Sales", fontsize=14, fontweight="bold")
plt.xticks(rotation=35, fontsize=10)
plt.xlabel("Product Names", fontsize=11, weight="bold")
plt.ylabel("Net Sales (INR in Lakhs)", fontsize=11, weight="bold")

plt.yticks(range(1000000, 1700000, 1500000))
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("Product_analysis.png")
plt.show()

# Q6 — City performance
# Compare city performance
# Group by City and calculate net sales, profit, order count, and average rating. 
# Sort cities by net sales. Create a horizontal bar chart and set suitable axis limits and ticks.


Calculated_net_sales=df.groupby("City")["Net_Sales_INR"].sum()
calculated_Profit=df.groupby("City")["Profit_INR"].sum()
Calculated_Order_count=df.groupby("City")["Order_ID"].count()
calculated_Rating=df.groupby("City")["Customer_Rating"].mean()
sorted_city=Calculated_net_sales.sort_values(ascending=True)
plt.figure(figsize=(10,6))
a=plt.barh(sorted_city.index,sorted_city.values,color="#8A810D")
plt.bar_label(a,fmt="%.0f")
plt.title(" Comparing city performance",color="#140664",fontsize=14,weight="bold")
plt.ylabel("City",color="#020001",fontsize=14)
plt.xlabel("Net_Sales_inr",color="#0C0109",fontsize=11,weight="bold")
plt.xticks(range(1000000,8000000,1000000))
plt.ticklabel_format(style="plain",axis="x")
plt.savefig("City_Performance.png")
plt.show()


# # Q7 — Category contribution
# # Analyze category revenue share
# # Calculate each Category's share of total Net Sales. Create a pie chart with labels
#  autopct='%1.1f%%', distinct colors, and startangle=90. 
# Change individual category label colors using the texts returned by plt.pie().

Category_type=df.groupby("Category")["Net_Sales_INR"].sum()

plt.pie(Category_type.values,labels=Category_type.index,autopct="%1.1f%%", wedgeprops={'edgecolor': 'white', 'linewidth': 2})
plt.title("Analyze category revenue share",color="#07000FFF",fontsize=14,weight="bold")
plt.grid()

plt.suptitle("Retail Sales Dashboard",fontsize=20,color="royalblue",fontweight="bold")
plt.tight_layout()
plt.savefig("Category_Contribution.png")
plt.show()

# # Q8 — Sales channel analysis
# # Compare sales channels
# # Compare total net sales and order counts across Sales_Channel. Identify the best channel using Pandas.
# # Plot a bar chart with title, labels, colors, grid, and legend.

compare_sales_channel=df.groupby("Sales_Channel")["Order_ID"].count()
print(compare_sales_channel)
comapre_net_sales=df.groupby("Sales_Channel")["Net_Sales_INR"].sum()
print(comapre_net_sales)

print(compare_sales_channel.idxmax())
print(comapre_net_sales.idxmax())
plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
barss=plt.bar(compare_sales_channel.index,compare_sales_channel.values,label="Order Count",color="#3B82F6")
plt.bar_label(barss)
plt.title("Order Count by Sales Channel",color="#680C33",fontsize=17,weight="bold")
plt.xlabel("Sales Channel",color="#210457",fontsize=11)
plt.ylabel("Number of Orders",color="#2A0653",fontsize=11)
plt.legend()
plt.grid(axis="y")

plt.subplot(1,2,2)
bar=plt.bar(comapre_net_sales.index,comapre_net_sales.values,label="Net Sales",color="#10B981")
plt.bar_label(bar,fmt="%.0f")
plt.title("Net Sales by Sales Channel",color="#640D39", fontsize=17,)
plt.xlabel("Sales Channel", color="#1408B1",fontsize=11)
plt.ylabel("Net Sales (INR)", color="#220686",fontsize=11)
plt.ticklabel_format(style="plain", axis="y")
plt.suptitle("Compare sales channels",fontsize=20,weight="bold",color="#3D0358")
plt.tight_layout()
plt.savefig("Compare_sales_channels.png")
plt.show()
# # Q9 — Customer ratings
# Understand customer satisfaction
# Calculate rating counts and average rating by Product and by City. 
# Create a histogram of Customer_Rating using bins=5. Explain the overall rating distribution.

Calculate_rating_counts=df["Customer_Rating"].count()
calculate_average_rating=df.groupby(["City","Product"])["Customer_Rating"].mean()
print(calculate_average_rating)

counts, bins, patches=plt.hist(df["Customer_Rating"],bins=5,color="yellow",edgecolor="red")
plt.title("Distribution of Average Customer Ratings", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Average Customer Rating")
plt.ylabel("Count")
for patch in patches:
    height = patch.get_height() 
    if height > 0:              
      
        plt.text(patch.get_x() + patch.get_width()/2, height + 0.5, 
                 f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.savefig("Customer_satisfaction.png")
plt.show()


# # Q10 — Discount and profit
# # Investigate discounts
# # Group by Discount_Rate and calculate total net sales, total profit, and average profit margin. 
# # Identify the discount level with the highest total profit. Present findings using a bar chart.
# =====================================================================
# Q10 — Discount and Profit Analysis (Clean Labels + Text on Bars)
# =====================================================================

Discount_Rate_Calculation = df.groupby("Discount_Rate").agg({
    "Profit_INR": "sum",
    "Net_Sales_INR": "sum"
})

plt.figure(figsize=(8, 5))

bars = plt.bar(
    Discount_Rate_Calculation.index, 
    Discount_Rate_Calculation["Profit_INR"].values, 
    width=0.03, 
    color="skyblue", 
    edgecolor="black"
)


plt.ticklabel_format(style='plain', axis='y')


for bar in bars:
    height = bar.get_height()
   
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        height + 50000, 
        f'₹{height/1e5:.1f}L', 
        ha='center', 
        va='bottom', 
        fontsize=9, 
        fontweight='bold'
    )


plt.title("Total Profit by Discount Rate", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Discount Rate", fontsize=12, fontweight='bold')
plt.ylabel("Total Profit (INR)", fontsize=12, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("Investigate_discounts.png")
plt.show()
# # Q11 — Returns analysis
# # Study returned orders
# # Compare returned vs non-returned orders. Calculate order counts and net sales by Returned status.
# # Calculate return rate by Product and identify products with the highest return rates.
# =====================================================================
# Q11 — Returns Analysis & Visualization
# =====================================================================
print("========================================================")
print("------------------ Q11: Returns Analysis -----------------")
print("========================================================")

Calculate_order = df.groupby("Returned")["Order_ID"].count()
Calculate_Net_sales = df.groupby("Returned")["Net_Sales_INR"].sum()
print("Order Counts by Return Status:\n", Calculate_order)
print("\nNet Sales by Return Status:\n", Calculate_Net_sales)


product_total = df.groupby("Product")["Order_ID"].count()
product_returns = df[df["Returned"] == "Yes"].groupby("Product")["Order_ID"].count()


returns_df = pd.DataFrame({"Total_Orders": product_total, "Returned_Orders": product_returns}).fillna(0)
returns_df["Return_Rate_Pct"] = (returns_df["Returned_Orders"] / returns_df["Total_Orders"]) * 100

print("\nProduct-wise Return Summary:\n", returns_df)

highest_return_prod = returns_df["Return_Rate_Pct"].idxmax()
print(f"\n★ Product with Highest Return Rate: {highest_return_prod} ({returns_df.loc[highest_return_prod, 'Return_Rate_Pct']:.2f}%)\n")

# =====================================================================
# Matplotlib Chart: Total Orders vs Returned Orders (With Text on Bars)
# =====================================================================
plt.figure(figsize=(11, 6))

x = np.arange(len(returns_df.index))
width = 0.35


bars1 = plt.bar(x - width/2, returns_df["Total_Orders"], width, color="royalblue", edgecolor="black", label="Total Orders")


bars2 = plt.bar(x + width/2, returns_df["Returned_Orders"], width, color="crimson", edgecolor="black", label="Returned Orders")

for bar in bars1:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        height + 2, 
        f'{int(height)}', 
        ha='center', 
        va='bottom', 
        fontsize=9, 
        fontweight='bold'
    )

for bar in bars2:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        height + 0.5, 
        f'{int(height)}', 
        ha='center', 
        va='bottom', 
        fontsize=9, 
        fontweight='bold',
        color='darkred'
    )

plt.title("Product-wise Comparison: Total Orders vs Returned Orders", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Product Name", fontsize=12, fontweight="bold")
plt.ylabel("Number of Orders", fontsize=12, fontweight="bold")
plt.xticks(x, returns_df.index, rotation=30, fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend(fontsize=11, loc="upper right")

plt.tight_layout()
plt.savefig("Return_Analysis.png")
plt.show()
# # # Q12 — Shipping analysis
# # # Analyze shipping performance
# # # Calculate average Shipping_Days by City and Sales_Channel. Identify the slowest 
# # # city and channel. Create a bar chart of average shipping days by city.

  
  
Average_shiping_days=df.groupby("City")["Shipping_Days"].mean()
print(Average_shiping_days,"Shiping_days ")

slowest_city_channels=df.groupby(["City","Sales_Channel"])["Shipping_Days"].mean()
print(slowest_city_channels)
slowest=slowest_city_channels.idxmin()
print(slowest)

c=plt.bar(Average_shiping_days.index,Average_shiping_days.values)
plt.bar_label(c,fmt="%.0f")
plt.xlabel("City",color="Black",fontsize=11,weight="bold")
plt.ylabel("Shipping  Days",color="Black",fontsize=11,weight="bold")
plt.title("Analyze shipping performance",color="black",weight="bold")

plt.savefig("Analyze_shipping_performance.png")
plt.show()


# # # Q13 — Relationship analysis
# # # Study units, sales, and ratings
# # # Create a scatter plot with Units on X-axis and Net_Sales_INR on Y-axis. Discuss the relationship.
# # # Calculate a Pandas correlation matrix for Units, Unit_Price_INR, Net_Sales_INR, Profit_INR, Customer_Rating, and Shipping_Days.

correlation_columns = [
    "Units", 
    "Unit_Price_INR", 
    "Net_Sales_INR", 
    "Profit_INR", 
    "Customer_Rating", 
    "Shipping_Days"
]

scat=df.groupby("Units")["Net_Sales_INR"].sum()
print(scat)
corr_matrix = df[correlation_columns].corr()
print(corr_matrix)
plt.scatter(scat.index,scat.values,color="red")
plt.xlabel("Units",color="Black",fontsize=11,weight="bold")
plt.ylabel("Net_Sales_INR",color="Black",fontsize=11,weight="bold")
plt.title("units_sales",color="black",weight="bold")
plt.text(1,13712156,"13712156",color="red")
plt.text(2,12775334,"12775334",color="red")
plt.text(3,10018790,"10018791",color="red")
plt.text(4,6663221,"6663222",color="red")
plt.text(5,4062908,"4062909",color="red")
plt.grid()
plt.savefig("units_sales.png")
plt.show()


# # # Q14 — Multi-chart dashboard
# # # Build a subplot dashboard
# # # Create one figure with 4 subplots (2 rows × 2 columns): (1) monthly net sales line plot, (2) top 8 products bar chart,
# # # (3) customer rating histogram, (4) category revenue-share pie chart. Give each subplot a title and suitable labels.
# # # Use figsize, plt.tight_layout(), and save as retail_dashboard.png with dpi=300.



# # Q4 — Monthly trend
# # Analyze monthly sales and profit
# # Group by month and calculate Net_Sales_INR and Profit_INR totals. Plot sales and profit
# # as two lines in one chart or separate subplots. Add title, labels, markers, colors, grid, and legend.

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Total = ["2L", "7L", "12L", "17L", "22L", "27L", "32L", "37L", "42L", "47L","50L"]


Sales_inr=df.groupby("Month_Number")["Net_Sales_INR"].sum()



Profit_inr=df.groupby("Month_Number")["Profit_INR"].sum()
print(Profit_inr)
plt.figure(figsize=(15,8))
plt.subplot(2,2,1)
plt.plot(Sales_inr.index,Sales_inr.values,marker="*",color="Blue",label="Sales")
plt.xticks(range(1,13),labels=month_names,weight=12,color="#2D3748",fontsize=10)

plt.text(1,4400000," ₹ 4356892",fontsize=9)
plt.text(2,4200000," ₹ 4128793",fontsize=9)
plt.text(3,3200000," ₹ 3114912",fontsize=9)
plt.text(4,4700000," ₹ 4648282",fontsize=9)
plt.text(5,2200000," ₹ 2138591",fontsize=9)
plt.text(6,4700000," ₹ 4639741",fontsize=9)
plt.text(7,3700000," ₹ 3823858",fontsize=9)
plt.text(8,4600000," ₹ 4505341",fontsize=9)
plt.text(9,2600000," ₹ 2541882",fontsize=9)
plt.text(10,4800000," ₹ 4734604",fontsize=9)
plt.text(11,3700000," ₹ 3621247",fontsize=9)
plt.text(12,5000000," ₹ 4978264",fontsize=9)

plt.plot(Sales_inr.index,Profit_inr.values,marker="o",color="Green",label="Profit")

plt.text(1 ,800000 ,"₹ 1160602",fontsize=9)
plt.text(2 ,1200000,"₹ 1128130",fontsize=9)
plt.text(3,700000,"₹ 858289",fontsize=9)
plt.text(4,1300000,"₹ 1236440",fontsize=9)
plt.text(5,400000,"₹ 595579",fontsize=9)
plt.text(6,1400000,"₹ 1351547",fontsize=9)
plt.text(7,800000,"₹ 1003400",fontsize=9)
plt.text(8,1200000,"₹ 1169098",fontsize=9)
plt.text(9,500000,"₹ 685203",fontsize=9)
plt.text(10,1400000,"₹ 1331549",fontsize=9)
plt.text(11,800000,"₹ 911942",fontsize=9)
plt.text(12,1400000,"₹ 1325369",fontsize=9)


plt.yticks(range(100000,5100000,300000),color="#1A365D")
plt.xlabel("Month",color="#1A365D",weight="bold")
plt.ylabel("Rupees in Lakhs  ",color="#1A365D",weight="bold")
plt.title("Monthly Sales & Profit Performance", color="#0F2B52", fontweight="bold", pad=15)
plt.grid(True, linestyle="--", alpha=0.5, color="#CBD5E0")
plt.legend(facecolor="#FFFFFF", edgecolor="#CBD5E0", loc="upper left")
plt.ticklabel_format(style="plain",axis="y")


# #Q5 — Product analysis
# #Find best-selling products
# #Group by Product and calculate total net sales, profit, units sold, and average rating. Sort by net sales descending. 
# # Plot top 8 products in a bar chart. Use plt.text() to show values above bars.
b = df.groupby("Product").agg({
    "Net_Sales_INR": "sum",
    "Profit_INR": "sum",
    "Units": "sum",
    "Customer_Rating": "mean"
})


top_8 = b.sort_values("Net_Sales_INR", ascending=False).head(8)
print(top_8)

plt.subplot(2,2,2)
colors = plt.cm.Blues(np.linspace(0.8, 0.3, len(top_8)))



bars = plt.bar(top_8.index, top_8["Net_Sales_INR"], color=colors, edgecolor="black")
plt.bar_label(bars, fmt="%.0f")

plt.title("Top 8 Best-Selling Products by Net Sales", fontsize=14, fontweight="bold")
plt.xticks(rotation=35, fontsize=10)
plt.xlabel("Product Names", fontsize=11, weight="bold")
plt.ylabel("Net Sales (INR in Lakhs)", fontsize=11, weight="bold")

plt.yticks(range(1000000, 1700000, 1500000))
plt.grid(True, linestyle="--", alpha=0.5)

# # Q9 — Customer ratings
# Understand customer satisfaction
# Calculate rating counts and average rating by Product and by City. 
# Create a histogram of Customer_Rating using bins=5. Explain the overall rating distribution.

Calculate_rating_counts=df["Customer_Rating"].count()
calculate_average_rating=df.groupby(["City","Product"])["Customer_Rating"].mean()
print(calculate_average_rating)

plt.subplot(2,2,3)
counts, bins, patches=plt.hist(df["Customer_Rating"],bins=5,color="yellow",edgecolor="red")
plt.title("Distribution of Average Customer Ratings", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Average Customer Rating")
plt.ylabel("Count")
for patch in patches:
    height = patch.get_height() 
    if height > 0:              
      
        plt.text(patch.get_x() + patch.get_width()/2, height + 0.5, 
                 f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.savefig("Understand_customer_satisfaction.png")



# Q7 — Category contribution
# Analyze category revenue share
# Calculate each Category's share of total Net Sales. Create a pie chart with labels
#  autopct='%1.1f%%', distinct colors, and startangle=90. 
# Change individual category label colors using the texts returned by plt.pie().

Category_type=df.groupby("Category")["Net_Sales_INR"].sum()
plt.subplot(2,2,4)
plt.pie(Category_type.values,labels=Category_type.index,autopct="%1.1f%%", wedgeprops={'edgecolor': 'white', 'linewidth': 2})
plt.title("Analyze category revenue share",color="#07000FFF",fontsize=14,weight="bold")
plt.grid()

plt.suptitle("Retail Sales Dashboard",fontsize=20,color="royalblue",fontweight="bold")
plt.tight_layout()
plt.suptitle("Retail_Sales_Dashboard",fontsize=20,color="royalblue",weight="bold")
plt.tight_layout()
plt.savefig("Retail_Sales_Dashboard.png",dpi=300)
plt.show()


# Q15 — Final conclusion
# Write business recommendations
# Write 5 evidence-based findings, including best product, best city, best sales channel, 
# return-rate concern, and one recommendation to improve sales or customer satisfaction.

