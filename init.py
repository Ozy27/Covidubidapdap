import psycopg2
conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="postgres27")
cursor = conn.cursor()

start_query = """
CREATE SCHEMA covid;
CREATE TABLE covid.data (
CaseNo varchar(255), Age int, Sex varchar(255), Nationality varchar(255), Status varchar(255), StatusDate varchar(255),DatePositive varchar(255),
DateOnset varchar(255), A varchar(255), B varchar(255), C varchar(255),D varchar(255),E varchar(255), F varchar(255),
Facility varchar(255), Residence varchar (255), Town varchar(255), Travel varchar(255), TravelTo varchar(255),
link1 varchar(255), link2 varchar(255), info varchar(255)
);"""
cursor.execute(start_query)


f= open('covph.txt')
next(f)
next(f)
cursor.copy_from(f, 'covid.data', sep='	', null ="")


conn.commit()
