---
title : "json 파일을 pasvalVOC format xml 파일로 바꾸기"
categories:
    - data
tags:
    - data
    - python
---

# Change json file to PascalVOC format

## PascalVOC format 구성요소

- `folder` — the parent directory of the image.
- `filename` — the name of the image (including extension).
- `path` — the absolute path of the image
- `source:database` — the original location of the file in a database. Only applicable if a database is used. Otherwise, it will default to `Unknown`.
- `size:width` — the width of the image in pixels.
- `size:height` — the height of the image in pixels.
- `size:depth` — the depth of the image. For object detection tasks, it represents the number of channels.
- `segmented` — determines if the annotations are linear (0) or non-linear (1). Non-linear refers to polygon shapes.
- `object:name` — the label for the object.
- `object:pose` — determines if the object is of different orientation. Normal images default to `Unspecified`.
- `object:truncated` — determines if the object fully (0) or partially visible (1).
Partially visible refers to object that is hidden behind another object.
- `object:difficult` — determines if the object can be easily recognize (0) or difficult to recognize (1).
- `object:bndbox:xmin` — the x coordinate of the top-left position.
- `object:bndbox:ymin` — the y coordinate of the top-left position.
- `object:bndbox:xmax` — the x coordinate of the bottom-right position.
- `object:bndbox:ymax` — the y coordinate of the bottom-right position.

## json 파일 읽어오기

```python
import json

with open(origin_path_dir + filename) as file:
    ann = json.load(file)
```

## xml 파일 생성방법

```python
filename = "파일이름" # 생성시작
root = Element('구성요소 테그 이름') # 구성요소 만들기
SubElement(root, 'folder').text = 'images' # sub element 만들기
tree = ElementTree(root)    # 생성종료
tree.write(destination_path_dir + filename.split(".")[0] +'.xml') # 파일로 내보내기

```

## 전체 코드 예시

```python
import json
from xml.etree.ElementTree import Element, SubElement, ElementTree
import os

# load original file names
origin_path_dir = ''
origin_file_list = os.listdir(origin_path_dir)

# set directory to save xml
destination_path_dir = ''
if not os.path.exists(destination_path_dir):
    os.makedirs(destination_path_dir)

# make pascalVOC format annotation files
for filename in origin_file_list:
    with open(origin_path_dir + filename) as file:
        ann = json.load(file)
    
    filename = ann["imagePath"]

    root = Element('annotation')

    SubElement(root, 'folder').text = 'images'

    SubElement(root, 'filename').text = str(filename)

    SubElement(root, 'path').text = './images/' +  filename

    source = SubElement(root, 'source')
    SubElement(source, 'database').text = 'Unknown'

    size = SubElement(root, 'size')
    SubElement(size, 'width').text = str(ann["imageWidth"])
    SubElement(size, 'height').text = str(ann["imageHeight"])
    SubElement(size, 'depth').text = '3'

    # SubElement(root, 'segmented').text = '0'
    for i in range(len(ann["shapes"])):
        obj = SubElement(root, 'object')
        SubElement(obj, 'name').text = ann["shapes"][i]["label"]

        # SubElement(obj, 'pose').text = 'Unspecified'
        # SubElement(obj, 'truncated').text = '0'

        SubElement(obj, 'difficult').text = '0'
        
        bbox = SubElement(obj, 'bndbox')
        points = ann["shapes"][i]["points"]
        xmin, ymin = ann["imageWidth"], ann["imageHeight"]
        xmax, ymax = 0, 0
        for point in points:
            xmin = min(xmin, point[0])
            ymin = min(ymin, point[1])
            xmax = max(xmax, point[0])
            ymax = max(ymax, point[1])
        SubElement(bbox, 'xmin').text = str(xmin)
        SubElement(bbox, 'ymin').text = str(ymin)
        SubElement(bbox, 'xmax').text = str(xmax)
        SubElement(bbox, 'ymax').text = str(ymax)
    

    tree = ElementTree(root)

    tree.write(destination_path_dir + filename.split(".")[0] +'.xml')
```

## 참고자료

- [https://towardsdatascience.com/convert-pascal-voc-xml-to-yolo-for-object-detection-f969811ccba5](https://towardsdatascience.com/convert-pascal-voc-xml-to-yolo-for-object-detection-f969811ccba5)
- [https://deepbaksuvision.github.io/Modu_ObjectDetection/posts/02_01_PASCAL_VOC.html](https://deepbaksuvision.github.io/Modu_ObjectDetection/posts/02_01_PASCAL_VOC.html)