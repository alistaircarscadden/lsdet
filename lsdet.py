import os
import sys

DIRECTORY = -1
errors = 0

class FileTree:
	def __init__(self, parent, path):
		self.parent = parent
		self.children = []
		self.size = 0
		self.name = os.path.basename(path)
		self.path = path
 
	def head(self):
		if(self.parent == None):
			return True
		return False

	def add_child(self, child):
		self.children.append(child)

def bytes_to_str(bytes):
	suffixes = [' B', ' kB', ' MB', ' GB', ' TB']
	suffix = 0

	while(bytes > 1000):
		bytes /= 1000
		suffix += 1

	return str(bytes) + suffixes[suffix]

def contents(path):
	global errors
	if(os.path.isdir(path)):
		try:
			return os.listdir(path)
		except WindowsError:
			errors += 1
			return None
	else:
		return None

def size(path):
	global errors
	try:
		if(os.path.isdir(path)):
			return DIRECTORY
		else:
			return os.stat(path).st_size
	except WindowsError:
		errors += 1
		return 0

def fill_file_tree(file_tree_node):
	ftn_size = size(file_tree_node.path)

	if(ftn_size == DIRECTORY):
		ftn_contents = contents(file_tree_node.path)

		if(ftn_contents is not None):
			for child_path_basename in ftn_contents:
				child_path_full = file_tree_node.path + '/' + child_path_basename
				child_node = FileTree(file_tree_node, child_path_full)
				file_tree_node.add_child(child_node)
				file_tree_node.size += fill_file_tree(child_node)

	else:
		file_tree_node.size = ftn_size

	return file_tree_node.size

def print_file_tree(file_tree_node, depth, max_depth, only_dirs, detailed_bytes):
	if(detailed_bytes == 1):
		print('    ' * depth + str(file_tree_node.size) + ' B ' + file_tree_node.name)
	else:
		print('    ' * depth + '{:<6}'.format(bytes_to_str(file_tree_node.size)) + ' ' + file_tree_node.name)

	if(depth < max_depth):
		file_tree_node.children.sort(key=lambda i: -i.size)
		num_children = len(file_tree_node.children)
		for i in range(num_children):
			if(only_dirs == 0 or os.path.isdir(file_tree_node.children[i].path)):
				print_file_tree(file_tree_node.children[i], depth + 1, max_depth, only_dirs, detailed_bytes)

if __name__ == '__main__':
	# Help Menu (lsdet help)
	if(len(sys.argv) > 1 and sys.argv[1] == 'help'):
		help = [
			'Usage: lsdet [<path>|path=<path>] [flag=value]...',
			'    no flags defaults to "lsdet ."',
			'\nFlags: (_default_)',
			'    max_depth: 0+ (_1_), Number of layers of subfolders to include in output',
			'    only_dirs: _true_/false, Whether to display only directories or everything',
			'    errors: true/_false_, Whether to display the number of errors',
			'    detailed_bytes: true/_false_, Show 1030204 B instead of 1 MB'
			'\n'
		]
		for line in help:
			print(line)
		exit()

	# Configure Flags
	options = {
		'path': '.',
		'errors': 'false',
		'max_depth': '1',
		'only_dirs': 'true',
		'detailed_bytes': 'false'
	}

	for i in range(1, len(sys.argv)):
		val = sys.argv[i].split('=')
		if(len(val) > 1):
			options[val[0]] = val[1]
		else:
			options['path'] = val[0]

	# Generate File Tree Info
	file_tree = FileTree(None, options['path'])
	fill_file_tree(file_tree)
	file_tree.children.sort(key=lambda i: -i.size)

	# Output
	print_file_tree(
		file_tree,
		0,
		int(options['max_depth']),
		1 if options['only_dirs'] == 'true' else 0,
		1 if options['detailed_bytes'] == 'true' else 0,
	)

	if(options['errors'] == '1'):
		print('\nNumber of errors: ' + str(errors))
