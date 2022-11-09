#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os, sys
import rospy
from sensor_msgs.msg import NavSatFix
from sensor_message_getter import SensorMessageGetter
import matplotlib.pyplot as plt
import random

class NavsatfixTrajectory(object):
    def __init__(self, topic, points_size, available_statuses, save_path, colors, end_th=10, msg_wait=1.0):
        self.msg = SensorMessageGetter(topic, NavSatFix, msg_wait)
        self.points_size = points_size
        self.statuses = available_statuses
        self.save_path = save_path
        self.end_th = end_th
        self.colors = colors
        self.flag = 0
        self.count = 0
    
    def spin(self):
        if not self.flag:
            plt.title("gnss trajectory log points with line")
            plt.xlabel("latitude")
            plt.ylabel("Longitude")
            plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
            plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
            for i in range(len(self.colors)):
                plt.plot([], [], color=self.colors[i], label=self.statuses[i])
            plt.legend()
            self.flag = 1
        get_msg = self.msg.get_msg()
        if get_msg is not None:
            self.count = 0
            status = get_msg.status.status
            if status in self.statuses:
                latitude = get_msg.latitude
                longitude = get_msg.longitude
                rospy.loginfo("status = "+str(status)+", latitude = "+str(latitude)+", longitude = "+str(longitude))
                plt.scatter(latitude, longitude, s=self.points_size, color=self.colors[status], label=str(status))
            else:
                rospy.logwarn("The msg is not accurate")
            plt.pause(0.05)
        else:
            rospy.logwarn("No msg in this try.")
            self.count += 1
            if self.count > self.end_th:
                plt.savefig(self.save_path)
                rospy.logwarn("END")
                sys.exit(0)

def main():
    script_name = os.path.basename(__file__)
    node_name = os.path.splitext(script_name)[0]
    rospy.init_node(node_name)

    # param
    navsatfix_topic = rospy.get_param("~navsatfix_topic")
    points_size = rospy.get_param("~points_size")
    save_path = rospy.get_param("~save_path")
    available_statuses = rospy.get_param("~available_statuses")
    colors = rospy.get_param("~colors")

    rospy.loginfo("navsatfix_topic = " + navsatfix_topic)
    rospy.loginfo("points_size = "+ str(points_size))
    rospy.loginfo("save_path = " + save_path)
    rospy.loginfo("available_statuses = " + str(available_statuses))
    rospy.loginfo("colors = " + str(colors))

    rate = rospy.Rate(5)
    node = NavsatfixTrajectory(navsatfix_topic, points_size, available_statuses, save_path, colors)
    while not rospy.is_shutdown():
        node.spin()
        rate.sleep()

if __name__ == '__main__':
    main()