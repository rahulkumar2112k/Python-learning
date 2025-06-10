from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

#MongoDB connection
MONGO_URI=os.getenv("MONGO_URI")

client=MongoClient(MONGO_URI,tlsAllowInvalidCertificates=True)
print(client)

# not a good idea to include id and password in code files we can set env file aand gitignore 
# tlsAllowInvalidCertificates=True- not a good way to handle ssl 


db=client["ytmanager"]
video_collection=db["videos"]


#list video
def list_videos():
    print("\n"+"*" * 100)
    for video in video_collection.find():
        print(f"ID:{video['_id']}, Video Name:{video['name']}, Video Duration:{video['time']}")
    print("\n"+"*" * 100)
# Add Video
def add_video(name, time):
    video_collection.insert_one({"name":name,"time":time})

# Update Video
def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {"$set":{"name":new_name,"time":new_time}}
    )

# Delete Video
def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})


#main function
def main():
    while True:
        print("\n🎬 Youtube Manager App with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App")
        
        choice = input("👉 Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("📌 Enter the video name: ")
            time = input("⏱️ Enter the video time: ")
            add_video(name, time)

        elif choice == '3':
            try:
                video_id = (input("🔄 Enter the video ID to update: "))
                if not ObjectId.is_valid(video_id):
                    print("❌ Invalid ID format. Please enter a valid ObjectId.")
                    continue
                name = input("📌 Enter the new video name: ")
                time = input("⏱️ Enter the new video time: ")
                update_video(video_id, name, time)
            except Exception as e:
                print(f"❌ Error:{e}")

        elif choice == '4':
            try:
                video_id = (input("🗑️ Enter the video ID to delete: "))
                if not ObjectId.is_valid(video_id):
                    print("❌ Invalid ID format. Please enter a valid ObjectId.")
                    continue
                delete_video(video_id)
            except Exception as e:
                print(f"❌ Error:{e}")

        elif choice == '5':
            print("🚀 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

    

if __name__=="__main__":
    main()
    