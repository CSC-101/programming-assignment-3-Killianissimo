import county_demographics
import data
import build_data
from data import CountyDemographics
import math

'''This function inputs a list of County Demographics and outputs an integer. The function takes the
inputted County Demographics and adds all of their 2014 Population data to an integer. It then 
returns that integer. 
'''
def population_total(input:list[CountyDemographics]) -> int:
    output = 0
    for i in range(len(input)):
            output += input[i].population["2014 Population"]
    return output

'''This function inputs a list of County Demographics and a string. The function takes each
County Demographic and checks if the state key attached to it is equal to the given string. The
function outputs a new list composed of all the County Demographics in the input list that has the
correct state.
'''
def filter_by_state(vals:list[CountyDemographics], state:str) -> list[CountyDemographics]:
    output = []
    for i in range(len(vals)):
        if vals[i].state == state:
            output.append(vals[i])
    return output

'''These functions input a list of County Demographics and a string and outputs an integer. The 
function takes the 2014 Population of the county and multiplies it by the percentage associated
with the education of the type of the given string (that has been divided by 100, so it's not in
percentage form anymore) and returns that integer. 
'''
def population_by_education(lists:list[CountyDemographics], type:str) -> int:
    output = 0
    for i in range(len(lists)):
        countyTotal = (lists[i].education[type]/100)*lists[i].population["2014 Population"]
        output += countyTotal
    output = math.floor(output)
    return output
def population_by_ethnicity(lists:list[CountyDemographics], type:str) -> int:
    output = 0
    for i in range(len(lists)):
        countyTotal = (lists[i].ethnicities[type]/100)*lists[i].population["2014 Population"]
        output += countyTotal
    output = math.floor(output)
    return output
def population_below_poverty_line(lists:list[CountyDemographics], type:str) -> int:
    output = 0
    for i in range(len(lists)):
        countyTotal = (lists[i].income[type]/100)*lists[i].population["2014 Population"]
        output += countyTotal
    output = math.floor(output)
    return output

'''These functions take a list of county demographics and a string. These functions take the 
number of people that had a certain characteristic and divides that number by the total number
of people in 2014. This number is then multiplied by 100 and returned as the output. 
'''

def percent_by_education(lists:list[CountyDemographics], type:str) -> int:
    output = 0
    output += (population_by_education(lists, type)/population_total(lists))*100
    return output
def percent_by_ethnicity(lists:list[CountyDemographics], type:str) -> int:
    output = 0
    output += (population_by_ethnicity(lists, type)/population_total(lists))*100
    return output
def percent_below_poverty_line(lists:list[CountyDemographics], type:str) -> int:
    output = 0
    output += (population_below_poverty_line(lists, type)/population_total(lists))*100
    return output


'''These functions input a list of county demographics, a string, and a float and output a list of
county demographics. This function checks the education value of each element of the inputted list
of the type of the provided string and adds that element to a new list if the education value is
greater than or less than (depending on which function) the given float. The function then returns
this new list.
'''
def education_greater_than(vals:list[CountyDemographics], type:str, value:float) -> list[CountyDemographics]:
    output = []
    for i in range(len(vals)):
        if vals[i].education[type] > value:
            output.append(vals[i])
    return output
def education_less_than(vals:list[CountyDemographics], type:str, value:float) -> list[CountyDemographics]:
    output = []
    for i in range(len(vals)):
        if vals[i].education[type] < value:
            output.append(vals[i])
    return output

'''These functions input a list of county demographics, a string, and a float and output a list of
county demographics. This function checks the ethnicity value of each element of the inputted list
of the type of the provided string and adds that element to a new list if the ethnicity value is
greater than or less than (depending on which function) the given float. The function then returns
this new list.
'''
def ethnicity_greater_than(vals:list[CountyDemographics], type:str, value:float) -> list[CountyDemographics]:
    output = []
    for i in range(len(vals)):
        if vals[i].ethnicities[type] > value:
            output.append(vals[i])
    return output
def ethnicity_less_than(vals:list[CountyDemographics], type:str, value:float) -> list[CountyDemographics]:
    output = []
    for i in range(len(vals)):
        if vals[i].ethnicities[type] < value:
            output.append(vals[i])
    return output

'''These functions input a list of county demographics, a string, and a float and output a list of
county demographics. This function checks the income value of each element of the inputted list
of the type of the provided string and adds that element to a new list if the income value is
greater than or less than (depending on which function) the given float. The function then returns
this new list.
'''
def below_poverty_line_greater_than(vals:list[CountyDemographics], type:str, value:float) -> list[CountyDemographics]:
    output = []
    for i in range(len(vals)):
        if vals[i].income[type] > value:
            output.append(vals[i])
    return output
def below_poverty_line_less_than(vals:list[CountyDemographics], type:str, value:float) -> list[CountyDemographics]:
    output = []
    for i in range(len(vals)):
        if vals[i].income[type] < value:
            output.append(vals[i])
    return output