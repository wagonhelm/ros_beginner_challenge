;; Auto-generated. Do not edit!


(when (boundp 'challenge::CustomMessage)
  (if (not (find-package "CHALLENGE"))
    (make-package "CHALLENGE"))
  (shadow 'CustomMessage (find-package "CHALLENGE")))
(unless (find-package "CHALLENGE::CUSTOMMESSAGE")
  (make-package "CHALLENGE::CUSTOMMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude CustomMessage.msg.html


(defclass challenge::CustomMessage
  :super ros::object
  :slots (_number_1 _number_2 ))

(defmethod challenge::CustomMessage
  (:init
   (&key
    ((:number_1 __number_1) 0)
    ((:number_2 __number_2) 0)
    )
   (send-super :init)
   (setq _number_1 (round __number_1))
   (setq _number_2 (round __number_2))
   self)
  (:number_1
   (&optional __number_1)
   (if __number_1 (setq _number_1 __number_1)) _number_1)
  (:number_2
   (&optional __number_2)
   (if __number_2 (setq _number_2 __number_2)) _number_2)
  (:serialization-length
   ()
   (+
    ;; uint32 _number_1
    4
    ;; uint32 _number_2
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _number_1
       (write-long _number_1 s)
     ;; uint32 _number_2
       (write-long _number_2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _number_1
     (setq _number_1 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _number_2
     (setq _number_2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get challenge::CustomMessage :md5sum-) "a943712877e7ef9d7005faad2d1b0651")
(setf (get challenge::CustomMessage :datatype-) "challenge/CustomMessage")
(setf (get challenge::CustomMessage :definition-)
      "uint32 number_1
uint32 number_2

")



(provide :challenge/CustomMessage "a943712877e7ef9d7005faad2d1b0651")


