

for i in range(1,51):
     print("Fizz" * (i%3 == 0) + "Buzz" * (i%5 == 0) or str(i)) 

print(list(map(lambda  i: "Fizz" * (i%3 == 0) + "Buzz" * (i%5 == 0) or str(i), range(1,101))))


USE AdventureWorks2019;

GO

select * from HumanResources.Department;