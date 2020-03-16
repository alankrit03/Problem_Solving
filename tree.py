class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None

class binary_search_tree:
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root==None:
			self.root=node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value<cur_node.value:
			if not cur_node.left_child:
				cur_node.left_child=node(value)
			else:
				self._insert(value,cur_node.left_child)
		elif value>cur_node.value:
			if not cur_node.right_child:
				cur_node.right_child=node(value)
			else:
				self._insert(value,cur_node.right_child)
		else:
			print("The value is already in tree!")

	def print_tree(self):
		if self.root:
			self._print_tree(self.root)
	
	def _print_tree(self,cur_node):
		if cur_node:
			
			self._print_tree(cur_node.left_child)
			print(cur_node.value)
			self._print_tree(cur_node.right_child)
			

	def height(self):
		if self.root:
			return self._height(self.root,0)
		else:
			return 0
	def _height(self,cur_node,cur_height):
		if not cur_node:
			return cur_height
		left_height=self._height(cur_node.left_child,cur_height+1)
		right_height=self._height(cur_node.right_child,cur_height+1)
		return max(left_height,right_height)

def fill_tree(tree,num_elems=100,max_int=1000):
	from random import randint
	for i in range(num_elems):
		#cur_elem=randint(0,max_int)
		tree.insert(i)
	return tree

tree = binary_search_tree()
#tree=fill_tree(tree,num_elems=10)
ch='y'
while(ch=='y'):
	ele=int(input("Enter the element: "))
	tree.insert(ele)
	ch=input("Enter 'y' for continue and 'n' for display")

tree.print_tree()

print("tree height is = {}".format(tree.height()))