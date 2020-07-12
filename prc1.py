import itertools
import pprint

data = ["A","E","I","K","M","N","O","R","U","W"]

pl_pairs = []

def listExcludedIndices(data, indices=[]):
  return [x for i, x in enumerate(data) if i not in indices]

result = []
for i in range(len(data)):
  for j in range(len(data) - 1):
    for k in range(len(data) - 2):
      for l in range(len(data) - 3):
        for m in range(len(data) - 4):
          for n in range(len(data) - 5):
            jData = listExcludedIndices(data, [i])
            kData = listExcludedIndices(jData, [j])
            lData = listExcludedIndices(kData, [k])
            mData = listExcludedIndices(lData, [l])
            nData = listExcludedIndices(mData, [m])
            result.append([data[i], jData[j], kData[k], lData[l], mData[m], nData[n]])




with open('file.txt', 'w') as f:
  print(result, file=f)