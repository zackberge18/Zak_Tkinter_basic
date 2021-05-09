import random

answer_list=[]
our_states=['kawaki', 'asta', 'goku', 'vegeta', 'edward', 'sasuke', 'ichigo']

global our_state_capitals

def choices():
    for i in range(3):
        rand_num=random.randint(0,len(our_states)-1)
        if i ==0:
            answer=our_states[rand_num]
        answer_list.append(our_states[rand_num])
        our_states.remove(our_states[rand_num])
    print(answer_list)
    print(answer)


choices()


