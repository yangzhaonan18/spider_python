# import xlwt
#
# f = xlwt.Workbook()  # 创建工作薄
# # 创建个人信息表
# sheet1 = f.add_sheet(u'JD-python', cell_overwrite_ok=True)
# rowTitle = [u'编号', u'姓名', u'性别', u'年龄']
# rowDatas = [[u'小明', u'男', u'18'], [u'小黄', u'女', u'20'], [u'小张', u'男', u'38'], [u'小李', u'男', u'88']]
#
# for i in range(0, len(rowTitle)):
#     sheet1.write(0, i, rowTitle[i])
#
# for k in range(0, len(rowDatas)):  # 先遍历外层的集合，即每行数据
#     rowDatas[k].insert(0, k + 1)  # 每一行数据插上编号即为每一个人插上编号
#     for j in range(0, len(rowDatas[k])):  # 再遍历内层集合
#         sheet1.write(k + 1, j, rowDatas[k][j])  # 写入数据,k+1表示先去掉标题行，另外每一行数据也会变化,j正好表示第一列数据的变化，rowdatas[k][j] 插入数据
#
# # # 创建个人收入表
# # sheet1 = f.add_sheet(u'个人收入表', cell_overwrite_ok=True)
# # rowTitle2 = [u'编号', u'姓名', u'学历', u'工资']
# # rowDatas2 = [[u'小明', u'本科', u'8000'], [u'小黄', u'硕士', u'10000'], [u'小张', u'博士', u'20000'], [u'小李', u'教授', u'50000']]
# #
# # for i in range(0, len(rowTitle2)):
# #     sheet1.write(0, i, rowTitle2[i])
# #
# # for k in range(0, len(rowDatas2)):  # 先遍历外层的集合
# #     rowDatas2[k].insert(0, k + 1)  # 每一行数据插上编号即为每一个人插上编号
# #     for j in range(0, len(rowDatas2[k])):  # 再遍历内层集合
# #         sheet1.write(k + 1, j, rowDatas2[k][j])  # 写入数据,k+1表示先去掉标题行，另外每一行数据也会变化,j正好表示第一列数据的变化，rowdatas[k][j] 插入数据
#
# f.save('H:\excel.xlsx')


plt = [('', 'Python', '数据分析与挖掘实战')]
plt = "".join(list((plt[0])))
print(plt)