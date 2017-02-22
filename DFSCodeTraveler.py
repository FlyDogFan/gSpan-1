#!/usr/bin/python
#!coding:UTF-8
from Stack import *
from Edge import *

class DFSCodeTraveler:
      def __init__(self,edgeSeqs,graph):
            self.g2s = []
            self.f = []
            self.isMin = True
            self.edgeSeqs = edgeSeqs
            self.graph = graph
      def traveler(self):
            nodeLNums = len(self.graph.nodeLabels)
            self.g2s = [-1]*nodeLNums
            self.f = [[False]*nodeLNums]*nodeLNums
            for i in range(nodeLNums):
                  if self.graph.nodeLabels[i]>self.edgeSeqs[0].x:
                        continue
                  self.g2s[i] = 0
                  stack = Stack()
                  stack.push(i)
                  self.dfsSearch(stack,0,1)
                  if not self.isMin:
                        return
                  self.g2s[i] = -1

      def dfsSearch(self,stack,currentPosition,next):
            if currentPosition>=len(self.edgeSeqs):
                  stack.pop()
                  return
            while not stack.isEmpty():
                  x = stack.pop()
                  for i in range(len(self.graph.edgeNexts[x])):
                        y = self.graph.edgeNexts[x][i]
                        if self.f[x][y] or self.f[y][x]:
                              continue
                        if self.g2s[y]<0:
                              edge = Edge(self.g2s[x],next,self.graph.nodeLabels[x],
                                          self.graph.edgeLabels[x][i],self.graph.nodeLabels[y])
                              compareResult = edge.compareWith(self.edgeSeqs[currentPosition])
                              if compareResult==Edge.edge_smaller:
                                    self.isMin = False
                                    return
                              elif compareResult==Edge.edge_larger:
                                    continue
                              self.g2s[y] = next
                              self.f[x][y] = True
                              self.f[y][x] = True
                              stack.push(y)
                              self.dfsSearch(stack,currentPosition+1,next+1)
                              if self.isMin!=True:
                                    return
                              self.f[x][y] = False
                              self.f[y][x] = False
                              self.g2s[y] = -1
                        else:
                              edge = Edge(self.g2s[x],self.g2s[y],self.graph.nodeLabels[x],
                                          self.graph.edgeLabels[x][i],self.graph.nodeLabels[y])
                              compareResult = edge.compareWith(self.edgeSeqs[currentPosition])
                              if compareResult==Edge.edge_smaller:
                                    self.isMin = False;
                                    return
                              elif compareResult==Edge.edge_larger:
                                    continue
                              self.g2s[y] = next
                              self.f[x][y] = True
                              self.f[y][x] = True
                              stack.push(y)
                              self.dfsSearch(stack,currentPosition+1,next)
                              if self.isMin!=True:
                                  return
                              self.f[x][y] = False
                              self.f[x][y] = False