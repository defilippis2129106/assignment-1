"""
INPUT: 2 2 2
OUTPUT: 0.78333
"""
k = 2 # AA
m = 2 # Aa
n = 2 # aa

tot = k + m + n

def ProbDominant(k,m,n):
    tot = k + m + n
    # firstly we calculate the probabilty of having a combination with at least one A-
    prob_kk = (k/tot) * ((k-1)/(tot-1))
    prob_km = (k/tot) * (m/(tot-1)) + (m/tot)*(k/(tot-1))
    prob_kn = (k/tot) * (n/(tot-1))+ (n/tot)*(k/(tot-1)) 
    # in these first 3 cases all offspring will have a dominant allele, based on a simple Punnett Square
    # so we don't need to multiply by anything
    prob_mm = (m/tot) * ((m-1)/(tot -1)) * 0.75 # in AaxAa only 75% of the offspring has a dominant allele
    prob_mn = (m/tot) * (n/(tot-1)) * 0.5 + (n/tot)*(m/(tot-1)) * 0.5 # in Aaxaa only 50% has a dominant allele
    tot_dom = prob_kk + prob_km + prob_kn + prob_mm + prob_mn
    return tot_dom

result = ProbDominant(k,m,n)
print(result)

