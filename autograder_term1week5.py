import numpy.testing as npt
import csv
usernamefile = open('usernames.csv', 'r')
usernames = list(csv.reader(usernamefile))[0]
usernamefile.close()
print("Autograder loaded successfully!")
print("Remember to always restart and run all from the Kernel menu before submitting!")

def question0(_globals):
    score = 0
    myusernamefile = open('my_username.txt', 'r')
    my_username = myusernamefile.read().strip().replace('\'','').replace('\"','')
    myusernamefile.close()
    try:
        assert(not(my_username == 'Delete this text, and insert your short form user name'))
    except:
        print('You don\'t seem to have changed the contents of the file.')
        print(f'\n0 out of 5 marks')
        return 0
    else:
        print('You\'ve changed the contents of the file; thank you!')
        score += 1
    try:
        assert(my_username in usernames)
    except:
        print('Unfortunately, your username has not been recognised; contact Phil or Sam.')
        pass
    else:
        print('Your username has been recognised; thank you!')
        score += 4
    print(f'\n{score} out of 5 marks')
    return score

def question1(_globals):
    score = 0
    number_of_tests = 6
    try:
        assert(_globals['q1ia_answer'] == 4**2 + 1)
    except:
        print('Question 1(i)a failed!')
        pass
    else:
        print('Question 1(i)a passed!')
        score += 1
        
    try:
        assert(_globals['q1ib_answer'] == 4**(2+1))
    except:
        print('Question 1(i)b failed!')
        pass
    else:
        print('Question 1(i)b passed!')
        score += 1
        
    try:
        assert(_globals['q1ic_answer'] == 2/3)
    except:
        print('Question 1(i)c failed!')
        pass
    else:
        print('Question 1(i)c passed!')
        score += 1
        
    try:
        assert(_globals['q1id_answer'] == 381//47)
    except:
        print('Question 1(i)d failed!')
        pass
    else:
        print('Question 1(i)d passed!')
        score += 1
        
    try:
        assert(_globals['q1ie_answer'] == 4*2**5)
    except:
        print('Question 1(i)e failed!')
        pass
    else:
        print('Question 1(i)e passed!')
        score += 1
        
    try:
        assert(_globals['q1if_answer'] == (4*2)**5)
    except:
        print('Question 1(i)f failed!')
        pass
    else:
        print('Question 1(i)f passed!')
        score += 1
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')
    
def question1_ii(_globals):
    score = 0
    number_of_tests = 5
    try:
        assert(_globals['q1iia_answer'] == 1237)
    except:
        print('Question 1(ii)a failed!')
        pass
    else:
        print('Question 1(ii)a passed!')
        score += 1
    
    try:
        assert(_globals['q1iib_answer'] == 1157)
    except:
        print('Question 1(ii)b failed!')
        pass
    else:
        print('Question 1(ii)b passed!')
        score += 1
        
    try:
        assert(_globals['q1iic_answer'] == 636)
    except:
        print('Question 1(ii)c failed!')
        pass
    else:
        print('Question 1(ii)c passed!')
        score += 1
        
    try:
        assert(_globals['q1iid_answer'] == 976)
    except:
        print("Question 1(ii)d failed! Incorrect value.")
    else:
        print('Question 1(ii)d: Correct value!')
        score += 1
    
    try:
        assert(_globals['duration'] < 1e-3)
    except:
        print('Question 1(ii)d failed! The powers example seems to be taking too long; did you use pow with three arguments?')
        pass
    else:
        print('Question 1(ii)d: Quick execution time; you seem to have used pow!')
        score += 1
        
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')
    
    
def question2_i(_globals):
    #from math import sqrt, cos, pi, exp, log, log10, atan, atanh
    from numpy import isclose
    score = 0
    number_of_tests = 7
    try:
        assert(isclose(_globals['q2ia_answer'],7.0710678118654755))
    except:
        print('Question 2(i)a failed!')
        pass
    else:
        print('Question 2(i)a passed!')
        score += 1
    
    try:
        assert(isclose(_globals['q2ib_answer'],0.9009688679024191))
        ans = True
    except:
        ans = False
        print('Question 2(i)b solution value incorrect!')
        pass
    try:
        assert(str(_globals['cos']) == '<built-in function cos>')
        fromed = True
    except:
        fromed = False
        pass
    try:
        assert(_globals['math'])
        imported = True
    except:
        imported = False
        pass
    
    if (imported and ans) or (fromed and ans):
        print('Question 2(i)b passed!')
        score += 1
    else:
        print("The cosine function does not seem to come from the math module")
        print('Question 2(i)b failed!')
        
    try:
        assert(isclose(_globals['q2ic_answer'],1618.1779919126539))
    except:
        print('Question 2(i)c failed!')
        pass
    else:
        print('Question 2(i)c passed!')
        score += 1
     
    try:
        assert(isclose(_globals['q2id_answer'],4.060443010546419))
        ans = True
    except:
        ans = False
        print('Question 2(i)d solution value incorrect!')
        pass
    try:
        assert(str(_globals['log']) == '<built-in function log>')
        fromed = True        
    except:
        fromed = False
        pass
    try:
        assert(_globals['math'])
        imported = True
    except:
        imported = False
        pass
    
    if (imported and ans) or (fromed and ans):
        print('Question 2(i)d passed!')
        score += 1
    else:
        print("The logarithm function does not seem to come from the math module")
        print('Question 2(i)d failed!')
        
    try:
        assert(isclose(_globals['q2ie_answer'],1.7634279935629373))
    except:
        print('Question 2(i)e failed!')
        pass
    else:
        print('Question 2(i)e passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q2if_answer'],0.4636476090008061))
    except:
        print('Question 2(i)f failed!')
        pass
    else:
        print('Question 2(i)f passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q2ig_answer'],0.5493061443340549))
    except:
        print('Question 2(i)g failed!')
        pass
    else:
        print('Question 2(i)g passed!')
        score += 1
        
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')
        
        
    
    
def question2_ii(_globals):
    #from numpy import sqrt, cos, pi, exp, log, log10, arctan, arctanh
    from numpy import isclose
    score = 0
    number_of_tests = 7
    try:
        assert(isclose(_globals['q2iia_answer'],7.0710678118654755))
    except:
        print('Question 2(ii)a failed!')
        pass
    else:
        print('Question 2(ii)a passed!')
        score += 1
    
    try:
        assert(isclose(_globals['q2iib_answer'],0.9009688679024191))
    except:
        print('Question 2(ii)b solution value incorrect!')
        pass
    try:
        assert(isclose(_globals['q2iib_answer'],0.9009688679024191))
        #assert(str(_globals['cos']) == "<ufunc 'cos'>")
    except:
        #print("The cosine function does not seem to come from the numpy module")
        print('Question 2(ii)b failed!')
    else:
        print('Question 2(ii)b passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q2iic_answer'],1618.1779919126539))
    except:
        print('Question 2(ii)c failed!')
        pass
    else:
        print('Question 2(ii)c passed!')
        score += 1
     
    try:
        assert(isclose(_globals['q2iid_answer'],4.060443010546419))
    except:
        print('Question 2(ii)d solution value incorrect!')
        pass
    try:
        assert(isclose(_globals['q2iid_answer'],4.060443010546419))
        #assert(str(_globals['log']) == "<ufunc 'log'>")
    except:
        #print("The logarithm function does not seem to come from the numpy module")
        print('Question 2(ii)d failed!')
    else:
        print('Question 2(ii)d passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q2iie_answer'],1.7634279935629373))
    except:
        print('Question 2(ii)e failed!')
        pass
    else:
        print('Question 2(ii)e passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q2iif_answer'],0.4636476090008061))
    except:
        print('Question 2(ii)f failed!')
        pass
    else:
        print('Question 2(ii)f passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q2iig_answer'],0.5493061443340549))
    except:
        print('Question 2(ii)g failed!')
        pass
    else:
        print('Question 2(ii)g passed!')
        score += 1
        
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')
        
        
            
