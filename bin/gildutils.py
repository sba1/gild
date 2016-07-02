"""Some simple utils for gild"""

import os.path
import sys

def find_component_base(component):
	"""Returns the base directory of the given component or exits the program"""
	root = os.getcwd()
	while True:
		base = os.path.join(root, component)
		if os.path.isdir(base): break
		last_root = root
		root = os.path.dirname(root)
		if root == last_root: sys.exit("No gild folder structure found.")
	return base
