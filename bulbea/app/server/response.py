# imports - compatibility imports
from __future__ import absolute_import

# imports - module imports
from bulbea._util import _autodict, _assign_if_none

class Response(object):
	class Status(object):
		SUCCESS = 'success'
		FAIL    = 'fail'
		ERROR   = 'error'

	def __init__(self, status = 'success', data = None):
		self.status = status
		self.data   = _assign_if_none(data, dict())

	def set_data(self, data):
		self.data = data

	def todict(self):
		dict_ = _autodict()

		dict_['status'] = self.status
		dict_['data']   = self.data

		return dict_