# import _sqlite3

# conn=_sqlite3.connect('yotube_videos.db')

# cursor=conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS videos(
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         time TEXT NOT NULL
#     )
             
               
# ''')


# def list_videos():
#     cursor.execute("SELECT * FROM videos")
#     for row in cursor.fetchall():
#         print(row)


# def add_video(name,time):
#     cursor.execute("INSERT INTO videos(name,time)VALUES(?,?)",(name,time))
#     conn.commit()


# def update_video(video_id,new_name,new_time):
#     cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
#     conn.commit()



# def delete_video(video_id):
#     cursor.execute("DELETE FROM videos where id=?",(video_id,))
#     conn.commit()



# def main():
#     while True:
#         print("\n Youtube manager app with DB")
#         print("1. List Videos")
#         print("2. Add Videos")
#         print("3. Update Videos")
#         print("4. Delete Videos")
#         print("5. Exit app")
        
#         choice=input ("Enter Your Choice: ")
        
#         if choice =='1':
#             list_videos()
           
            
#         elif choice=='2':
#             name=input("Enter the Video name: ")
#             time=input("Enter the video time: ")
#             add_video(name,time)
            
#         elif choice=='3':
#             video_id=input("Enter video ID to update: ")
#             name=input("Enter the Video name: ")
#             time=input("Enter the video time: ")
#             update_video(video_id,name,time)
           
#         elif choice=='4':
#             video_id=input("Enter video ID to Delete: ")
#             delete_video(video_id)
            
#         elif choice=='5':
#             break
#         else:
#             print("Invalid choice")
                
#     conn.close()          
            


# if __name__=="__main__":
#     main()



import _sqlite3

# Database Connection
conn = _sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Table Creation
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

# List Videos
def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    if not videos:
        print("\n❌ No videos found in the database.")
    else:
        print("\n📋 List of Videos")
        print("-" * 70)
        for row in videos:
            print(f"🎥 ID: {row[0]}, Name: {row[1]}, Duration: {row[2]}")
        print("-" * 70)

# Add Video
def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(f"✅ Video '{name}' added successfully!")

# Update Video
def update_video(video_id, new_name, new_time):
    cursor.execute("SELECT * FROM videos WHERE id=?", (video_id,))
    if cursor.fetchone():
        cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", 
                       (new_name, new_time, video_id))
        conn.commit()
        print(f"✅ Video ID {video_id} updated successfully!")
    else:
        print(f"❌ No video found with ID {video_id}")

# Delete Video
def delete_video(video_id):
    cursor.execute("SELECT * FROM videos WHERE id=?", (video_id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
        conn.commit()
        print(f"✅ Video ID {video_id} deleted successfully!")
    else:
        print(f"❌ No video found with ID {video_id}")

# Main Function
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
                video_id = int(input("🔄 Enter the video ID to update: "))
                name = input("📌 Enter the new video name: ")
                time = input("⏱️ Enter the new video time: ")
                update_video(video_id, name, time)
            except ValueError:
                print("❌ Invalid ID format. Please enter a number.")

        elif choice == '4':
            try:
                video_id = int(input("🗑️ Enter the video ID to delete: "))
                delete_video(video_id)
            except ValueError:
                print("❌ Invalid ID format. Please enter a number.")

        elif choice == '5':
            print("🚀 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
