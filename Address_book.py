from faker import Faker

fake = Faker('pl_PL')
fake.name()
fake.first_name()
fake.last_name()
fake.company()
fake.job()
fake.email()

class AdrBook:
   def __str__(self):
        return f'{self.first_name} {self.surname} {self.email}'

   def __init__(self, first_name,surname,firm_name,status,email):
        self.first_name=first_name
        self.surname=surname
        self.firm_name=firm_name
        self.status=status
        self.email=email
        #variables
        self.__len_addr=0

   @property
   def len_addr(self):
        return len(self.first_name)+1+len(self.surname)

   def contact(self):
        return f'Kontaktuję się z {self.first_name} {self.surname} {self.status} {self.email}'
        

adr_list=[]

for _ in range(5):
    adr_list.append(AdrBook(first_name=fake.first_name(),surname=fake.last_name(),firm_name=fake.company(),status=fake.job(),email=fake.email()))

for i in range(5):
   #print('%s %s, %s, %s, %s' % (adr_list[i].first_name, adr_list[i].surname, adr_list[i].firm_name, adr_list[i].status, adr_list[i].email))
   print(adr_list[i])
      
by_first_name = sorted(adr_list, key=lambda AdrBook: AdrBook.first_name)
print('by first name -------------')
for i in range(5):
   print(by_first_name[i])

by_surname = sorted(adr_list, key=lambda AdrBook: AdrBook.surname)
print('by surname -------------')
for i in range(5):
   print(by_surname[i])

by_email = sorted(adr_list, key=lambda AdrBook: AdrBook.email)
print('by email -------------')
for i in range(5):
   print(by_email[i])

print('')
print('--- metoda contact ---')
print(adr_list[1].contact())
print(adr_list[1].len_addr)

#print('-----------')




