#!/usr/bin/python
#!coding:UTF-8
from Graph import *
from Edge import *
class SubChildTraveler:
      def __init__(self,edgeSeq,graph):
            self.g2s = []
            self.s2g = []  # 图中边是否被用的情况
            self.f = []  # 最右路径，rm[id] 表示的是此id节点在最右路径中的下一个节点id
            self.rm = []  # 下一个五元组的id
            self.next1 = 0;
            self.edgeSeq = edgeSeq
            self.graph = graph
            self.childEdge = []
      def traveler(self):
            self.next1 = len(self.edgeSeq)+1
            size = len(self.graph.nodeLabels)
            self.g2s = [-1]*size
            self.s2g = [-1]*size
            self.f = [[False]*size]*size
            self.rm = [-1]*(len(self.edgeSeq)+1)
            for edge in self.edgeSeq:
                  if edge.ix<edge.iy and edge.iy>self.rm[edge.ix]:
                        self.rm[edge.ix] = edge.iy
            for i in range(size):
                  if self.edgeSeq[0].x!=self.graph.nodeLabels[i]:
                        continue
                  self.g2s[i] = 0
                  self.s2g[0] = i
                  self.dfsSearchEdge(0)
                  self.g2s[i] = -1
                  self.s2g[0] = -1
      def dfsSearchEdge(self,currentPosition):
            if currentPosition>= len(self.edgeSeq):
                  rmPosition = 0
                  while rmPosition>=0:
                        gId = self.s2g[rmPosition]
                        for i in range(len(self.graph.edgeNexts[gId])):
                              gId2 = self.graph.edgeNexts[gId][i]
                              if self.f[gId][gId2]:
                                    continue
                              if self.g2s[gId2]<0:
                                    self.g2s[gId2] = self.next1
                                    edge = Edge(self.g2s[gId],self.g2s[gId2],self.graph.nodeLabels[gId],
                                                self.graph.edgeLabels[gId][i],self.graph.nodeLabels[gId2])
                                    self.childEdge.append(edge)
                              else:
                                    flag = True
                                    for j in range(len(self.graph.edgeNexts[gId2])):
                                          tempId = self.graph.edgeNexts[gId2][j]
                                          if self.g2s[gId2]<self.g2s[tempId]:
                                                flag = False
                                                break;
                                    if flag:
                                          edge = Edge(self.g2s[gId],self.g2s[gId2],self.graph.nodeLabels[gId],
                                                      self.graph.edgeLabels[gId][i],self.graph.nodeLabels[gId2])
                                          self.childEdge.append(edge)
                        rmPosition = self.rm[rmPosition]
                  return ;
            edge = self.edgeSeq[currentPosition]
            y = edge.y
            a = edge.a
            gId1 = self.s2g[edge.ix]
            for i in range(len(self.graph.edgeLabels[gId1])):
                  if self.graph.edgeLabels[gId1][i]!=a:
                        continue
                  tempId = self.graph.edgeNexts[gId1][i]
                  if self.graph.nodeLabels[tempId]!=y:
                        continue
                  gId2 = tempId
                  if self.g2s[gId2]==-1 and self.s2g[edge.iy]==-1:
                        self.g2s[gId2] = edge.iy
                        self.s2g[gId2] = gId2
                        self.f[gId1][gId2] = True
                        self.f[gId2][gId1] = True
                        self.dfsSearchEdge(currentPosition+1)
                        self.f[gId1][gId2] = False
                        self.f[gId2][gId1] = False
                        self.g2s[gId2] = -1
                        self.s2g[edge.iy] = -1
                  else:
                        if self.g2s[gId2]!=edge.iy:
                              continue
                        if self.s2g[edge.iy]!=gId2:
                              continue
                        self.f[gId1][gId2] = True
                        self.f[gId2][gId1] = True
                        self.dfsSearchEdge(currentPosition)
                        self.f[gId1][gId2] = False
                        self.f[gId2][gId1] = False