def question3(p, q):
    from cmath import sqrt
    x = (q/2 + sqrt((q/2)**2 - (p/3)**3))**(1/3) + (q/2 - sqrt((q/2)**2 - (p/3)**3))**(1/3)
    return x
    

    
def question4():
    return 2



def question5_i(_globals):
    from cmath import asin, acos, atanh, log
    from numpy import isclose
    score = 0
    number_of_tests = 4
    try:
        assert(isclose(_globals['q5ia_answer'],(-1.5707963267948966+1.3169578969248166j)))
    except:
        print('Question 5(i)a failed!')
        pass
    else:
        print('Question 5(i)a passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q5ib_answer'],(3.141592653589793-1.3169578969248166j)))
    except:
        print('Question 5(i)b failed!')
        pass
    else:
        print('Question 5(i)b passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q5ic_answer'],(-0.5493061443340549+1.5707963267948966j)))
    except:
        print('Question 5(i)c failed!')
        pass
    else:
        print('Question 5(i)c passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q5id_answer'],(0.6931471805599453+3.141592653589793j)))
    except:
        print('Question 5(i)d failed!')
        pass
    else:
        print('Question 5(i)d passed!')
        score += 1
    
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')    
    
    
    
    
def question5_ii(_globals):
    from numpy import arcsin, arccos, arctanh, log, isclose
    score = 0
    number_of_tests = 4
    try:
        assert(isclose(_globals['q5iia_answer'],(-1.5707963267948966+1.3169578969248166j)))
    except:
        print('Question 5(ii)a failed!')
        pass
    else:
        print('Question 5(ii)a passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q5iib_answer'],(3.141592653589793-1.3169578969248166j)))
    except:
        print('Question 5(ii)b failed!')
        pass
    else:
        print('Question 5(ii)b passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q5iic_answer'],(-0.5493061443340549+1.5707963267948966j)))
    except:
        print('Question 5(ii)c failed!')
        pass
    else:
        print('Question 5(ii)c passed!')
        score += 1
        
    try:
        assert(isclose(_globals['q5iid_answer'],(0.6931471805599453+3.141592653589793j)))
    except:
        print('Question 5(ii)d failed!')
        pass
    else:
        print('Question 5(ii)d passed!')
        score += 1
    
    print(f'{score} out of {number_of_tests} tests passed')
    #return score 
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')
  
def question5_iii_a():
    return 20666298

def question5_iii_b():        
    return 2
  
def question5_iii_c():        
    return 3