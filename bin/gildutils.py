"""Some simple utils for gild"""

import glob
import os.path
import subprocess
import sys

if False:
	from typing import Any, List, Iterable

def is_gild_root(path):
	# type: (str) -> bool
	"""Checks if the given path is a valid gild root"""
	urls = glob.glob(os.path.join(path,"*","*.url"))
	return len(urls) > 0

def get_gild_root():
	# type: () -> str
	"""Returns the gild root or None if none could be found."""
	root = os.getcwd()
	while True:
		if is_gild_root(root): return root;
		last_root = root
		root = os.path.dirname(root)
		if root == last_root: sys.exit("No gild folder structure found.")
	return None

def find_component_base(component):
	# type: (str) -> str
	"""Returns the base directory of the given component or exits the program"""
	root = os.getcwd()
	while True:
		base = os.path.join(root, component)
		if os.path.isdir(base): break
		last_root = root
		root = os.path.dirname(root)
		if root == last_root:
			sys.exit("No gild folder structure for requested component '{0}' found.".format(component))
	return base

def get_components():
	# type: () -> List[str]
	"""Returns the names all components."""
	root = get_gild_root()
	if root is None: sys.exit("No gild folder structure found.")
	# FIXME: Should probably return all names without the prefix (instead just the last pathname)
	return [os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(root, "*","*.url"))]

def get_branch_of_current_checkout(component):
	# type: (str) -> str
	"""To a given component, return the base of the branch currently checked out in the repo folder"""
	base = find_component_base(component)
	repo = os.path.join(base, 'repo')
	return subprocess.check_output(["git", "symbolic-ref", "--short", "HEAD"], cwd=repo, encoding='UTF-8').strip()

class PatchSeries(object):
	def __init__(self, branch, checkout, url):
		# type: (str, str, str) -> None
		self.branch = branch
		self.checkout = checkout
		self.url = url

def get_series_of_component(component):
	# type: (str) -> Iterable[PatchSeries]
	"""Return info about all registered patch series for the given component"""
	base = find_component_base(component)
	series = os.path.join(base, "series")
	lines = [line.strip() for line in open(series)]
	for line in lines:
		if line:
		    branch, checkout, url = line.split("\t")
		    yield PatchSeries(branch, checkout, url)

def get_repo_url(component_base):
	# type: (str) -> str
	"""Given the full path to a component, returns it repo URL"""
	return open(os.path.join(component_base, "repo.url")).readline().strip()

# Various completers
def component_completer(**kwargs):
	# type: (Any) -> List[str]
	return sorted(get_components())

def branch_completer(prefix, parsed_args, **kwargs):
	# type: (str, Any, Any) -> List[str]
	return [s.branch for s in get_series_of_component(parsed_args.component)]

def autocomplete(parser):
	# type: (Any) -> None
	"""Calls argcomplete.autocomplete() if available"""
	try:
		import argcomplete
		argcomplete.autocomplete(parser)
	except ImportError:
		pass
