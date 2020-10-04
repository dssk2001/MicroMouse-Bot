#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = None

def clbk(msg):
  reg = {
    'Right': min(min(msg.ranges[0:44]),10),
    'Front': min(min(msg.ranges[45:134]),10),
    'Left': min(min(msg.ranges[135:179]),10),
  }
  
  check_to_move(reg)
  
def check_to_move(reg):
  msg = Twist()
  linear_x = 0
  angular_z = 0
  frnt_lim = 0.3
  left_lim = 3
  rt_lim = 0.2
  
  direction = ''
  
  if(reg['Front']>frnt_lim and reg['Left']<left_lim and reg['Right']<rt_lim):
    print(reg['Right'],reg['Front'],reg['Left'])
    direction = 'Front 1'
    linear_x = -0.03
    angular_z=0
    
  elif(reg['Front']<frnt_lim and reg['Left']>left_lim and reg['Right']<rt_lim ):
    print(reg['Right'],reg['Front'],reg['Left'])
    direction = 'Left'
    linear_x = 0.01
    angular_z = 60
    
  elif(reg['Front']<frnt_lim and reg['Left']<left_lim and reg['Right']>rt_lim) :
    print(reg['Right'],reg['Front'],reg['Left'])
    direction = 'Right'
    linear_x = 0.01
    angular_z = -60

    
    
  elif(reg['Front']>frnt_lim and reg['Left']<left_lim and reg['Right']>rt_lim and reg['Front'] > reg['Right']):
    print(reg['Right'],reg['Front'],reg['Left'])
    direction = 'Front 2'
    linear_x = -0.03
    angular_z = 0
    
  elif(reg['Front']>frnt_lim and reg['Left']<left_lim and reg['Right']>rt_lim and reg['Front'] < reg['Right']):
    print(reg['Right'],reg['Front'],reg['Left'])
    direction = 'Right 2'
    linear_x = 0.01
    angular_z = -60
    


  else:
    print(reg['Right'],reg['Front'],reg['Left'])
    #direction = 'Front 3'
    #linear_x = -0.03
    #angular_z = 0
  
  #direction = 'Front'
  #linear_x = -0.3
  #angular_z = 0
  
  rospy.loginfo(direction)  
  msg.linear.x = linear_x
  msg.angular.z = angular_z
  pub.publish(msg)
  
def start():
  global pub
  
  rospy.init_node('laser_reading')
  
  pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
  sub = rospy.Subscriber('/scan_top',LaserScan,clbk)
  rospy.spin()
  
if __name__ == '__main__':
  start()
