def royal_flush(card):
    return True if sorted(list(map(lambda x:x[0],card.split())))==['A', 'J', 'K', 'Q', 'T'] else False

def straight_flush(card,val_list):    
    val_dic = {r:i for i,r in enumerate('23456789TJQKA', 2)}
    if len(set(map(lambda x:x[1],card.split())))==1:
        if val_dic[val_list[-1]]-val_dic[val_list[0]]==4 and len(set(val_list))==5: return True
    return False

def four_kind(val_list):
    if len(set(val_list))==2 and val_list.count(val_list[1])==4:
        return (True,val_list[1])
    return (False,0)

def full_house(val_list):
    if len(set(val_list))==2 and val_list.count(val_list[2])==3:
        return (True,val_list[0]) if val_list[0]==val_list[2] else (True,val_list[-1])
    return (False,0)

def flush(card):
    return True if len(set(map(lambda x:x[1],card.split())))==1 else False

def straight(val_list):
    val_dic = {r:i for i,r in enumerate('23456789TJQKA', 2)}
    return True if val_dic[val_list[-1]]-val_dic[val_list[0]]==4 and len(set(val_list))==5 else False

def three_kind(val_list):
    if len(set(val_list))==3:
        for ele in val_list:
            if val_list.count(ele)==3: return (True,ele)
    return (False,0)

def two_pairs(val_list):
    if [val_list.count(ele) for ele in  val_list].count(2)==4: return True
    return False

def one_pair(val_list):
    if len(set(val_list))==4:
        for ele in val_list:
            if val_list.count(ele)==2: return (True,ele)
    return (False,0)

def high_card(val_list):
    return val_list[-1]


def rank_count(card):
    sort_order=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    value_dic = {r:i for i,r in enumerate('23456789TJQKA', 2)}
    val_list=list(map(lambda x:x[0],card.split()))
    val_list.sort(key=lambda x:sort_order.index(x))
    a=four_kind(val_list); b=full_house(val_list);c=three_kind(val_list);d=one_pair(val_list)
    if royal_flush(card): return (10,0,value_dic[high_card(val_list)])
    elif straight_flush(card,val_list): return (9,0,value_dic[high_card(val_list)])
    elif a[0]:return (8,value_dic[a[1]],value_dic[high_card(val_list)])
    elif b[0]:return (7,value_dic[b[1]],value_dic[high_card(val_list)])
    elif flush(card): return (6,0,value_dic[high_card(val_list)])
    elif straight(val_list): return (5,0,value_dic[high_card(val_list)])
    elif c[0]:return (4,value_dic[c[1]],value_dic[high_card(val_list)])
    elif two_pairs(val_list): return (3,0,value_dic[high_card(val_list)])
    elif d[0]:return (2,value_dic[d[1]],value_dic[high_card(val_list)])
    else : return (1,value_dic[high_card(val_list)])
    
    
data=open("p054_poker.txt");count=0
for line  in data:
    t=(rank_count(line[:14]),rank_count(line[15:]))
    if t[0][0]>t[1][0]: count+=1
    elif t[0][0]==t[1][0] and t[0][1]>t[1][1]: count+=1
    elif t[0][0]==t[1][0] and t[0][1]==t[1][1] and t[0][0] !=1:
        if t[0][2]>t[1][2]: count+=1

print(count)
        
