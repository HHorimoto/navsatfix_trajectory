#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

class SensorMessageGetter(object):
    def __init__(self, topic, msg_type, msg_wait=1.0):
        self.msg_wait = msg_wait
        self.topic = topic
        self.msg_type = msg_type

    def get_msg(self):
        message = None
        try:
            message = rospy.wait_for_message(
                self.topic, self.msg_type, self.msg_wait)
        except rospy.exceptions.ROSException as e:
            rospy.logdebug(e)
        return message