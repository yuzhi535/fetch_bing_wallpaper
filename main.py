import requests
import json
import os

def verify_folder(folder_name):
   if not os.path.exists(folder_name):
      os.mkdir(folder_name)

def get_image():
    bing_url = '/HPImageArchive.aspx?format=js&idx=0&n=7&mkt=en-US'
    base_url = 'http://www.bing.com'
    base_path = 'bing_wallpaper/'
    verify_folder(base_path)

    context = requests.get(base_url+bing_url)
    if (context.status_code == 200):
        for i in range(7):
            json_response = json.loads(context.content)
            image_url = base_url + json_response['images'][i]['url']
            image_name = json_response['images'][i]['startdate']
            image = requests.get(image_url)

            with open(base_path+image_name+'.jpg', 'wb') as f:
               f.write(image.content)
            print(f'the {i+1}th image has been downloaded!')
        return True

    else:
        return False

if __name__ == "__main__":
    get_image()
