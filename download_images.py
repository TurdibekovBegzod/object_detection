from simple_image_download import simple_image_download as simp

response = simp.simple_image_download()
keywords = ["building workers"]

for kw in keywords:
    try:
        response.download(kw, 50)
    except Exception as e:
        print("Xato:", e)