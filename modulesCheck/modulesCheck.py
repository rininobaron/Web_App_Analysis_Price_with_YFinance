import os
def modulesCheck(modules_list):
	'''
	This function check if a module like "pandas" is 
	installed in your python envioronment. Otherwise the module is installed.

	Arguments:

	modules_list: The list of names of modules in string format
	'''
	for module in modules_list:
		try:
			__import__(module)
		except e:
			print(e)
			print()
			print('Installing ', module, ' ...')
			pip.main(['install', module])