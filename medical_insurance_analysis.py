import csv
field_names = ['Age', 'Sex', 'BMI', 'Children', 'Smoker', 'Region', 'Charges']
with open('insurance.csv') as insurance_csv:
    csv_reader = csv.DictReader(insurance_csv, fieldnames = field_names)
    record_list = [row for row in csv_reader]
#print(record_list)
record_list.pop(0)
num = 1
medical_dict = {}
for row in record_list:
    medical_dict.update({f'patient_{num}': row})
    num += 1

region_list = []
for record in medical_dict:
    region = medical_dict[record]['Region']
    if region not in region_list:
        region_list.append(region)

def age_affect(dict, age):
    age_and_below_charges_list = []
    above_age_charges_list = []
    for record in dict:
        info = dict[record]
        if int(info['Age']) <= age:
            age_and_below_charges_list.append(float(info['Charges']))
        else:
            above_age_charges_list.append(float(info['Charges']))
    total_age_and_below = float(sum(age_and_below_charges_list))
    total_above_age = float(sum(above_age_charges_list))
    average_charge_age_and_below = float(total_age_and_below/len(age_and_below_charges_list))
    average_charge_above_age = float(total_above_age/len(above_age_charges_list))
    ratio = round(float(average_charge_age_and_below / average_charge_above_age), 2)
    
    print('\n', '\n', f'According to the dataset it seems like all patients of age {age} and below paid {float(1-ratio) * 100}% less than those older than them. This analysis did not take in to account other factors such as smoking, children, and BMI.')

#age_affect(medical_dict, 30)

def smoker_affect(dict):
    smoker_charges = 0.0
    smoker_count = 0.0
    non_smoker_charges = 0.0
    non_smoker_count = 0.0
    ratio = 0.0
    for record in dict:
        patient = dict[record]
        if patient['Smoker'] == 'yes':
            smoker_charges += float(patient['Charges'])
            smoker_count += 1
        else:
            non_smoker_charges += float(patient['Charges'])
            non_smoker_count += 1
    ratio = round((smoker_charges/smoker_count) / (non_smoker_charges/ non_smoker_count), 2)
    print('\n', '\n', f'According to the dataset it seems that smokers pay {ratio * 100}% more than non-smokers. This analysis does not take into account age, BMI, or how many children the subject has.')


#smoker_affect(medical_dict)
    
def bmi_affect(dict):
    good_bmi_charges = 0.0
    good_bmi_count = 0.0
    bad_bmi_charges = 0.0
    bad_bmi_count = 0.0
    ratio = 0.0
    for record in dict:
        patient = dict[record]
        if float(patient['BMI']) >= 18.5 and float(patient['BMI']) <= 24.9:
            good_bmi_charges += float(patient['BMI'])
            good_bmi_count += 1.0
        else:
            bad_bmi_charges += float(patient["BMI"])
            bad_bmi_count += 1.0
        
    ratio = (good_bmi_charges / good_bmi_count) / (bad_bmi_charges / bad_bmi_count)
    print('\n', '\n', f'Individuals with a healthy BMI (between 18.5 and 24.9) paid approximately {round((1-ratio) * 100,2)} % less than individuals with a less than healthy BMI. This analysis does not take into account different hieghts and sexes. It also does not take into account other factors that might affect insurance costs.')

#bmi_affect(medical_dict)
def create_region_list(dict):
    new_list = []
    for record in dict:
        if dict[record]['Region'] not in new_list:
            new_list.append(dict[record]['Region'])
    return new_list
# region_list = create_region_list(medical_dict)
# print(region_list)
#def region_affect(dict):