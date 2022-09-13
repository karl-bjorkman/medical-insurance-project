import csv

ages = []
sex = []
bmi = []
children = []
smoker = []
regions = []
charges = []

with open('insurance.csv', newline='') as csvfile:
    med_insurance = csv.DictReader(csvfile)
    for record in med_insurance:
        ages.append(record['age'])
        sex.append(record['sex'])
        bmi.append(record['bmi'])
        children.append(record['children'])
        smoker.append(record['smoker'])
        regions.append(record['region'])
        charges.append(record['charges'])


def avg_age(age_lst):
    total_age = 0
    for age in age_lst:
        total_age += int(age)

    avg_patient_age = round(total_age / len(age_lst))

    return avg_patient_age

avg_age(ages)


def avg_age_parent(age_lst, children_lst):
    age_children_comp = list(zip(age_lst, children_lst))
    total_age = 0
    total_parents = 0
    for record in age_children_comp:
        if int(record[1]) > 0:
            total_age += int(record[0])
            total_parents += 1

    avg_parent_age = round(total_age / total_parents)

    return "Average parent age is {age} years old.".format(age=avg_parent_age)

avg_age_parent(ages, children)


def parent_count(children_lst):
    parents = 0
    for i in children_lst:
        if int(i) > 0:
            parents += 1

    return "Out of {all_patients} patients, {parents} are parents.".format(
        all_patients=len(children_lst), parents=parents)

parent_count(children)


def smoking_cost(smoker_lst, charges_lst):
    smoker_charges_comp = list(zip(smoker_lst, charges_lst))
    smoker_charges_total = 0
    smoker_total = 0
    nonsmoker_charges_total = 0
    nonsmoker_total = 0
    for record in smoker_charges_comp:
        if record[0] == 'yes':
            smoker_charges_total += float(record[1])
            smoker_total += 1
        else:
            nonsmoker_charges_total += float(record[1])
            nonsmoker_total += 1

    avg_smoker_cost = round(smoker_charges_total / smoker_total, 2)
    avg_nonsmoker_cost = round(nonsmoker_charges_total / nonsmoker_total, 2)

    return "Avg Nonsmoker Charges: ${nonsmoker_charges} | Avg Smoker Charges: ${smoker_charges}".format(nonsmoker_charges=avg_nonsmoker_cost, smoker_charges=avg_smoker_cost)

smoking_cost(smoker, charges)


def loc_counter(region_lst):
    loc_lst = []
    sw_count = 0
    se_count = 0
    nw_count = 0
    ne_count = 0
    # Not returned, but finds all location names from csv file
    for region in region_lst:
        if region not in loc_lst:
            loc_lst.append(region)
    for region in region_lst:
        if region == 'southwest':
            sw_count += 1
        elif region == 'southeast':
            se_count += 1
        elif region == 'northwest':
            nw_count += 1
        elif region == 'northeast':
            ne_count += 1
        else:
            return None

    return "Southwest: {sw}, Southeast: {se}, Northwest: {nw}, Northeast: {ne}".format(
        sw=sw_count, se=se_count, nw=nw_count, ne=ne_count)

loc_counter(regions)