class Graph:
      def __init__(self):
            self.nodeLabels = []
            self.edgeLabels = []
            self.edgeNexts = []
      def hasEdge(self,x,a,y):
            isContained = False
            t = 0
            for i in range(len(self.nodeLabels)):
                  if self.nodeLabels[i]==x:
                        t = y
                  elif self.nodeLabels[i]==y:
                        t = x
                  else:
                        continue
                  for j in range(len(self.edgeNexts[i])):
                        if self.edgeLabels[i][j] == a and self.nodeLabels[self.edgeNexts[i][j]] == t:
                              isContained = True
                              return isContained
            return isContained
      def removeEdge(self,x,a,y):
            t = 0
            for i in range(len(self.nodeLabels)):
                  if self.nodeLabels[i]==x:
                        t = y
                  elif self.nodeLabels[i]==y:
                        t = x
                  else:
                        continue
                  for j in range(len(self.edgeNexts[i])):
                        if self.edgeLabels[i][j]==a and self.nodeLabels[self.edgeNexts[i][j]]==t:
                              del self.edgeLabels[i][j]
                              id = self.edgeNexts[i][j]
                              del self.edgeNexts[i][j]
                              for k in range(len(self.edgeNexts[id])):
                                    if self.edgeNexts[id][k]==i:
                                          del self.edgeNexts[id][k]
                                          break;
                              break;

      def constructGraph(self,gd):
            graph = Graph()
            for i in range(len(gd.nodeVisibles)):
                  if gd.nodeVisibles[i]:
                        graph.nodeLabels.append(gd.nodeLabels[i])
                  graph.edgeLabels.append([])
                  graph.edgeNexts.append([])
            for i in range(len(gd.edgeLabels)):
                  if gd.edgeVisibles[i]==True:
                        graph.edgeLabels[gd.edgeX[i]].append(gd.edgeLabels[i])
                        graph.edgeLabels[gd.edgeY[i]].append(gd.edgeLabels[i])
                        graph.edgeNexts[gd.edgeX[i]].append(gd.edgeY[i])
                        graph.edgeNexts[gd.edgeY[i]].append(gd.edgeX[i])
            return graph

















