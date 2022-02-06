from google_images_download import google_images_download
response = google_images_download.googleimagesdownload() 

queries = ['pine tree', 'oak tree', 'rose flower', 'daisy flower', 'robin bird', 'canary bird', 'sunfish', 'salmon']
for qq in queries:
    arguments = {"keywords": qq,
                    #"format": "jpg",
                    "limit":1000,
                    'chromedriver':r'C:\Users\curti\Downloads\chromedriver.exe'}
    response.download(arguments)