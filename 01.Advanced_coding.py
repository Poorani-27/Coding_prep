'''Problem statement. 
An automobile company manufacturers both a two Wheeler and a 4 Wheeler. A company manager wants to make the production of both the type of vehicles according Given data below.
 first data,  total number of Vehicle(2 Wheeler + 4 Wheeler) equal to V.
   second data, Total number of wheels equal to W. 
   The task is to find how many two wheelers as well as 4 wheelers need to manufacture as per the given data.
     Input format 
     value of V= 200
     value of w = 540
    output format
      TW equal to 130 
      FW equal to 70
        Explanation.
          130 + 70  = 200 vehicles 
          (70*4)+ (130 *2) = 540 wheelss'''

def finding_wheels(v,w):
    if w<=v :
        print("Invalid ")
    else:
        x=((v*4)-w)//2
        print(v*4)
        print((v*4)-w)
        print((((v*4))-w)//2)

        tw=x
        fw=v-x
        print(tw,fw)

v=200
w=540
finding_wheels("tw=",v,"fw=",w)