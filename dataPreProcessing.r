dataset = read.csv('data/Data.csv')

dataset$Age = ifelse(is.na(dataset$Age), #Verifies if the field age is empty
                    ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),#if the condition is true, replace by columns mean
                    dataset$Age)#if the condition is false keep the value

dataset$Salary = ifelse(is.na(dataset$Salary), #Verifies if the field age is empty
                    ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),#if the condition is true, replace by columns mean
                    dataset$Salary)#if the condition is false keep the value

#Encoding non numerical data
dataset$Country = factor(dataset$Country,
                        levels = c('France','Spain','Germany'),
                        labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased,
                        levels = c('No','Yes'),
                        labels = c(0, 1))

print(dataset)