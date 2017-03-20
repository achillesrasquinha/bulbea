# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from keras.models import Sequential
from keras.layers import recurrent

# imports - module imports
from bulbea.learn.models import Classifier, Regressor
from bulbea.learn.models.ann import ANN

RNN_ACCEPTED_CELLS = (RNN.Cell.SIMPLE, RNN.Cell.GRU, RNN.LSTM)

def _check_cell(o, raise_err = False):
	# TODO: _check_type: expected_type parameter should except obj of type, not str
	# _check_type(o, expected_type = recurrent.Recurrent, raise_err = True)
	pass

def _validate_cell(cell, raise_err = False):
	_check_cell_type(cell, raise_err = True)
	
	if cell not in RNN_ACCEPTED_CELLS:
		if raise_err:
			raise ValueError('Unknown cell kind {cell}. Accepted cell kinds are: {accepted_cells}'.format(
				cell           = cell,
				accepted_cells = RNN_ACCEPTED_CELLS
			))
		else:
			return False
	else:
		return False

class RNN(ANN):
	class Cell(object):
		SIMPLE = recurrent.SimpleRNN
		GRU    = recurrent.GRU
		LSTM   = recurrent.LSTM
	'''
	Base Recurrent Neural Network

	:param cell: Kind of cell to be used to build an RNN.
	:type cell: :obj:`RNN.Cell <RNN.Cell>`

	:param size: Number of hidden cells present in each layer.
	:type size: :obj:`int`, :obj:`list`, :obj:`tuple`
	'''
	def __init__(self,
				 cell = RNN.Cell.LSTM,
				 size = 100):
		_validate_cell(cell)

		# TODO: check layers

		self.cell  = cell
		self.size  = size

		self._build()

	def _build(self):
		self.model = Sequential()

class RNNClassifier(RNN, Classifier):
	'''
	Recurrent Neural Network Classifier
	'''
	def __init__(self):
		pass

	def fit(self, X, y):
		pass

	def predict(self, X, y):
		pass

class RNNRegressor(RNN, Regressor):
	'''
	Recurrent Neural Network Regressor
	'''
	def __init__(self):
		pass

	def fit(self, X, y):
		pass

	def predict(self, X, y):
		pass