#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from my_robot_controller.msg import encodermsg

start_sp_l = 0
start_sp_r = 0
Fi = 0
real_Omega = 0
real_V = 0
pos_X = 0
pos_Y = 0
prev_ENC_l = 0
prev_ENC_r = 0
ENC_l = 0
ENC_r = 0

def speed_callback(speed: Twist):
    global start_sp_l, start_sp_r, Fi, real_Omega, real_V, pos_X, pos_Y, prev_ENC_l, prev_ENC_r, ENC_l, ENC_r
    msg_enc = encodermsg()
    msg_odom = Odometry()
    msg_enc.header = rospy.Time.now()
    msg_odom.header.frame_id = "Odom"

    V = speed.linear.x
    Omega = speed.angular.z
    r = 0.033
    L = 0.287
    if Omega == 0:
        V_left_wheel = V_right_wheel = V
        Omega_l_wheel = V_left_wheel/r
        Omega_r_wheel = V_right_wheel/r
    else:
        R = V/Omega
        V_left_wheel = Omega * (R - 0.5 * L)
        V_right_wheel = Omega * (R + 0.5 * L)
        Omega_l_wheel = V_left_wheel/r
        Omega_r_wheel = V_right_wheel/r

    change_sp_l = 0
    change_sp_r = 0
    delta_sp_l = Omega_l_wheel - start_sp_l
    delta_sp_r = Omega_r_wheel - start_sp_r
    for i in range(3):
        x_now = i * 0.1
        x_next = x_now + 0.1
        real_Omega_now = real_Omega
        real_V_now = real_V
        change_sp_l += (((delta_sp_l*10/math.exp(10*x_now)) + (delta_sp_l*10/math.exp(10*x_next)))/2) * (x_next-x_now)
        change_sp_r += (((delta_sp_r*10/math.exp(10*x_now)) + (delta_sp_r*10/math.exp(10*x_next)))/2) * (x_next-x_now)
        cur_sp_l = start_sp_l + change_sp_l
        cur_sp_r = start_sp_r + change_sp_r
        if -0.0001 < cur_sp_l < 0.0001:
            cur_sp_l = 0
        if -0.0001 < cur_sp_r < 0.0001:
            cur_sp_r = 0

        if ENC_l > 4096:
            ENC_l = 0
        elif ENC_l < 0:
            ENC_l = 4096
        if ENC_r > 4096:
            ENC_r = 0
        elif ENC_r < 0:
            ENC_r = 4096
        
        now_ENC_l = ((cur_sp_l*4096*0.1)/(2*math.pi)) - prev_ENC_l
        now_ENC_r = ((cur_sp_r*4096*0.1)/(2*math.pi)) - prev_ENC_r
        prev_ENC_l = now_ENC_l
        prev_ENC_r = now_ENC_r
        ENC_l += now_ENC_l
        ENC_r += now_ENC_r
        msg_enc.num1 = round(ENC_l)
        msg_enc.num2 = round(ENC_r)

        real_Omega = (cur_sp_r - cur_sp_l)*r/L
        Fi += ((real_Omega + real_Omega_now)/2)*(x_next-x_now)
        real_V = (cur_sp_l + cur_sp_r)*r/2
        pos_X += (real_V*math.cos(Fi) + real_V_now*math.cos(Fi))*(x_next-x_now)
        pos_Y += (real_V*math.sin(Fi) + real_V_now*math.sin(Fi))*(x_next-x_now)

        #msg_odom.pose.pose.position.z = Fi
        msg_odom.pose.pose.position.x = pos_X
        msg_odom.pose.pose.position.y = pos_Y
        
        rospy.loginfo(str(msg_odom.header.frame_id)+str(msg_odom.pose.pose.position.x)+","+str(msg_odom.pose.pose.position.y))
        #rospy.loginfo("[" + str(msg_enc.header.secs) + "]" + str(msg_enc.num1) + "," + str(msg_enc.num2))
        
        pub.publish(msg_enc)
        pub_odom.publish(msg_odom)
    start_sp_l = cur_sp_l
    start_sp_r = cur_sp_r


if __name__ == '__main__':
    rospy.init_node("turtle_controller")
    pub = rospy.Publisher("/topic_ex", encodermsg, queue_size=10)
    pub_odom = rospy.Publisher("/topic_odom", Odometry, queue_size=10)
    sub = rospy.Subscriber("/cmd_vel", Twist, callback=speed_callback)
    rospy.loginfo("Node has been started !")
    
    rospy.spin()
