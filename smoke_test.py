import boto3 ,os,sys
client=boto3.client('ssm',region_name='us-east-1')
param={
    os.path.basename(p["Name"]):p["Value"]
    for p in client.get_parameters_by_path(
        Path="/application/banking",
        WithDecryption=True
        )["Parameters"]
}

required=["DB_HOST","DB_NAME,"DB_USER","DB_PASSWORD","DB_PORT]
missing=[k for k in required if k not in params]

for k in required:
    print(f"{k} : {"👍"if k in params else "🤞"}")

if missing:
    print(f"failed : {missing}")
    sys.exit(1)

#DB FIND banking_ and show table
try:
    connection = pymysql.connect(
        host=params["DB_HOST"],
        user=params["DB_USER"],
        password=params["DB_PASSWORD"],
        database=params["DB_NAME"],
        port=int(params["DB_PORT"])
        connect_timeout=10
    )

    cur=connection.cursor()
    cursor.execute("SHOW TABLES")
    tables =[row[0] for row in cursor.fetchall()]
    connection.close()
    print(f"{params["DB_NAME"]}")
    print(f"Table : {tables}")
except Exception as e:
    print("DB_ERROR : ",e)
    sys.exit(1)

print("Smoke Test Done ✅")

    