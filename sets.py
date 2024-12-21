# sets module

st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)
#joining set and list

family_members = {'yusuf', 'usman', 'aliyu', 'adam'}
family_members.add('abubakar')
family_members.update(['baffa', 'saad', 'nura'])
print(family_members)

#joining sets and tuple
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

#pop method
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 