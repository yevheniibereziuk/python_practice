def create_record(name, phone, address):
    """Create record"""
    record = {
        'name': name,
        'phone': phone,
        'address': address
    }
    return record

user1 = create_record("Vasya", "+38068595959", "Dnipro")
user2 = create_record("Oleg", "+380656546589", "Lviv")

print(user1)
print(user2)

def give_award(medal, *persons):
    """Give medals to persons"""
    for person in persons:
        print("Pane " + person.title() + " nagoroda medliyu " + medal)
    
give_award("Za Kharkiw", "Andriy", "Ostap")
give_award("Za Kherson", "Petya", "Alex", "Viktor")
