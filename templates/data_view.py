import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI
import uvicorn

api = FastAPI()


class DataView:
    # 画饼状图
    def draw_pie(self, labels, sizes):
        img_url = "static/classify_pie.png"
        # 设置饼图的标签和大小
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        # 设置x,y轴刻度一致，这样饼图才能是圆的
        plt.axis('equal')
        # 解决中文乱码
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 显示图形
        # plt.show()
        plt.savefig(img_url)
        return img_url

    def scene_classify_pie(self):
        labels = ["一级分类", "二级分类", "三级分类", "四级分类", "五级分类", "六级分类", "七级分类", "八级分类",
                  "九级分类", "十级分类"]
        sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return self.draw_pie(labels, sizes)

