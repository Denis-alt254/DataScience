import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019'],
    'Searches': [50, 60, 75, 80, 92],
    'Direct': [39, 47, 56, 62, 60],
    'Social Media': [47, 50, 66, 51, 51]
}

df = pd.DataFrame(data)

bar_width = 0.25
x = range(len(df['Month']))

plt.figure(figsize=(10,6))
plt.bar([p - bar_width for p in x], df['Searches'], width=bar_width, label='Searches', color='blue')
plt.bar(x, df['Direct'], width=bar_width, label='Direct', color='orange')
plt.bar([p + bar_width for p in x], df['Social Media'], width=bar_width, label='Social Media', color='pink')

plt.xlabel('Month')
plt.ylabel('Visitors (Thousands)')
plt.title('Visitors by Web Traffic Sources')
plt.xticks(x, df['Month'])
plt.legend()
plt.tight_layout()
plt.show()


print(df)