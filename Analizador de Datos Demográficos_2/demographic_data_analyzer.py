import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer datos del archivo
    df = pd.read_csv("adult.data.csv")

    # ¿Cuántos de cada "raza" (etnia) están representados en este conjunto de datos? 
    # Serie de Pandas con nombres de carreras como etiquetas de índice.
    
    race_count = df['race'].value_counts()

    # Edad promedio de los hombres
    men = df[df['sex'] == "Male"]
    average_age_men = round(men['age'].mean(), 1)

    # Porcentaje de personas que tienen Licenciatura
    bachelor = df[df['education'] == "Bachelors"]
    percentage_bachelors = round(bachelor.shape[0]/df.shape[0]*100, 1)

    # # Porcentaje de personas con educación avanzada 
    # ("licenciatura", "maestría" o "doctorado") kue ganan más de 50K
    # Porcentaje de personas SIN educación avanzada y kue ganan más de 50K

    # CON y SIN "licenciatura", "maestría" o "doctorado"
    
    higher_education = df[df['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df['education'].isin(["Bachelors", "Masters", "Doctorate"])]

    # Porcentaje salarial >50K
    higher_education_rich = round(higher_education[higher_education['salary'] == ">50K"].shape[0]/higher_education.shape[0]*100, 1)
    lower_education_rich = round(lower_education[lower_education['salary'] == ">50K"].shape[0]/lower_education.shape[0]*100, 1)

    # Cantidad mínima de horas que una persona trabaja por semana 
    # en horas por semana...
    min_work_hours = df['hours-per-week'].min()

    # Porcentaje de las personas que trabajan el número mínimo de horas por semana 
    # y tienen un salario de >50K...
    
    min_hours = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]

    rich_percentage = round(min_hours[min_hours['salary'] == ">50K"].shape[0]/num_min_workers*100, 1)

    # País con el porcentaje más alto de personas que ganan >50K?
    num_high_salary_per_country = df[df['salary'] == ">50K"]['native-country'].value_counts()
    num_country = df['native-country'].value_counts()
    percentage = num_high_salary_per_country/num_country*100

    highest_earning_country = percentage.idxmax()
    highest_earning_country_percentage = round(percentage.max(), 1)

  
    high_salary_India_occ = df[(df['salary'] == ">50K") & (df['native-country'] == "India")]['occupation'].value_counts()

    top_IN_occupation = high_salary_India_occ.idxmax()


    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
