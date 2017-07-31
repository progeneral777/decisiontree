import xlrd
import xlwt
import os.path
import math

MIN_SUPPORT = 0.3

def setnode(catnum):
    samples = []
    for t,x in enumerate(explikes):
        samples.append([newscatlikes[t][catnum-1],x])
    dic = {"nodeid":1,"idenfea":None,"fealeft":[num for num in range(1,15)],"TorF":"not here","purity":"not here","support":1,"data": samples,"likefea":'not here'}
    return dic
        

def entropyplus(exp,node):
    print('calculate entropyplus')
    total = len(node['data'])
    tlist = []
    flist = []
    for x in node['data']:
        #print(exp,x)
        if x[1][exp-1]==1:
            tlist.append(x)
        else:
            flist.append(x)
    tamount = len(tlist)
    famount = len(flist)
    if total ==0:
        value =0
        return value
    #print(tamount,famount)
    value =tamount/total*(-1)*entropy(tlist) + famount/total*(-1)*entropy(flist)
    #print("entropyplus:  ",value)
    return value
     


def entropy(nums):
    catlike = 0
    value = 0
    for n in nums:
        if n[0] == 1:
            catlike +=1
    catdislike = len(nums) - catlike
    #print(len(nums),catlike,catdislike)
    if len(nums) == 0:
        value = 0
    elif catlike == 0:
        catdislike/len(nums)*math.log(catdislike/len(nums),2)
    elif catdislike == 0: 
        value = catlike/len(nums)*math.log(catlike/len(nums),2) 
    else:
        value = catlike/len(nums)*math.log(catlike/len(nums),2) + catdislike/len(nums)*math.log(catdislike/len(nums),2)
    return value

def divide(exp,node):
    t = []
    f = []
    for n in node['data']:
        if n[1][exp-1] == 1:
            t.append(n)
        else:
            f.append(n)
    #print("t,f",t,f)
    #calculate which has more likes, then set to right node
    tlikes = sum([int(x[0]) for x in t ])
    flikes = sum([int(x[0]) for x in f ])
    print("t,,tlikes,f, flikes      ",len(t),tlikes,len(f),flikes)


    tnode = {}
    #print(tnode)
    tnode['data'] = t
    tnode['fealeft'] = [x for x in node['fealeft'] if x !=exp]
    tnode['support'] = len(t)/len(explikes)
    tnode['idenfea'] = 'no'
    tnode['likefea'] = 'yes'    

    fnode = {}
    fnode['data'] = f
    fnode['fealeft'] = [x for x in node['fealeft'] if x !=exp]
    fnode['support'] = len(f)/len(explikes)
    fnode['idenfea'] = 'no'
    fnode['likefea'] = 'no'


    if tlikes>= flikes:
        tnode['nodeid'] = 2*node['nodeid'] +1
        #print('t nodeid  ',tnode['nodeid'])
        tnode['TorF'] = 'T'
        if len(t) == 0:
            tnode['purity'] = 0
        else:
            tnode['purity'] = tlikes/len(t)

        fnode['nodeid'] = 2*node['nodeid']
        #print('f nodeid  ',fnode['nodeid'])
        fnode['TorF'] = 'F'
        if len(f) == 0:
            fnode['purity'] = 0
        else:
            fnode['purity'] = (len(f) - flikes)/len(f)
        #print("return    ",[tnode,fnode])
        return [fnode,tnode]
    else:
        tnode['nodeid'] = 2*node['nodeid'] 
        #print('nodeid  ',tnode['nodeid'])
        tnode['TorF'] = 'F'
        if len(t) == 0:
            tnode['purity'] = 0
        else:
            tnode['purity'] = (len(t)- tlikes)/len(t)

        fnode['nodeid'] = 2*node['nodeid'] +1
        fnode['TorF'] = 'T'
        if len(f) == 0:
            fnode['purity'] = 0
        else:
            fnode['purity'] =  flikes/len(f)
        
        #print("return    ",[tnode,fnode])
        return[tnode,fnode]

def change(dic):
    print("dic",dic)
    value ='id:  '+ str(dic['nodeid']) +'\n' +'喜歡新聞類別:  '+ dic["TorF"] + '\n' +"喜歡體驗: "+str(dic['likefea'])  +'\n'+ "feature"+str(expchi[dic["idenfea"]])+'\n'+'purity:' +str( dic['purity']) + '\n' + 'support:  ' +str( dic['support'])
    return value

def tojson(dic):
    data = {"id":1,""}
    
    value = json.dumps()

def getchildren(dic)
    childlist = []
    for r in resultlist:
        if dic['nodeid']*2 == r['nodeid']: 
            {"exp":}
        if dic['nodeid']*2 == r['nodeid']: 

data = xlrd.open_workbook(os.path.join("/home/jimmy/pyprojects/decisiontree/cal.xls"))
cal = data.sheet_by_name("cal");

newschi = {1:'文化藝術',2:'設計與時尚',3:'運動',4:'健康',5:'影視娛樂',6:'旅遊',7:'親子',8:'美食'}
expchi = {0:'no','no':'no',1:'色香味感受',2:'視聽愉悅',3:'美感要素',4:'同情關懷',5:'煽情感受',6:'共鳴感受',7:'震撼性',8:'重大意義',9:'反省檢討',10:'聲援呼應',11:'活動宣傳',12:'持續關注',13:'議題相關性',14:'利害相關'}
xlpos = {1:[1,8],2:[2,3],3:[2,12],4:[3,1],5:[3,6],6:[3,10],7:[3,15],8:[4,0],9:[4,2],10:[4,5],11:[4,7],12:[4,9],13:[4,11],14:[4,14],15:[4,16] }
explikes = []
newscatlikes = []
trees = []
wb = xlwt.Workbook()
rulelist = []
for i in range(1,cal.nrows):
    explikes.append([int(t) for t in list(cal.cell_value(rowx = i,colx = 0))])
    newscatlikes.append([int(t) for t in list(cal.cell_value(rowx = i,colx = 2))])
    
for i in range(1,9):
    node=setnode(i) 
    nodelist = []
    resultlist = []
    jsondata = {}
    nodelist.append(node)
    #print(nodelist)

    while len(nodelist)>0:
        thisnode = nodelist.pop(0)
        #print("nodelist :    ",nodelist)
        #print("thisnode\n",thisnode)
        if 2*thisnode['nodeid'] > 15:
            resultlist.append(thisnode)
            #print('resultlist',resultlist)i
            rulelist.append(thisnode)
        elif thisnode['support']<0.3:
            resultlist.append(thisnode)
            rulelist.append(thisnode)
        else:
            val = [0,0]
            for exp in range(1,15):
                if exp not in thisnode['fealeft']:
                    continue
                ent = entropyplus(exp,thisnode)
                if ent > val[1]:
                    val = [exp,ent]
                    print("largest amount: ",val)
            thisnode['idenfea'] = val[0]
            twonodes = divide(val[0], thisnode)
            #print("twonodes",twonodes)
            nodelist.append(twonodes[0])
            nodelist.append(twonodes[1])
            #print("nodelist :    ",nodelist)

            resultlist.append(thisnode)
            #print('resultlist',resultlist)

    #trees.append([i,resultlist])
    #print("trees",trees)

    ws = wb.add_sheet(newschi[i])
    for r in resultlist:
        print(xlpos[1])
        de = change(r)
        num = r['nodeid']
        two = xlpos[num]
        row = two[0]
        col = two[1]
        print(row, col)
        ws.write(row,col,de)
wb.save('tree.xls')         
