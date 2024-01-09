import sys

alpha=float(sys.argv[1]) if len(sys.argv)>1 else .5
l1_ratio= float(sys.argv[2]) if len(sys.argv)>1 else .5

print(l1_ratio,alpha)