from multiprocessing.sharedctypes import Value
import re
import sys

timetable = {
    "1": "13",
    "2": "14",
    "3": "15",
    "4": "16",
    "5": "17",
    "6": "18",
    "7": "19",
    "8": "20",
    "9": "21",
    "10": "22",
    "11": "23"
}

def main():
    print(convert(input("Hours: ")))

def convert24(str1):

    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]

def convert(s):
    time = re.search(r"^(([1-9]|[0-1][0-2])(:)*([1-5]?[0-9])*( )*(AM|PM)) to (([1-9]|[0-1][0-2])(:)*([1-5]?[0-9])*( )*(AM|PM))$",s)
    #^([0-9])(:)*(00)* (AM) to ([0-9])(:)*(00)* (PM)$
    #print(time)
    if time:
        seperated_time = time.groups()
        print(seperated_time)
        seperated_time = list(seperated_time)
        #checks the invalid time


        #for the 9 AM to 9 PM Type
        if len(seperated_time[0]) == 4 and len(seperated_time[6]) == 4:
            a = seperated_time[0]
            b = "0"+ a[0] + ":" + "00 " + a[2] + a[3]
            seperated_time[0] = b
            c = seperated_time[6]
            d = "0"+ c[0] + ":" + "00 " + c[2] + c[3]
            seperated_time[6] = d
        #For the 12 AM to 12 PM type
        if len(seperated_time[0]) == 5 and len(seperated_time[6]) == 5:
            a = seperated_time[0]
            b =  a[0] + a[1] + ":" + "00 " + a[3] + a[4]
            seperated_time[0] = b
            e = seperated_time[6]
            f = "0"+ e[0] + ":" + "00 " + e[2] + e[3]
            seperated_time[6] = f

        if len(seperated_time[0]) == 7:
            seperated_time[0] = "0" + seperated_time[0]
        if len(seperated_time[6]) == 7:
            seperated_time[6] = "0" + seperated_time[6]

        if seperated_time[0].endswith("PM"):
            first_time = convert24(seperated_time[0])
        else:
            first_time = seperated_time[0]
        if seperated_time[6].endswith("PM"):
            second_time = convert24(seperated_time[6])
        else:
            second_time = seperated_time[6]


        return first_time[:-3] + " to " + second_time[:-3]
        """
        turned1 = None
        turned2 = None
        if seperated_time[0].endswith("PM"):
            turned1 = timetable[seperated_time[1]]

        if seperated_time[6].endswith("PM"):
            turned2 = timetable[seperated_time[7]]

        if turned1 and turned2:
            output = turned1 + ":" + seperated_time[3] + " to " + turned2 + ":" + seperated_time[9]
        if turned1:
            if seperated_time[9] == 0:
                output = turned1 + ":" + seperated_time[3] + " to " + seperated_time[7] + ":0" + seperated_time[9]
            else:

             output = turned1 + ":" + seperated_time[3] + " to " + seperated_time[7] + ":" + seperated_time[9]
        if turned2:
            if seperated_time[3] == 0:

                output = seperated_time[1] + ":" + seperated_time[3] + "0 to " + turned2 + ":" + seperated_time[9]
            else:

             output = seperated_time[1] + ":" + seperated_time[3] + " to " + turned2 + ":" + seperated_time[9]

        else:
            output = seperated_time[1] + ":" + seperated_time[3] + " to " + seperated_time[7] + ":" + seperated_time[9]
        if len(output) == 11:
            output = output.replace("0","00")
        return output
       # print(seperated_time)
       """
        """
            if ":" in seperated_time[0]:

                m2 = seperated_time[0]
                in_time = datetime.strptime(m2, "%I:%M %p")
                out_time = datetime.strftime(in_time, "%H:%M")
            else:
                m2 = seperated_time[0]
                in_time = datetime.strptime(m2, "%I %p")
                out_time = datetime.strftime(in_time, "%H:%M")
            if ":" in seperated_time[6]:

                m3 = seperated_time[6]
                in3_time = datetime.strptime(m3, "%I:%M %p")
                out_time3 = datetime.strftime(in3_time, "%H:%M")
            else:
                m3 = seperated_time[6]
                in3_time = datetime.strptime(m3, "%I %p")
                out_time3 = datetime.strftime(in3_time, "%H:%M")
            """
            #output = out_time + " to " + out_time3
            #return output
    else:
        raise ValueError









if __name__ == "__main__":
    main()