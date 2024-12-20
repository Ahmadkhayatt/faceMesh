import cv2 
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
ptime = 0 

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
FaceMesh = mpFaceMesh.FaceMesh(max_num_faces = 2)
drawSpec = mpDraw.DrawingSpec (thickness = 1 , circle_radius = 1)




while True :
    success , img = cap.read()
    
    imgRgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = FaceMesh.process(imgRgb)
    # print(results)
    if results.multi_face_landmarks :
        for faceLms in results.multi_face_landmarks:
            # print(id,detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACEMESH_TESSELATION, drawSpec, drawSpec )



    cTime = time.time()
    fps = 1/(cTime - ptime)
    ptime = cTime
    cv2.putText(img , str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,0),3)

    cv2.imshow('nigga',img)
    if cv2.waitKey(1) == ord('q'):
        break
