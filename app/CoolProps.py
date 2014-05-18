import CoolProp
import CoolProp.CoolProp as CP
from CoolProp import *

class CoolProp_State():
	"""Get States from Properties Entered"""
	def __init__(self, P, T):
		self.P = P
		self.T = T
		self.d = {'P':P,'T':T}
		self.state = CoolProp.State('Water',self.d)

	def get_cv(self):
		return self.state.get_cv()

	def get_cp(self):
		return self.state.get_cp()

	def get_rho(self):
		return self.state.get_rho()

	def get_p(self):
		return self.state.get_p()

	def get_t(self):
		return self.state.get_T()

	def get_all(self):
		t = self.get_t()
		p = self.get_p()
		cv = self.get_cv()
		cp = self.get_cp()
		rho = self.get_rho()
		return {'t':t,'p':p,'cv':cv, 'cp':cp, 'rho':rho}

		
		