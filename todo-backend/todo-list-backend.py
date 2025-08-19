from flask import Flask, request
import os
import psycopg2
import logging
import time
import sys

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ],
    format="%(levelname)s:%(name)s:%(message)s"
)
logger = logging.getLogger(__name__)

def get_db_connection():
    conn = None
    while True:
        try:
            conn = psycopg2.connect(
                host=os.environ.get('DB-SVC-NAME'),
                port=int(os.environ.get('DB-PORT')),
                dbname=os.environ.get('DB-NAME'),
                user=os.environ.get('DB-USER', "postgres"),
                password=str(os.environ.get('DB-PASSWORD', 'postgres'))
            )
            break
        except psycopg2.OperationalError as e:
            logger.error(f"Attempting to connect to the database...")
            time.sleep(2)
    return conn

conn = get_db_connection()

if conn is None:
    logger.error("Failed to connect to the database after multiple retries. Exiting.")
    exit(1)

cur = conn.cursor()

def init_db():
    cur.execute("CREATE TABLE IF NOT EXISTS todos (id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, todo_item TEXT)")

    # some base values that were already there
    cur.execute("INSERT INTO todos(todo_item) VALUES ('Bake a cake')")
    cur.execute("INSERT INTO todos(todo_item) VALUES ('Learn basic networking')")
    cur.execute("INSERT INTO todos(todo_item) VALUES ('Learn containerization')")

    conn.commit()

    logger.info("DB connection established and initialised")


init_db()

def get_todos_list_from_db():
    logger.info("GET request sent to backend")
    cur.execute("SELECT todo_item FROM todos")

    return [item[0] for item in cur.fetchall()]

def append_todo_item_to_db(new_todo):
    logger.info(f"Append request sent to backend: {new_todo}")
    cur.execute("INSERT INTO todos(todo_item) VALUES (%s)", (new_todo,))

    conn.commit()

@app.route('/healthz')
def readiness_health_check():
    try:
        cur.execute("SELECT 1")
        return ("db conn ok", 200)
    except:
        return ("db conn fail", 500)

@app.route('/todos', methods=["GET", "POST"])
def get_todos():
    if request.method == "POST":
        todo_task = request.values.get("todo-input")

        if len(todo_task) > 140:
            logger.warning(f"TODO ITEM TOO LONG (>140 chars): {todo_task}")
            return "failure"
        
        logger.info(f"SUCCESSFULLY ADDED TODO ITEM: {todo_task}")
        append_todo_item_to_db(todo_task)
        return "success"

    return get_todos_list_from_db()

@app.route('/')
def health_check():
    return f"Server Healthy!", {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get('BACKEND-PORT', 4040))) # 4040 as backup for my sanity

