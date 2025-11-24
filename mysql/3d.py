import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Connect to MySQL
conn = mysql.connector.connect(
host="db4free.net",
user="georgew",
password="12345george",
database="georgew",
port=3306
)

df = pd.read_sql("SELECT * FROM STUDENT", conn)

# ---- 3D CHART ----
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111, projection='3d')

# Bar positions
x = list(range(len(df)))
y = [0]*len(df)
z = [0]*len(df)

dx = [0.6]*len(df)
dy = [0.6]*len(df)
dz = df["POINTS"]

# Draw bars
ax.bar3d(x, y, z, dx, dy, dz, shade=True)

# Names under bars
ax.set_xticks(x)
ax.set_xticklabels(df["NAME"], rotation=25, ha='right')

ax.set_zlabel("Points")
ax.set_title("3D Student Performance")

# ---- VERTICAL LABELS ON THE SIDE (FACING UPWARD) ----
for i in range(len(df)):
 label = f"{df['POINTS'][i]} | {df['GRADE'][i]}"

ax.text(
    x[i] + dx[i]/2 - 0.15,  # shift slightly left to align with bar
    y[i],                    # same base Y
    dz[i] / 2,               # halfway up the bar
    label,
    ha='center',
    va='center',
    rotation=90,             # rotate upright along the bar
    rotation_mode='anchor',  # ensures rotation is properly anchored
    fontsize=11,
    color="black"
)
plt.tight_layout()
plt.show()
conn.close()