# Python code to illustrate the Module 
class Nissan: 
	# First we create a constructor for this class 
	# and add members to it, here models 
	def __init__(self): 
		self.models = ['altima', '370z', 'cube', 'rogue'] 

	# A normal print function 
	def outModels(self): 
		print('These are the available models for Nissan') 
		for model in self.models: 
			print('\t%s ' % model) 
