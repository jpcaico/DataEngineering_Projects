import psycopg2

def update_record(actor_id, first_name, last_name):
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="pagila",
        user="admin",
        password="root"
    )
    cursor = conn.cursor()
    update_query = "UPDATE public.actor SET first_name = %s, last_name = %s WHERE actor_id = %s"
    cursor.execute(update_query, (first_name, last_name, actor_id))
    conn.commit()
    print("Record updated successfully")
    cursor.close()
    conn.close()

def insert_record(first_name, last_name):
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="pagila",
        user="admin",
        password="root"
    )
    cursor = conn.cursor()
    insert_query = "INSERT INTO public.actor (first_name, last_name) VALUES (%s, %s)"
    cursor.execute(insert_query, (first_name, last_name))
    conn.commit()
    print("Record inserted successfully")
    cursor.close()
    conn.close()

if __name__ == "__main__":

    insert_record("joao", "alvim")
