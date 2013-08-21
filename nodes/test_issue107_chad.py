#!/usr/bin/env python

import rospy

from dynamic_reconfigure.server import Server
from test_dynamic_reconfigure.cfg import SumConfig


def callback(config, level):
    # Comment out this loginfo that is taken from tutorial; causes 
    # runtime error.    
    ##rospy.loginfo("""Reconfigure Request: {int_param}, {double_param},\
    ##    {str_param}, {bool_param}, {size}""".format(**config))
    return config

if __name__ == "__main__":
    rospy.init_node("testnode_dynamic_reconfigure_chad", anonymous=True)

    srv = Server(SumConfig, callback)
    rospy.spin()
