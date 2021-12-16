from faker import Faker

fake = Faker('pl_PL')
fake.name()
fake.first_name()
fake.last_name()
fake.company()
fake.job()
fake.email()

class BaseContact:
   def __str__(self):
        return f'{self.first_name} {self.surname} {self.email}     {self.phone_number}'

   def __init__(self, first_name,surname,email,phone_number):
        self.first_name=first_name
        self.surname=surname
        self.email=email
        self.phone_number=phone_number
        #variables
        self.__label_length=0

   @property
   def label_lenght(self):
        return len(self.first_name)+1+len(self.surname)

   def contact(self):
        return f'Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.surname}'
        
class BusinessContact(BaseContact):
    def __init__(self,status,firm_name,bphone, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.firm_name=firm_name
        self.status=status
        self.bphone=bphone      # business phone number

    def contact(self):
        return f'Wybieram numer {self.bphone} i dzwonię do {self.first_name} {self.surname}'

def create_contact(nr_listy, ilosc):
    if nr_listy==1:
        for _ in range(ilosc):
            adr_list1.append(BaseContact(first_name=fake.first_name(),surname=fake.last_name(),email=fake.email(),phone_number=fake.phone_number()))
    else:
        for _ in range(ilosc):
            adr_list2.append(BusinessContact(first_name=fake.first_name(),surname=fake.last_name(),firm_name=fake.company(),status=fake.job(),email=fake.email(),phone_number=fake.phone_number(),bphone=fake.phone_number()))


adr_list1=[]
adr_list2=[]

create_contact(1,5)
create_contact(2,5)

print('Base contact')
print('------------')
for i in range(5):
   #print('%s %s, %s, %s, %s' % (adr_list[i].first_name, adr_list[i].surname, adr_list[i].firm_name, adr_list[i].status, adr_list[i].email))
   print(adr_list1[i])
print('--------')

print('Business contact')
print('----------------')
for i in range(5):
   print(adr_list2[i])
print('--------')

by_first_name = sorted(adr_list1, key=lambda BaseContact: BaseContact.first_name)
print('--- by first name -------------')
for i in range(5):
   print(by_first_name[i])

by_surname = sorted(adr_list1, key=lambda BaseContact: BaseContact.surname)
print('--- by surname -------------')
for i in range(5):
   print(by_surname[i])

by_email = sorted(adr_list1, key=lambda BaseContact: BaseContact.email)
print('--- by email -------------')
for i in range(5):
   print(by_email[i])

print('')
print('--- Base Contact ---')
print(adr_list1[1].contact())
print(adr_list1[1].label_lenght)
print('')
print('--- Business Contact ---')
print('Business phone: %s ' % (adr_list2[1].bphone))
print('Private phone: %s ' % (adr_list2[1].phone_number))
print(adr_list2[1].contact())
print(adr_list2[1].label_lenght)
#print('-----------')




