#!/usr/bin/python
#!coding:UTF-8
class GraphData:

      def __init__(self):
            self.nodeLabels = []  # 节点是否可用, 可能被移除
            self.nodeVisibles = []  # 边的集合标号
            self.edgeLabels = []  # 边的一边点id
            self.edgeX = []  # 边的另一边的点id
            self.edgeY = []  # 边是否可用
            self.edgeVisibles = []
      def removeInFreqNodeAndEdge(self,freqNodeLabel,freqEdgeLabel, minSupportCount):
            for i in range(len(self.nodeLabels)):
                  label = self.nodeLabels[i]
                  if freqNodeLabel[label]<minSupportCount:
                        self.nodeVisibles[i] = False
            for i in range(len(self.edgeLabels)):
                  label = self.edgeLabels[i]
                  if freqEdgeLabel[label] < minSupportCount:   #如果小于支持度计数，则此边不可用
                        self.edgeVisibles[i] = False
                        continue
                  x = self.edgeX[i];
                  y = self.edgeY[i];
                  if not self.nodeVisibles[x] or not self.nodeVisibles[y]:
                        self.edgeVisibles[i] = False
      def reLabelByRank(self,nodeLabel2Rank,edgeLabel2Rank):
            count = 0
            oldId2New = [0]*len(self.nodeLabels)
            for i in range(len(self.nodeLabels)):
                  label = self.nodeLabels[i]
                  if self.nodeVisibles[i]==True:
                        self.nodeLabels[i] = nodeLabel2Rank[label]
                        oldId2New[i] = count
                        count +=1
            for i in range(len(self.edgeLabels)):
                  label = self.edgeLabels[i]
                  if self.edgeVisibles[i]==True:
                        self.edgeLabels[i] = edgeLabel2Rank[label]
                        temp = self.edgeX[i]
                        self.edgeX[i] = oldId2New[temp]
                        temp = self.edgeY[i]
                        self.edgeY[i] = oldId2New[temp]

class GraphCode:
      def __init__(self):
            self.edgeSeq = []
            self.gs = []
