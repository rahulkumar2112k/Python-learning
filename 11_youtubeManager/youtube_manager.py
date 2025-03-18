# import json

# def load_data():
#     try:
#         with open('youtube.txt','r')as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
    
    
# def save_data_helper(videos):
#     with open('youtube.txt','w')as file:
#         json.dump(videos,file)

# def list_all_videos(videos):
#     print("\n")
#     print("*" *70)
#     for index,video in enumerate(videos,start=1):
#         print(f"{index}.{video['name']}, Duration :{video['time']}")
#     print("\n")
#     print("*" *70)

# def add_videos(videos):
#     name=input("Enter video name: ")
#     time=input("Enter video time: ")
#     videos.append({'name':name, 'time':time})
#     save_data_helper(videos)
    


# def update_videos(videos):
#     list_all_videos(videos)
#     index=int(input("Enter the video number to update:"))
#     if 1<=index<=len(videos):
#         name=input("Enter the new Video name:")
#         time=input("Enter the new Video time:")
#         videos[index-1]={'name':name,'time':time}
#         save_data_helper(videos)
#     else:
#         print("Invalid index selected")    



# def delete_videos(videos):
#     list_all_videos(videos)
#     index=int(input("Enter the video number to be deleted:"))
    
#     if 1<=index<=len(videos):
#         del videos[index-1]
#         save_data_helper(videos)
        
#     else:
#         print("Invalid video number")
        


# def main():
    
#     videos= load_data()
    
#     while True:
#         print("\n Youtube Manager | choose an option ")
#         print("1. List all youtube videos ")
#         print("2. Add a youtube video ")
#         print("3. update a youtube video details ")
#         print("4. Delete a youtube video ")
#         print("5. Exit the app")
#         choice=input("Enter your choice :")
       
        

#         match choice:
#             case '1':
#                 list_all_videos(videos)
            
#             case '2':
#                 add_videos(videos)
                
#             case '3':
#                 update_videos(videos)
                
#             case '4':
#                 delete_videos(videos)    
                
#             case '5':
#                 break
            
#             case _:
#                 print("Invalid choice")
                
# if __name__== "__main__":
#         main()




import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    if not videos:
        print("No videos available.")
        return
    print("\n" + "*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 70)

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("✅ Video added successfully!")

def update_videos(videos):
    if not videos:
        print("No videos available to update.")
        return

    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            videos[index - 1] = {'name': name, 'time': time}
            save_data_helper(videos)
            print("✅ Video updated successfully!")
        else:
            print("❌ Invalid index selected.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_videos(videos):
    if not videos:
        print("No videos available to delete.")
        return

    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to delete: "))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_data_helper(videos)
            print("✅ Video deleted successfully!")
        else:
            print("❌ Invalid video number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    videos = load_data()
    
    while True:
        print("\n🎬 Youtube Manager | Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                print("🚀 Exiting... Goodbye!")
                break
            case _:
                print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


