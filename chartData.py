import psycopg2
import csv

try:
	conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="postgres27")
	cursor = conn.cursor()


	sex_query = """
	SELECT sex, count(*) AS num 
	FROM covid.data 
	GROUP BY sex"""

	cursor.execute(sex_query)
	cursor.fetchone() #skips 1st row
	sex_records = cursor.fetchall() 
	print("Sex data")

	for col in sex_records:
		print(col[0],"	",col[1])


	fieldnames = ["Sex","Count"]
	with open('chartSex.csv', 'w') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
		csv_writer.writeheader()

	for col in sex_records:
		with open('chartSex.csv', 'a') as csv_file:
			csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
			info = {"Sex": col[0], "Count": col[1]}
			csv_writer.writerow(info)


	age_query = """SELECT AgeGroup, Count(AgeGroup)
	from (SELECT
    CASE
    WHEN Age <= 17 THEN '0-17'
    WHEN Age between 18 and 30 THEN '18-30'
    WHEN Age between 31 and 45 THEN '31-45'
    WHEN Age between 46 and 60 THEN '46-60'
    ELSE '60+'
    END AS AgeGroup
	FROM covid.data) AS AgeGroup
	GROUP BY AgeGroup
	ORDER BY AgeGroup """

	cursor.execute(age_query)
	cursor.fetchone()
	age_records = cursor.fetchall() 
	print("Status data")

	for col in age_records:
		print(col[0],"	",col[1])


	fieldnames = ["AgeGroup","Count"]
	with open('chartAge.csv', 'w') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
		csv_writer.writeheader()

	for col in age_records:
		with open('chartAge.csv', 'a') as csv_file:
			csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
			info = {"AgeGroup": col[0], "Count": col[1]}
			csv_writer.writerow(info)




	residence_query = """SELECT residence, count(status) 
	from covid.data where status = 'Admitted' or status = 'Dead' 
	group by residence
	order by count(status) DESC """

	cursor.execute(residence_query)
	cursor.fetchone()
	residence_records = cursor.fetchall() 
	print("Status data")

	for col in residence_records:
		print(col[0],"	",col[1])

	fieldnames = ["Residence","Count"]
	with open('chartResidence.csv', 'w') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
		csv_writer.writeheader()

	for col in residence_records:
		with open('chartResidence.csv', 'a') as csv_file:
			csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
			info = {"Residence": col[0], "Count": col[1]}
			csv_writer.writerow(info)
			

finally:
    if(conn):
        cursor.close()
        conn.close()
        #print("PostgreSQL connection is closed")

