P1 = the proportion of Republican voters in the first state 
P2 = the proportion of Republican voters in the second state
p1 = the proportion of Republican voters in the sample from the first state
p2 = the proportion of Republican voters in the sample from the second state 

The number of voters sampled from the first state (n1) = 100,
the number of voters sampled from the second state (n2) = 100.

The solution involves four steps.

 n1P1 = 100 * 0.52 = 52, 
 n1(1 - P1) = 100 * 0.48 = 48, 
 n2P2 = 100 * 0.47 = 47 
 n2(1 - P2) = 100 * 0.53 = 53 

 Find the mean of the difference in sample proportions: E(p1 - p2) = P1 - P2 = 0.52 - 0.47 = 0.05.

 Find the standard deviation of the difference.
    
 sd = sqrt{ [ P1(1 - P1) / n1 ] + [ P2(1 - P2) / n2 ] }
 sd = sqrt{ [ (0.52)(0.48) / 100 ] + [ (0.47)(0.53) / 100 ] }
 sd = sqrt (0.002496 + 0.002491) = sqrt(0.004987) = 0.0706
    
To find this probability, we need to transform the random variable (p1 - p2) into a z-score.

z p1 - p2 = (x - µ p1 - p2 ) / sd = = (0 - 0.05)/0.0706 = -0.7082 

Using normal distribution table we find that Probability fro z-score of -0.7082 is 0.24

Hence probability that the survey will show a greater percentage of Republican
voters in the second state than in the first state is 0.24