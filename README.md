# Client program for Waste Product Classification using AI

## Before you run the tracker


1. Create a virtual environment - python3 -m venv venv

2. Activate the virtual environment - source venv/bin/activate

3. Intall all the requirements - pip install -r requirements.txt

4. Add a new path as PYTHONPATH variable. 

   To view the existing PYTHONPATH.
   ```bash
   
   >>> python3 
   >>> print(sys.path)
   >>> exit()
   
   ```
   
   To add a new PYTHONPATH in the beginning of the list. This is to make sure that while searching for a specific file it will check for the file in the specified path first. 
   
   In terminal, 
   
   ```bash
   
   export PYTHONPATH=/home/higopika/Desktop/client_program/Yolov5_DeepSort_Pytorch/venv/lib/python3.9/site-packages:$PYTHONPATH
   
   ```


## Tracking sources

Tracking can be run on most video formats

```bash

$ python3 track.py

$ python3 track.py --source 0  # webcam
                           img.jpg  # image
                           vid.mp4  # video
                           path/  # directory
                           path/*.jpg  # glob
                           'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                           'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
                         
```


## References 

https://github.com/dongdv95/yolov5.git

