import pymysql
conn = pymysql.connect(host='devdbrds.cfgu9s5ykxy0.ap-southeast-1.rds.amazonaws.com', user='admin', passwd='Admin$2020$12!%', db='devai')
cur = conn.cursor()
keyword="Address"
cur.execute("SELECT resume_id,resume_text FROM devai.nr_resume_text LIMIT 5")
for r in cur:
    print(r)
cur.close()
conn.close()