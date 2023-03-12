{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **<center><font style=\"color:rgb(100,109,254)\">Object Detection Software</font> </center>**\n",
    "#### **<center><font style=\"color:rgb(100,109,254)\">By Engr. Zia Ur Rehman</font> </center>**"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Import Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "print(cv2.__version__)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 1.1 Load DNN model YOLOV4-tiny for Object Detection\n",
    "\n",
    "We need two files, one is configuration and other is weights file of the model.\n",
    "\n",
    "#### **<font style=\"color:rgb(255,0,0)\">Link: Download the model and wieght files from this link</font>** \n",
    "https://github.com/ZiaUrRehman-bit/Object-Detection-Software/tree/master/dnn_model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "net = cv2.dnn.readNet(\"dnn_model/yolov4-tiny.weights\", \"dnn_model/yolov4-tiny.cfg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = cv2.dnn_DetectionModel(net)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.setInputParams(size = (320, 320), scale = 1/255)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Capture Frame from Webcam"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cap = cv2.VideoCapture(0)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Object Detection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def detectObject(frame):\n",
    "    \n",
    "    clasIds, score, boundingBox = model.detect(frame)\n",
    "\n",
    "    return clasIds, score, boundingBox"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(round(12.7777, 2))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Read the frames and detect the objects using above created function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "while True:\n",
    "\n",
    "    _, frame = cap.read()\n",
    "\n",
    "    (clasIds, scores, bboxes) = model.detect(frame)\n",
    "\n",
    "    for classId, score, bbox in zip(clasIds, scores, bboxes):\n",
    "\n",
    "        score = round(score, 2)\n",
    "        x, y, w, h = bbox\n",
    "\n",
    "        cv2.putText(frame, f\"Class Id: {classId}, Score: {score}\", \n",
    "                    (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)\n",
    "        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)\n",
    "    \n",
    "    print(f\"Class Id: {clasIds}\\nSocres: {scores}\\nBoundbox: {bboxes}\")\n",
    "\n",
    "    cv2.imshow(\"frames\",frame)\n",
    "\n",
    "    key = cv2.waitKey(1)\n",
    "\n",
    "    if key == ord(\"q\"):\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Get the Class Name and display on frame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "classNamesList = []\n",
    "\n",
    "with open(\"dnn_model/classes.txt\", \"r\") as fileObject:\n",
    "    for className in fileObject.readlines():\n",
    "        className = className.strip()\n",
    "        classNamesList.append(className)\n",
    "\n",
    "# print(classNamesList)\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "while True:\n",
    "\n",
    "    _, frame = cap.read()\n",
    "\n",
    "    (clasIds, scores, bboxes) = model.detect(frame)\n",
    "\n",
    "    for classId, score, bbox in zip(clasIds, scores, bboxes):\n",
    "\n",
    "        score = round(score, 2)\n",
    "        x, y, w, h = bbox\n",
    "        objectName = classNamesList[classId]\n",
    "        cv2.putText(frame, f\"{objectName}\", \n",
    "                    (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)\n",
    "        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)\n",
    "    \n",
    "    print(f\"Class Id: {clasIds}\\nSocres: {scores}\\nBoundbox: {bboxes}\")\n",
    "\n",
    "    cv2.imshow(\"frames\",frame)\n",
    "\n",
    "    key = cv2.waitKey(1)\n",
    "\n",
    "    if key == ord(\"q\"):\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6. Enhance the resolution to increase the accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "classNamesList = []\n",
    "\n",
    "with open(\"dnn_model/classes.txt\", \"r\") as fileObject:\n",
    "    for className in fileObject.readlines():\n",
    "        className = className.strip()\n",
    "        classNamesList.append(className)\n",
    "\n",
    "# print(classNamesList)\n",
    "cap = cv2.VideoCapture(0)\n",
    "cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)\n",
    "cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)\n",
    "\n",
    "while True:\n",
    "\n",
    "    _, frame = cap.read()\n",
    "\n",
    "    (clasIds, scores, bboxes) = model.detect(frame)\n",
    "\n",
    "    for classId, score, bbox in zip(clasIds, scores, bboxes):\n",
    "\n",
    "        score = round(score, 2)\n",
    "        x, y, w, h = bbox\n",
    "        objectName = classNamesList[classId]\n",
    "        cv2.putText(frame, f\"{objectName}\", \n",
    "                    (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)\n",
    "        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)\n",
    "    \n",
    "    print(f\"Class Id: {clasIds}\\nSocres: {scores}\\nBoundbox: {bboxes}\")\n",
    "\n",
    "    cv2.imshow(\"frames\",frame)\n",
    "\n",
    "    key = cv2.waitKey(1)\n",
    "\n",
    "    if key == ord(\"q\"):\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 7. Now Create Interactive Buttons to detect specific object"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **<center><font style=\"color:rgb(100,109,254)\">Full Code</font> </center>**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "classNamesList = []\n",
    "\n",
    "with open(\"dnn_model/classes.txt\", \"r\") as fileObject:\n",
    "    for className in fileObject.readlines():\n",
    "        className = className.strip()\n",
    "        classNamesList.append(className)\n",
    "\n",
    "# print(classNamesList)\n",
    "cap = cv2.VideoCapture(0)\n",
    "cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)\n",
    "cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)\n",
    "\n",
    "buttonPerson = False\n",
    "buttonCell = False\n",
    "buttonRemote = False\n",
    "\n",
    "def clickButton(event, x, y, flags, params):\n",
    "    global buttonPerson, buttonCell, buttonRemote\n",
    "    if event == cv2.EVENT_LBUTTONDOWN:\n",
    "        print(x,y)\n",
    "\n",
    "        polygon = np.array([[(20, 20), (210, 20), (210, 70), (20, 70)]])\n",
    "        polygon1 = np.array([[(20, 80), (220, 80), (210, 130), (20, 130)]])\n",
    "        polygon2 = np.array([[(20, 140), (220, 140), (210, 190), (20, 190)]])\n",
    "\n",
    "        isInside = cv2.pointPolygonTest(polygon, (x, y), False)\n",
    "        isInside1 = cv2.pointPolygonTest(polygon1, (x, y), False)\n",
    "        isInside2 = cv2.pointPolygonTest(polygon2, (x, y), False)\n",
    "\n",
    "        if isInside > 0:\n",
    "            print(\"inside\")\n",
    "\n",
    "            if buttonPerson is False:\n",
    "                buttonPerson = True\n",
    "            else:\n",
    "                buttonPerson = False\n",
    "\n",
    "            print(\"Person Button: \", buttonPerson)\n",
    "        \n",
    "        if isInside1 > 0:\n",
    "            print(\"inside\")\n",
    "\n",
    "            if buttonCell is False:\n",
    "                buttonCell = True\n",
    "            else:\n",
    "                buttonCell = False\n",
    "\n",
    "            print(\"Cell Button: \", buttonCell)\n",
    "        \n",
    "        if isInside2 > 0:\n",
    "            print(\"inside\")\n",
    "\n",
    "            if buttonRemote is False:\n",
    "                buttonRemote = True\n",
    "            else:\n",
    "                buttonRemote = False\n",
    "\n",
    "            print(\"Remote Button: \", buttonRemote)\n",
    "\n",
    "\n",
    "# create window\n",
    "cv2.namedWindow(\"Frame\")\n",
    "cv2.setMouseCallback(\"Frame\", clickButton)\n",
    "\n",
    "while True:\n",
    "\n",
    "    _, frame = cap.read()\n",
    "\n",
    "    (clasIds, scores, bboxes) = model.detect(frame)\n",
    "\n",
    "    for classId, score, bbox in zip(clasIds, scores, bboxes):\n",
    "\n",
    "        score = round(score, 2)\n",
    "        x, y, w, h = bbox\n",
    "        objectName = classNamesList[classId]\n",
    "\n",
    "        if objectName == \"person\" and buttonPerson is True:\n",
    "            cv2.putText(frame, f\"{objectName}\", \n",
    "                        (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)\n",
    "            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)\n",
    "        \n",
    "        if objectName == \"cell phone\" and buttonCell is True:\n",
    "            cv2.putText(frame, f\"{objectName}\", \n",
    "                        (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)\n",
    "            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)\n",
    "        \n",
    "        if objectName == \"remote\" and buttonRemote is True:\n",
    "            cv2.putText(frame, f\"{objectName}\", \n",
    "                        (x-5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)\n",
    "            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)\n",
    "    \n",
    "    \n",
    "    # print(f\"Class Id: {clasIds}\\nSocres: {scores}\\nBoundbox: {bboxes}\")\n",
    "    # Create BUtton\n",
    "    # cv2.rectangle(frame, (20, 20),(210, 70), (200,0,200), -1)\n",
    "    polygon = np.array([[(20, 20), (220, 20), (210, 70), (20, 70)]])\n",
    "    cv2.fillPoly(frame, polygon, (200, 0, 200))\n",
    "    cv2.putText(frame, \"Person\", (30, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)\n",
    "\n",
    "    polygon1 = np.array([[(20, 80), (220, 80), (210, 130), (20, 130)]])\n",
    "    cv2.fillPoly(frame, polygon1, (200, 0, 200))\n",
    "    cv2.putText(frame, \"Phone\", (30, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)\n",
    "\n",
    "    polygon2 = np.array([[(20, 140), (220, 140), (210, 190), (20, 190)]])\n",
    "    cv2.fillPoly(frame, polygon2, (200, 0, 200))\n",
    "    cv2.putText(frame, \"Remote\", (30, 180), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)\n",
    "\n",
    "\n",
    "    cv2.imshow(\"Frame\",frame)\n",
    "\n",
    "    key = cv2.waitKey(1)\n",
    "\n",
    "    if key == ord(\"q\"):\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b671c20432fcd147198c92e7f072af9e705f087eb990bee22b07f08caab9f630"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
