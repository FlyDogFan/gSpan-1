#!/usr/bin/python
#!coding:UTF-8
from GSpanTool import *
class gSpan:
      def main(self):
          filePath = "data/graph.data"
          minSupportRate = 0.2
          tool = GSpanTool(filePath,minSupportRate)
          tool.freqGraphMining()

if __name__ == '__main__':
      gspan = gSpan()
      gspan.main()
