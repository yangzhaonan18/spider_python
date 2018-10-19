# -*- coding:utf-8 -*-
# 名称：信息检索作业（杨赵南）
# 时间：2018年10月19日
# 功能：爬取京东的图书信息，并存放在xlsx文件中
# 语言：python3
import requests
import re  # 正则表达式
import xlwt  # 写入xlsx文件时使用


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


def parsePage(ilt, html):
    try:
        html_list = re.findall(r"<li data-sku=[\s\S]*?</li>", html)  # find one
        for i in range(len(html_list)):
            html = html_list[i]
            # print("html:", i, html)
            try:
                plt = re.findall(r"<em>([^\"]*)<font class=\"skcolor_ljg\">([^\"]*)</font>([^\"]*)</em>", html)  # name
                # print(plt)  #  [('', 'Python', '数据分析与挖掘实战')]
                plt = "".join(list((plt[0])))  # 将拆分的书名合在一起，组成完整的书名
                # print(plt)  # Python数据分析与挖掘实战
                elt = re.findall(r"class=\"p-name\">\s*<a target=\"_blank\" title=\"([^\"]*)\"", html)  # instructions
                tlt = re.findall(r"class=\".*?\" data-done=\".*?\"><em>.*?</em><i>([^\"]*)</i>", html)  # price
                clt = re.findall(r"class=\"p-bi-store\" onclick=\"searchlog.*?\"><a title=\"([^\"]*)\"", html)  # press
                nlt = re.findall(r"class=\"p-bi-name\" onclick=\"searchlog.*?\">.*? <a title=\"([^\"]*)\"",
                                 html)  # author

                ilt.append([plt, elt, tlt, clt, nlt])  # 每一本图书的信息存放在一个列表中
            except:
                print("continue")
    except:
        print("continue")


def writeGoodsList(ilt, save_path):
    f = xlwt.Workbook()  # 创建工作薄
    sheet1 = f.add_sheet(u'JD-python', cell_overwrite_ok=True)  # 创建个人信息表
    rowTitle = [u'编号', u'书名', u'说明', u'价格', u'出版社', u'作者']  # 标题信息
    rowDatas = ilt  # 图书信息list
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])

    for k in range(0, len(rowDatas)):  # 先遍历外层的集合，即每行数据
        rowDatas[k].insert(0, k + 1)  # 每一行数据插上编号即为每一个人插上编号
        for j in range(0, len(rowDatas[k])):  # 再遍历内层集合
            sheet1.write(k + 1, j, rowDatas[k][j])  # 写入数据,k+1表示先去掉标题行，另外每一行数据也会变化,j正好表示第一列数据的变化，rowdatas[k][j] 插入数据
    f.save(save_path)


def main():
    goods = "python"  # 京东检索词
    depth = 20  # 京东是两个数字表示一页内容（20 表示有10页内容）
    start_url = "https://search.jd.com/Search?keyword=" + goods + "&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page="
    save_path = 'H:\yangzhaonan_JD_python.xlsx'  # 存放的路径和名称
    infoList = []
    for i in range(1, depth):
        try:
            url = start_url + str(i)  # 构造不同页面的的网址
            html = getHTMLText(url)
            parsePage(infoList, html)  # 解析内容，并将需要的信息存放到列表infoList
        except:
            continue
    writeGoodsList(infoList, save_path)  # 将信息一次性全部存放到xml文件中


if __name__ == "__main__":
    main()
