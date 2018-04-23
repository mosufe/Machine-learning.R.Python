dataset = read.csv('data/Data.csv')

dataset$Age = ifelse(is.na(dataset$Age), #Verifies if the field age is empty
                    ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),#if the condition is true, replace by columns mean
                    dataset$Age)#if the condition is false keep the value

dataset$Salary = ifelse(is.na(dataset$Salary), #Verifies if the field age is empty
                    ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),#if the condition is true, replace by columns mean
                    dataset$Salary)#if the condition is false keep the value