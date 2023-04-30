from controller import Robot
from controller import LED

robot = Robot()

time = int(robot.getBasicTimeStep())

ds = []
ds_names = ["ds_right", "ds_left", "ds_mid_right", "ds_mid_left","ds_right_wall", "ds_left_wall", "ds_front_wall", "ds_mid_right2", "ds_mid_left2","ds_right_wallback","ds_left_wallback"]
ds_val = [0]*len(ds_names)

for name in ds_names:

    ds.append(robot.getDevice(name))
    ds[-1].enable(time)
    
wheels =[]
wheel_names = ["front_right_motor", "front_left_motor", "rear_right_motor", "rear_left_motor"]    

for name in wheel_names:

    wheels.append(robot.getDevice(name))
    wheels[-1].setPosition(float('inf'))
    wheels[-1].setVelocity(0.0)

led =[]
led_names = ["led_right", "led_mid", "led_left"]    

for name in led_names:

    led.append(robot.getDevice(name))

last_error = intg = diff = prop = 0
kp = 0.0009
ki = 0
kd = 0.001    

def pid(error):

    global last_error, intg, diff, prop, kp, ki, kd
    prop = error
    intg = error + intg
    diff = error - last_error
    balance = (kp*prop) + (ki*intg) + (kd*diff)
    last_error = error
    return balance

def setSpeed(base_speed, balance):

    wheels[0].setVelocity(base_speed + balance)
    wheels[1].setVelocity(base_speed - balance)
    wheels[2].setVelocity(base_speed + balance)
    wheels[3].setVelocity(base_speed - balance)

stop = 0
ctr = 0
temp=0
 
while robot.step(time) != -1:

    for i in range(len(ds)):
    
        ds_val[i] = ds[i].getValue()
        print(f"{ds_names[i]} : {ds_val[i]}\n" + "*"*40 )
    
    
    print(int(ctr))
        
    
    if ds_val[2] < 350 and ds_val[3] < 350:
            error = 0
            rectify = pid(error)
            print(rectify)
            setSpeed(2,0)
            led[1].set(0)            
            print("Case 0")
            if ds_val[4] < 950:
                temp = 1
            if ds_val[4]<950 and ds_val[9]>950:
                 ctr=ctr+1
        
            if ds_val[5]<950 and ds_val[10]>950:
                 ctr=ctr+1
           
            if ds_val[4] < 950:
                led[0].set(1)
                
            elif ds_val[4] > 950:
                led[0].set(0) 
            
            if ds_val[5] < 950:
                led[2].set(1)
                
            elif ds_val[5] > 950:
                led[2].set(0)         
            
            
                  
            if ds_val[0] < 650 and ds_val[1] < 650:
               led[0].set(1)
               led[1].set(1)
               led[2].set(1)
               
               
   
    elif ds_val[2] < 950 and ds_val[3] < 950 and ds_val[0] < 950 and ds_val[1] < 950:
            print("Case 00")
            led[1].set(0)
            
            if ds_val[4] < 950:
                led[0].set(1)
                
            elif ds_val[4] > 950:
                led[0].set(0) 
            
            if ds_val[5] < 950:
                led[2].set(1)
                
            elif ds_val[5] > 950:
                led[2].set(0)         
            
            if  ds_val[4]< 950 and ds_val[5] > 950 and ds_val[6] > 950:
                setSpeed(5,0)
                print("case 01")
                stop = 1
            elif ds_val[4] > 780 and ds_val[5] > 950 and ds_val[6] > 950:
                
                setSpeed(1,-3)
                print("Case 02")
                if ds_val[4] > 700:
                    setSpeed(0,1) 
            
            elif ds_val[4] < 950 and ds_val[5] > 950 and ds_val[6] < 950:
               
                print("Case 03")
                if ds_val[4] < 700:               
                    setSpeed(3,2)
                    print("Case 03A")
                                
            
    
    elif ds_val[7] < 950 and ds_val[8] > 950 and ds_val[0] < 950 and ds_val[1] > 950:
            error = 0
            rectify = pid(error)
            print(rectify)
            setSpeed(4,-1*rectify)
            print("Case wtf1")
            
            
    
    elif ds_val[7] > 950 and ds_val[8] < 950 and ds_val[0] > 950 and ds_val[1] < 950:
            error = 0
            rectify = pid(error)
            print(rectify)
            setSpeed(4,-1*rectify)
            print("Case wtf3")
            if ds_val[4] < 950:
                led[0].set(1)
                
            elif ds_val[4] > 950:
                led[0].set(0) 
            
            if ds_val[5] < 950:
                led[2].set(1)
                
            elif ds_val[5] > 950:
                led[2].set(0) 
            
            if ds_val[4]<950 and ds_val[9]>950:
                 ctr=ctr+1
        
            if ds_val[5]<950 and ds_val[10]>950:
                 ctr=ctr+1
            
            
   
                                                     
    elif ds_val[2] > 950 and ds_val[3] < 950 and ds_val[0] > 950 and ds_val[5] > 950:
            
            setSpeed(3,3)
            print("Case 1")
                
    elif ds_val[2] < 950 and ds_val[3] > 950 and ds_val[1] > 950 and ds_val[5] > 950:
            
            setSpeed(3,-3)
            print("Case 2")         
           
    elif ds_val[0] > 950 and ds_val[1] > 950 and ds_val[2] > 950 and ds_val[3] > 950 and ds_val[5] < 950:
           
            setSpeed(3,0)
            
            print("Case 3")
            
                
    
   
                           
    elif ds_val[0] > 950 and temp==0:
            error = ds_val[1] - 200
            rectify = pid(error)
            print(rectify)
            setSpeed(0.4,-1*rectify)
            print("Case 5")
    
    
    a = ctr%2
    b = (ctr//2)%2
    c = (ctr//2)//2
    if ds_val[0] > 950 and ds_val[1] > 950 and ds_val[2] > 950 and ds_val[3] > 950:
        led[0].set(int(a))
        led[1].set(int(b))
        led[2].set(int(c))  
    
                           
    pass
