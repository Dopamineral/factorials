import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal

def brute_factorial(x,show_progress=False,progress_steps=1000):
	x = x
	y = 1
	for i in range(x):
		if show_progress == True and i % progress_steps == 0:
			print("processing: {} percent done".format('%.2f'%(i/x*100)),"current:{} factorial = {}".format('%2E'%Decimal(i),'%2E'%Decimal(y)))
		y *= (x-i)
	return y 
		
def stirling_factorial(x):
	y = (np.sqrt(2*np.pi*x))*((x/np.e)**x)
	return y

range_plot = 100

x_list = []
for i in range(range_plot+1):
	x_list.append(i)

y_list_brute = []
for i in range(range_plot+1):
	y_list_brute.append(brute_factorial(i))

y_list_stirling = []
for i in range(range_plot+1):
	y_list_stirling.append(stirling_factorial(i))

#print(x_list,y_list_stirling,y_list_brute)

diff_list = []
for i in range(len(y_list_stirling)):
	diff = - y_list_stirling[i] + y_list_brute[i]
	diff_list.append(diff)

#plt.semilogy(x_list,y_list_brute,linewidth=0.5)
#plt.semilogy(x_list,y_list_stirling, color='r',linewidth=0.5)
#plt.semilogy(x_list,diff_list,color='g',linewidth=0.5)
#plt.show()

diff_percent = []
for i in range(len(y_list_stirling)):
	diff = y_list_stirling[i] / y_list_brute[i]
	diff_percent.append(diff)


#plt.semilogx(x_list,diff_percent)
#plt.xlim(2,len(x_list))
#plt.show()

if __name__ == "__main__":
	import timeit
	#timeit.timeit("stirling_factorial(100)",setup="from __main__ import stirling_factorial"))
	#timeit.timeit("brute_factorial(100)",setup="from __main__ import brute_factorial"))

	print("Stirling method: {} seconds \n".format(timeit.timeit("stirling_factorial(100)",setup="from __main__ import stirling_factorial", number=100000)))
	print("Brute force method: {} seconds \n".format(timeit.timeit("brute_factorial(100)",setup="from __main__ import brute_factorial", number=100000)))


	test_range = 10000
	st_index = 1
	try:
		for i in range(test_range):
			stirling_factorial(i)
			i += 1
			st_index += 1
		print("Sitrling factorial succesful until {}".format(test_range))
	except:
		print("Stirling factorial failed at: {}".format(st_index))


	bt_index = 1
	try:
		outcome = brute_factorial(test_range,show_progress=True,progress_steps=9876)
		print("Brute factorial succesful until {}".format(test_range))
		print(outcome)
	except:
		print("Brute factorial failed at: {}".format("later"))

	input()
