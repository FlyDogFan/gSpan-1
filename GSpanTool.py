#!/usr/bin/python
#-*- coding:utf-8 -*-
from GraphData import *
from time import clock
from Graph import *
#from EdgeFrequency import *
from Edge import *
#from GraphCode import *
from DFSCodeTraveler import *
from SubChildTraveler import *
import datetime
#频繁子图挖掘工具类
class GSpanTool:
      def __init__(self,filePath,minSupportRate):
            #文件数据类型
            self.input_new_graph = 't'
            self.input_vertice = 'v'
            self.input_edge = 'e'
            self.label_max = 100  # label max
            self.minSupportRate = minSupportRate
            self.minSupportCount = 0
            self.freqEdgeLabel = []
            self.freqNodeLabel = []
            self.totalGraphDatas = []
            self.resultGraphs = []
            self.totalGraphs = []
            self.newEdgeLabelNum = 0
            self.newNodeLabelNum = 0
            self.ef = EdgeFrequency(self.newNodeLabelNum,self.newEdgeLabelNum)
            self.filePath = filePath
            self.readDataFile()
            #print "size",len(self.totalGraphDatas)
      def readDataFile(self):
            file_object = open(self.filePath)
            dataArray = []
            try:
                  for line in file_object.readlines():
                        tempArray = line.split(" ")
                        dataArray.append(tempArray)
            finally:
                  file_object.close()
            self.calFrequentAndRemove(dataArray)

      def calFrequentAndRemove(self,dataArray):
            tempCount = 0
            self.freqEdgeLabel = [0]*self.label_max
            self.freqNodeLabel = [0]*self.label_max
            gd = None
            for data in dataArray:
                  if data[0]==self.input_new_graph:
                        if gd!=None:
                              self.totalGraphDatas.append(gd)
                        gd = GraphData()
                  elif data[0]==self.input_vertice:
                        if not gd.nodeLabels.__contains__(int(data[2])):
                              tempCount = self.freqNodeLabel[int(data[2])]
                              tempCount +=1
                              self.freqNodeLabel[int(data[2])] = tempCount
                        gd.nodeLabels.append(int(data[2]))
                        gd.nodeVisibles.append(True)
                  elif data[0]==self.input_edge:
                        if not gd.edgeLabels.__contains__(int(data[3])):
                              tempCount = self.freqEdgeLabel[int(data[3])]
                              tempCount +=1
                              self.freqEdgeLabel[int(data[3])] = tempCount
                        i = int(data[1])
                        j = int(data[2])
                        gd.edgeLabels.append(int(data[3]))
                        gd.edgeX.append(i)
                        gd.edgeY.append(j)
                        gd.edgeVisibles.append(True)
            self.totalGraphDatas.append(gd)
            self.minSupportCount = int(self.minSupportRate*len(self.totalGraphDatas))
            for g in self.totalGraphDatas:
                  g.removeInFreqNodeAndEdge(self.freqNodeLabel,self.freqEdgeLabel,self.minSupportCount)
      #根据标号频繁度进行排序并且重新标号
      def sortAndReLabel(self):
            temp = 0
            rankNodeLabels = [0]*self.label_max
            rankEdgeLabels = [0]*self.label_max
            nodeLabel2Rank = [0]*self.label_max
            edgeLabel2Rank = [0]*self.label_max
            for i in range(self.label_max):
                  #表示排名第i位的标号为i，[i]中的i表示排名
                  rankNodeLabels[i] = i
                  rankEdgeLabels[i] = i
            for i in range(len(self.freqNodeLabel)-1):
                  k = 0
                  label1 = rankNodeLabels[i]
                  temp = label1
                  for j in range(i+1,len(self.freqNodeLabel)):
                        label2 = rankNodeLabels[j]
                        if  self.freqNodeLabel[temp]<self.freqNodeLabel[label2]:
                              temp = label2
                              k = j
                  if temp!= label1:
                        #进行i，k排名下的标号对调
                        temp = rankNodeLabels[k]
                        rankNodeLabels[k] = rankNodeLabels[i]
                        rankNodeLabels[i] = temp
            for i in range(len(self.freqEdgeLabel)-1):
                  k = 0
                  label1 = rankEdgeLabels[i]
                  temp = label1
                  for j in range(i+1,len(rankEdgeLabels)):
                        label2 = rankEdgeLabels[j]
                        if self.freqEdgeLabel[temp]<self.freqEdgeLabel[label2]:
                              temp = label2
                              k = j
                  if temp!= label1:
                        temp = rankEdgeLabels[k]
                        rankEdgeLabels[k] = rankEdgeLabels[i]
                        rankEdgeLabels[i] = temp
            for i in range(len(rankNodeLabels)):
                  nodeLabel2Rank[rankNodeLabels[i]] = i
            for i in range(len(rankEdgeLabels)):
                  edgeLabel2Rank[rankEdgeLabels[i]] = i
            for gd in self.totalGraphDatas:
                  gd.reLabelByRank(nodeLabel2Rank,edgeLabel2Rank)
            for i in range(len(rankNodeLabels)):
                  if self.freqNodeLabel[rankNodeLabels[i]]>self.minSupportCount:
                        self.newNodeLabelNum = i
            for i in range(len(rankEdgeLabels)):
                  if self.freqEdgeLabel[rankEdgeLabels[i]]>self.minSupportCount:
                        self.newEdgeLabelNum = i
            self.newNodeLabelNum = self.newNodeLabelNum+1
            self.newEdgeLabelNum = self.newEdgeLabelNum+1
      def freqGraphMining(self):
            startTime = datetime.datetime.now()
            self.sortAndReLabel()
            self.resultGraphs = []
            self.totalGraphs = []

            for gd in self.totalGraphDatas:
                  g = Graph()
                  g = g.constructGraph(gd)
                  self.totalGraphs.append(g)
            self.ef = EdgeFrequency(self.newNodeLabelNum, self.newEdgeLabelNum)
            len1 = self.newNodeLabelNum
            len2 = self.newEdgeLabelNum
            for i in range(len1):
                  for j in range(len2):
                        for k in range(len1):
                              for tempG in self.totalGraphs:
                                    if tempG.hasEdge(i,j,k):
                                          self.ef.edgeFreqCount[i][j][k] =self.ef.edgeFreqCount[i][j][k]+1

            for i in range(self.newNodeLabelNum):
                  for j in range(self.newEdgeLabelNum):
                        for k in range(self.newNodeLabelNum):
                              if self.ef.edgeFreqCount[i][j][k]>=self.minSupportCount:
                                    gc = GraphCode()
                                    edge = Edge(0,1,i,j,k)
                                    gc.edgeSeq.append(edge)
                                    for y in range(len(self.totalGraphs)):
                                          if self.totalGraphs[y].hasEdge(i,j,k):
                                                gc.gs.append(y)
                                    self.subMining(gc,2)
            endTime = datetime.datetime.now()
            print "Execution time:",(endTime-startTime).seconds,"s"
            self.printResultGraphInfo()
      def subMining(self,gc,next):
            graph = Graph()
            for i in range(next):
                  graph.nodeLabels.append(-1)
                  graph.edgeLabels.append([])
                  graph.edgeNexts.append([])
            for i in range(len(gc.edgeSeq)):
                  e = gc.edgeSeq[i]
                  id1 = e.ix
                  id2 = e.iy
                  graph.nodeLabels[id1] = e.x
                  graph.nodeLabels[id2] = e.y
                  graph.edgeLabels[id1].append(e.a)
                  graph.edgeLabels[id2].append(e.a)
                  graph.edgeNexts[id1].append(id2)
                  graph.edgeNexts[id2].append(id1)
            dTraveler = DFSCodeTraveler(gc.edgeSeq,graph)
            dTraveler.traveler()
            if not dTraveler.isMin:
                  return
            self.resultGraphs.append(graph)
            edge2GId = {}
            for i in range(len(gc.gs)):
                  id = gc.gs[i]
                  sct = SubChildTraveler(gc.edgeSeq,self.totalGraphs[id])
                  sct.traveler()
                  edgeArray = sct.childEdge
                  for e2 in edgeArray:
                        if not edge2GId.has_key(e2):
                              gIds = []
                        else:
                              gIds = edge2GId[e2]
                        gIds.append(id)
                        edge2GId[e2] = gIds
            for item in edge2GId.items():
                  e1 = item[0]
                  gIds = item[1]
                  if len(gIds)<self.minSupportCount:
                        continue
                  nGc = GraphCode()
                  nGc.edgeSeq.__add__(gc.edgeSeq)
                  nGc.edgeSeq.append(e1)
                  nGc.gs.__add__(gIds)
                  if e1.iy==next:
                        self.subMining(nGc,next+1)
                  else:
                        self.subMining(nGc,next)
      def printResultGraphInfo(self):
            print "Number of frequent subGraph:",len(self.resultGraphs)



