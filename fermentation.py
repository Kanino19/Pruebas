# --------------- Package ---------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# ----------------------------------------

# --------------- Class ---------------
# Reactor
class Reactor():
	def __init__(self, t, x, mu, k, K, x_0, Qi, V):
		# time
		self.t = t
		# Constants
		self.mu1max = mu[0]
		self.mu2max = mu[1]

		self.k1 = k[0]
		self.k2 = k[1]

		self.KN = K[0]
		self.KE = K[1]
		self.KS = K[2]
		self.x0 = x
		self.V = V

		# Initial concentration
		self.x_0 = x_0

		# Volumen parametres
		self.Qi = Qi

		# Simulation
		self.Update()
		self.CO2()
		
	def Update(self):
		# Integration
		self.y = odeint(Fermenter, self.x0, self.t, 
			args=(self.k1, self.k2, self.mu1max, self.mu2max, self.KN, self.KE, self.KS, self.x_0, self.Qi, self.V))

	def CO2(self,t):
		# Simulation calculation of CO2
		m = len(t)
		yB = self.y[-m:,0]
		yN = self.y[-m:,1]
		yE = self.y[-m:,2]
		yS = self.y[-m:,3]
		mu2 = ((self.mu2max*yS)/(self.KS+yS))*(self.KE/(self.KE+yE))
		self.y[-m:,4] = mu2*yB
# ----------------------------------------

# --------------- Functions ---------------
# Differential function
def Fermenter(x, t, k1, k2, mu1max, mu2max, KN, KE, KS, x_0, Qi, V):
	# Variables
	B = x[0]
	N = x[1]
	E = x[2]
	S = x[3]
	CO = x[4]
	#V = 1#x[5]

	# Array
	dx = np.zeros(6)
		
	# Mu
	mu1 = mu1max*N/(KN+N)
	mu2 = ((mu2max*S)/(KS+S))*(KE/(KE+E))

	# Differential equations
	dx[0] = mu1*B + Qi*(x_0[0]-B)/V
	dx[1] = -k1*mu1*B + Qi*(x_0[1]-B)/V
	dx[2] = mu2*B + Qi*(x_0[2]-B)/V
	dx[3] = -k2*mu2*B + Qi*(x_0[3]-B)/V
	dx[4] = mu2*B + Qi*(x_0[4]-B)/V
	dx[5] = 0
	return dx

def Plot(t, y, Data):
	# Sort Data
	DataT = Data[:,0]
	DataB = Data[:,6]
	DataN = Data[:,2]/1000.
	DataE = Data[:,3]
	DataS = Data[:,4]
	DataCO2 = Data[:,5]/100.
	#DataV = Data[:,?] 

	# Plotting in several graphics
		# Biomass
	plt.figure(1)
	plt.title('Wine Fermentation')
	plt.xlabel('Time')
	plt.ylabel('Biomass concentration')
	plt.plot(t,y[:,0], label = 'Biomass')
	plt.plot(DataT,DataB,'ro',label='Biomass(Data)')
	plt.legend()

		# Nitrogen
	plt.figure(2)
	plt.xlabel('Time')
	plt.ylabel('Nitrogen concentration')
	plt.plot(t,y[:,1], label = 'Nitrogen')
	plt.plot(DataT,DataN, 'ro',label='Nitrogen(Data)')
	plt.legend()

		#Ethanol
	plt.figure(3)
	plt.xlabel('Time')
	plt.ylabel('Ethanol concentration')
	plt.plot(t,y[:,2], label = 'Ethanol')
	plt.plot(DataT,DataE,'ro', label = 'Ethanol(Data)')
	plt.legend()

		#Sugar
	plt.figure(4)
	plt.xlabel('Time')
	plt.ylabel('Sugar concentration')
	plt.plot(t,y[:,3], label = 'Sugar')
	plt.plot(DataT,DataS,'ro', label = 'Sugar(Data)')
	plt.legend()

		#CO2
	plt.figure(5)
	plt.xlabel('Time')
	plt.ylabel('CO2 concentration')
	plt.plot(t,y[:,4], label = 'CO2')
	plt.plot(DataT,DataCO2,'ro', label = 'CO2(Data)')
	plt.legend()

	plt.show()
# ----------------------------------------


# --------------- Main ---------------
if __name__ == '__main__':
	# Time
	t = range(90)

	# Constants
	mu1max = 1.34
	mu2max = 1.45
	mu = [mu1max, mu2max]

	k1 = 0.0606
	k2 = 2.17
	k = [k1, k2]

	KN = 1.57
	KE = 14.1
	KS = 0.0154
	K = [KN, KE, KS]

	# Initial Condition for each reactor4
	# [B, N, E, S, CO2]
	x0r1 = [0.03, .43, 0., 188., 0., 10.0]
	x0r2 = [0.03, .43, 0., 188., 0., 10.0]
	x0r3 = [0.03, .43, 0., 188., 0., 10.0]
	x0r4 = [0.03, .43, 0., 188., 0., 10.0]

	# Initial concentration for each reactor
	x_0r1 = [0., .43, 0., 188., 0., 10.0]
	x_0r2 = [0., .43, 0., 188., 0., 10.0]
	x_0r3 = [0., .43, 0., 188., 0., 10.0]
	x_0r4 = [0., .43, 0., 188., 0., 10.0]

	# Volumen
	V = [1., 1., 1., 1.]

	# Volumen rate
	Qi = [.10, .8, .6, .4]

	# Create Reactors
	Rea1 = Reactor(t, x0r1, mu, k, K, x_0r1, Qi[0], V[0])
	Rea2 = Reactor(t, x0r1, mu, k, K, x_0r1, Qi[1], V[1])
	Rea3 = Reactor(t, x0r1, mu, k, K, x_0r1, Qi[2], V[2])
	Rea4 = Reactor(t, x0r1, mu, k, K, x_0r1, Qi[3], V[3])

	# Multi-stage Continous Fermentation Wine		

	
	# Concatenate arrays
	#y = np.concatenate((Env1.y, Env2.y, Env3.y, Env4.y), axis=0)

	# Load the data
	#Data = np.loadtxt('batch.txt')

	# Graph
	#Plot(t,y,Data)
# ----------------------------------------