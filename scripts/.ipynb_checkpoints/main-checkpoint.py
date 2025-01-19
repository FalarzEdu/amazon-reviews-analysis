from 'config/connection' import Connection

def main() 
    conn = Connection()

    db = conn.connect();

    if db:
        reviews_collection = db.get_collection("reviews")

        print(reviews_collection)

    db.close();

if __name__ == "__main__":
    main()