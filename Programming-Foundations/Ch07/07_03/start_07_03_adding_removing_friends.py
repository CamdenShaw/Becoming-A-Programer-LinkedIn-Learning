""" Adding and Removing Friends from Sets """

# revised set of friends to invite
invite = set(['Nestor', 'Amanda', 'Olivia'])

print('Verne' in invite)

invite.add('Verne')
invite.add('Olivia')
print(invite)

invite.remove('Nestor')
print(invite)
# invite.remove('Nestor') 

print(invite.pop())
print(invite.pop())
print(invite.pop())
print(invite.pop()) # error
