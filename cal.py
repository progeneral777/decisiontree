import os.path
import xlrd
import xlwt

data = xlrd.open_workbook(os.path.join("/home/jimmy/pyprojects/decisiontree/result.xlsx"))
sh1 = data.sheet_by_name("sh1");
sh2 = data.sheet_by_name("sh2");

explike = []
newslike = []
newstypelike = []

for i in range(1,sh1.nrows-1):

#calculate whether the user likes certain experience
    likes = []
    for x in range(3,17):
        t = str(sh1.cell_value(rowx=i,colx=x))
        t = t.replace(",","").replace(".","").replace("0","")
        #print(t)
        points = list(t)
        #print(points)
        total = sum([int(p) for p in points])
        if total/3.0 < 3:
            likes.append(0)
        else:
            likes.append(1)
        
    explike.append(likes)
    #print(explike)

#calculate whether the user likes certain news
for i in range(1,sh1.nrows-1):
    likes = []
    for x in range(17,25):
        t = str(sh1.cell_value(rowx=i,colx=x))
        t = t.replace(",","").replace(".","").replace("0","")
        print(t)
        points = list(t)[0:4]
        print(points)
        total = sum([int(p) for p in points])
        if total/5.0 < 3:
            likes.append(0)
        else:
            likes.append(1)

    newslike.append(likes)
    print(newslike)

wb = xlwt.Workbook()
ws = wb.add_sheet('cal')

ws.write(0,0,"explike")
ws.write(0,1,"allnewslike")
ws.write(0,2,"5newscatlike")

for i,x in enumerate(explike):
    print(i+1)
    ws.write(i+1,0,''.join([str(num) for num in x]))
 
for i,x in enumerate(newslike):
    ws.write(i+1,2,''.join([str(num) for num in x]))
wb.save('cal.xls')


