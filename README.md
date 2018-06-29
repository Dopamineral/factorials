# factorials
Experiments comparing brute-force calculating of factorials and the mathematical Stirling approximation.


Findings: 

Stirling method outperforms brute force method in terms of speed (4.5 times faster to execute):

time to execute 100k executions:

> Stirling method: 0.635 seconds 

> Brute force method: 2.846 seconds 

Max execution number:

> Stirling method: 172 on laptop due to overflow error using numpy modules.

> Brute force method: indefinite, succesfully calculated 1000000! 

Accuracy:

> Stirling method has a starting accuracy of about 0.925, but accuracy exponentially increases to 1, being more than 0.99 at 9! and more than 0.999 at 88! 

> Brute force obviously has 100% accuracy


