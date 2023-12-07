def royal_flush(card):
    return True if sorted(list(map(lambda x:x[0],card.split())))==['A', 'J', 'K', 'Q', 'T'] else False

def straight_flush(card):
    val_dic = {r:i for i,r in enumerate('23456789TJQKA', 2)}
    if len(set(map(lambda x:x[1],card.split())))==1:
        val_list=sorted(list(map(lambda x:x[0],card.split())))
        if val_dic[val_list[-1]]-val_dic[val_list[0]]==4: return True
    return False

def four_kind(card):
    val_list=sorted(list(map(lambda x:x[0],card.split())))
    if len(set(val_list))==2 and val_list.count(val_list[1])==4:
        return (True,val_list[1])
    return (False,0)
        
def full_house(card):
    val_list=sorted(list(map(lambda x:x[0],card.split())))
    if len(set(val_list))==2 and val_list.count(val_list[2])==3:
        return (True,val_list[0]) if val_list[0]==val_list[2] else (True,val_list[-1])
    return (False,0)    
    
def flush(card):
    return True if len(set(map(lambda x:x[1],card)))==1 else False

def straight(card):
    val_dic = {r:i for i,r in enumerate('23456789TJQKA', 2)}
    val_list=sorted(list(map(lambda x:x[0],card.split())))
    return True if val_dic[val_list[-1]]-val_dic[val_list[0]]==4 else False

def three_kind(card):
    val_list=sorted(list(map(lambda x:x[0],card.split())))
    if len(set(val_list))==3:
        for ele in val_list:
            if val_list.count(ele)==3: return (True,ele)
    return (False,0)

def two_pairs(card):
    val_list=sorted(list(map(lambda x:x[0],card.split())))
    if [val_list.count(ele) for ele in  val_list].count(2)==4: return True
    return False

def one_pair(card):
    val_list=sorted(list(map(lambda x:x[0],card.split())))
    if len(set(val_list))==4:
        for ele in val_list:
            if val_list.count(ele)==2: return (True,ele)
    return (False,0)

def high_card(card):
    sort_order=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    val_list=list(map(lambda x:x[0],card.split()))
    val_list.sort(key=lambda x:sort_order.index(x))
    return val_list

print(straight_flush("5C JC 2H 5S 3D"))


