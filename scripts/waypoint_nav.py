#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def move_to_goal(x, y, z, w):
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y

    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    client.send_goal(goal)
    client.wait_for_result()

    return client.get_result()

if __name__ == '__main__':
    rospy.init_node('waypoint_nav')
    waypoints = [
        (-1.15, -2.85, 0.0, 1.0),
        (-2.1, -3.4, 0.0, 1.0),
        (0.5, -1.25, 0.0, 1.0),
        (-2.45, -2, 0.0, 1.0),
        (-2.65, -3.0, 0.0, 1.0)
    ]

    for point in waypoints:
        rospy.loginfo("Gidiliyor: {}".format(point))
        move_to_goal(*point)
        rospy.sleep(2)

    rospy.loginfo("Bitti!")
