from wordcloud import WordCloud
import matplotlib.pyplot as plt

text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")

wordcloud=WordCloud(width=1000,height=800,background_color='orange',colormap='Blues',margin=0).generate(text) 

plt.imshow(wordcloud, interpolation='bilinear')

plt.axis('off')     ## gives the horizontal and vertical scale if axis =’off’ by default it is on 

plt.margins(x=0,y=0)
plt.show()
