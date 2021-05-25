import cv2
import numpy as np
import math
import mediapipe as mp

mp_holistic = mp.solutions.holistic

index_list = [1, 152, 130, 359, 61, 291]

cap = cv2.VideoCapture(1)

with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():

        success, image = cap.read()
        height, width, _ = image.shape
        size = image.shape
    
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        
        try:
            results = holistic.process(image)

            face_point_x = []
            face_point_y = []
            for i in index_list:
                face_point_x.append(results.face_landmarks.landmark[i].x * width)
                face_point_y.append(results.face_landmarks.landmark[i].y * height)
            face_point = list(zip(face_point_x, face_point_y))

            image_points = np.array([
                face_point[0],     # Nose tip

                face_point[1],     # Chin

                face_point[2],     # Left eye left corner

                face_point[3],     # Right eye right corne

                face_point[4],     # Left Mouth corner

                face_point[5]      # Right mouth corner
            ], dtype="double")

            # 3D model points.

            model_points = np.array([

                (0.0, 0.0, 0.0),             # Nose tip

                (0.0, -330.0, -65.0),        # Chin

                (-225.0, 170.0, -135.0),     # Left eye left corner

                (225.0, 170.0, -135.0),      # Right eye right corne

                (-150.0, -150.0, -125.0),    # Left Mouth corner

                (150.0, -150.0, -125.0)      # Right mouth corner
            ])

            # Camera internals



            focal_length = size[1]

            center = (size[1]/2, size[0]/2)

            camera_matrix = np.array(

                                     [[focal_length, 0, center[0]],

                                     [0, focal_length, center[1]],

                                     [0, 0, 1]], dtype = "double"

                                     )

            dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
            (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_UPNP)
            (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)



            for p in image_points:
                cv2.circle(image, (int(p[0]), int(p[1])), 3, (0,0,255), -1)

            p1 = ( int(image_points[0][0]), int(image_points[0][1]))
            p2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))

            cv2.line(image, p1, p2, (255,0,0), 2)
            cv2.line(image, (0, int(face_point[0][1])), (width, int(face_point[0][1])), (255, 0, 0), 2)
            if p2[1] > p1[1] + 50:
                cv2.putText(image, "LOOKING DOWN", (20, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))


            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        except:
            cv2.putText(image, "NO DETECTION", (20, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
            pass
        cv2.imshow('MediaPipe Pose', image)
        if cv2.waitKey(5) & 0xFF == ord("q"):
          break
cap.release()
cv2.destroyAllWindows()