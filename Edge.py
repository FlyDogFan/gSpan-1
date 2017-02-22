#!/usr/bin/python
#!coding:UTF-8
class Edge:
      edge_equal = 0
      edge_smaller = 1
      edge_larger = 2
      def __init__(self,ix,iy,x,a,y):
            self.ix = ix
            self.iy = iy
            self.x = x
            self.a = a
            self.y = y

      def compareWith(self,edge):
            result = Edge.edge_equal
            array1 = [self.ix,self.iy,self.x,self.y,self.a]
            array2 = [edge.ix,edge.iy,edge.x,edge.y,edge.a]
            for i in range(len(array1)):
                  if array1[i]<array2[i]:
                        result = Edge.edge_smaller
                        break;
                  elif array1[i]>array2[i]:
                        result = Edge.edge_larger
                        break;
                  else: continue
            return result


class EdgeFrequency:
      def __init__(self, nodeLabelNum, edgeLabelNum):
            self.nodeLabelNum = nodeLabelNum
            self.edgeLabelNum = edgeLabelNum
            self.edgeFreqCount = [0] * nodeLabelNum
            for i in range(len(self.edgeFreqCount)):
                  self.edgeFreqCount[i] = [0] * edgeLabelNum
                  for j in range(len(self.edgeFreqCount[i])):
                        self.edgeFreqCount[i][j] = [0] * nodeLabelNum