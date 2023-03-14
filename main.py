
import cv2
import numpy as np

net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")

model = cv2.dnn_DetectionModel(net)

model.setInputParams(size = (320, 320), scale = 1/255)

classNamesList = []

with open("dnn_model/classes.txt", "r") as fileObject:
    for className in fileObject.readlines():
        className = className.strip()
        classNamesList.append(className)

# print(classNamesList)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

buttonPerson = False
buttonCell = False
buttonRemote = False

color = (200,0,200)
color1 = (200,0,200)
color2 = (200,0,200)

def clickButton(event, x, y, flags, params):
    global buttonPerson, buttonCell, buttonRemote, color, color1, color2
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

        polygon = np.array([[(20, 20), (210, 20), (210, 70), (20, 70)]])
        polygon1 = np.array([[(20, 80), (220, 80), (210, 130), (20, 130)]])
        polygon2 = np.array([[(20, 140), (220, 140), (210, 190), (20, 190)]])

        isInside = cv2.pointPolygonTest(polygon, (x, y), False)
        isInside1 = cv2.pointPolygonTest(polygon1, (x, y), False)
        isInside2 = cv2.pointPolygonTest(polygon2, (x, y), False)

        if isInside > 0:
            print("inside")

            if buttonPerson is False:
                buttonPerson = True
                color = (0,255,0)
            else:
                buttonPerson = False
                color = (200,0,200)

            print("Person Button: ", buttonPerson)
        
        if isInside1 > 0:
            print("inside")

            if buttonCell is False:
                buttonCell = True
                color1 = (0,255,0)
            else:
                buttonCell = False
                color1 = (200,0,200)

            print("Cell Button: ", buttonCell)
        
        if isInside2 > 0:
            print("inside")

            if buttonRemote is False:
                buttonRemote = True
                color2 = (0,255,0)
            else:
                buttonRemote = False
                color2 = (200,0,200)

            print("Remote Button: ", buttonRemote)


# create window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", clickButton)

while True:

    _, frame = cap.read()

    (clasIds, scores, bboxes) = model.detect(frame)

    for classId, score, bbox in zip(clasIds, scores, bboxes):

        score = round(score, 2)
        x, y, w, h = bbox
        objectName = classNamesList[classId]

        if objectName == "person" and buttonPerson is True:
            cv2.putText(frame, f"{objectName}", 
                        (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
        
        if objectName == "cell phone" and buttonCell is True:
            cv2.putText(frame, f"{objectName}", 
                        (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
        
        if objectName == "remote" and buttonRemote is True:
            cv2.putText(frame, f"{objectName}", 
                        (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
    
    
    # print(f"Class Id: {clasIds}\nSocres: {scores}\nBoundbox: {bboxes}")
    # Create BUtton
    # cv2.rectangle(frame, (20, 20),(210, 70), (200,0,200), -1)
    polygon = np.array([[(20, 20), (220, 20), (210, 70), (20, 70)]])
    cv2.fillPoly(frame, polygon, color)
    cv2.putText(frame, "Person", (30, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    polygon1 = np.array([[(20, 80), (220, 80), (210, 130), (20, 130)]])
    cv2.fillPoly(frame, polygon1, color1)
    cv2.putText(frame, "Phone", (30, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    polygon2 = np.array([[(20, 140), (220, 140), (210, 190), (20, 190)]])
    cv2.fillPoly(frame, polygon2, color2)
    cv2.putText(frame, "Remote", (30, 180), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)


    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()