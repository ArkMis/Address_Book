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

adr_list=[]

for _ in range(5):
    adr_list.append(AdrBook(first_name=fake.first_name(),surname=fake.last_name(),firm_name=fake.company(),status=fake.job(),email=fake.email()))

for i in range(5):
   #print('%s %s, %s, %s, %s' % (adr_list[i].first_name, adr_list[i].surname, adr_list[i].firm_name, adr_list[i].status, adr_list[i].email))
   print(adr_list[i])
      
   #print('-----------')




