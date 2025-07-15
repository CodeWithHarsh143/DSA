class Treenodes:
  def __init__(self,node):
    self.node=node
    self.left=None
    self.right=None
#For creating a tree(not for visilize)
tree_tuple=(((5,3,None),2,(None,4,6)),1,((11,9,12),8,(13,10,14)))
def parse_tree(data):
  if isinstance(data,tuple) and len(data)==3:
    node=Treenodes(data[1])
    node.left=parse_tree(data[0])
    node.right=parse_tree(data[2])
    return node
  elif data is None:
    return None
  else:
    return Treenodes(data)
tree=parse_tree(tree_tuple)
# this is for test of creating a tree!!!
test_cases = [
    {"input": {"nodes": tree.left.left.node}, "output": 5},
    {"input": {"nodes": tree.right.right.node}, "output": 10},
    {"input": {"nodes": tree.right.node}, "output": 8},
    {"input": {"nodes": tree.right.left.right.node}, "output": 12},
    {"input": {"nodes": tree.right.right.right.node}, "output": 14},
]

correct=0
incorrect=0
total=0
for idx,test in enumerate(test_cases):
    result=test["input"]["nodes"]
    expected=test["output"]
    total+=1
    if result==expected:
         print(f"Test case {idx+1}: ✅ Passed")
         correct+=1
    else:
        print(f"Test case {idx+1}: ❌ Failed (Expected: {expected}, got :{result})")
        incorrect += 1

print(f"\nTotal: {total}, Correct: {correct}, Incorrect: {incorrect}")


# for returning a tuple from created tree!!!
def tree_to_tuple(node):
   if node is None:
      return None
   if node.left is None and  node.right is None:
      return node.node # return 1 (use key also but for that you have to add key in init function in class)
   return tree_to_tuple(node.left),node.node,tree_to_tuple(node.right)

tree2=tree_to_tuple(parse_tree(tree_tuple))# this return the tuple from table!!!
print(tree2)

# for visiulizing the tree!!!
def display_tree(node,space="\t",level=0):
   # if tree is empty!
   if node is None:
      print(space*level+"@") # @ means zero(or nothing)
      return
   # if tree is leaf!
   if node.left is None and node.right is None:
      print(space*level+str(node.node))
      return
   
   display_tree(node.right,space,level+1)# it display the right subtree!

   print(space*level+str(node.node)) # it display the top node (or main) of tree!

   display_tree(node.left,space,level+1)# it display the  left sub tree!

display_tree(tree," ")# it will create the display model of tree(but we have to rotate pie/2(or ninty degree) mentally)



    


   


