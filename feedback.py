global feedback_waiter,event
def feedback():
    global feedback_waiter,event
    print("Your events that you are participed is:",event)
    date1=input("Please insert date for doing relevant feedback: ")
    if (date1 in event):
        if(date1 in feedback_waiter):
            print("There is exist feedback for this event")
        else:
            feedback_waiter[date1]=input("Insert your feedback here: ")
    else:
        print("Wrong date input, return to main page")
"""
feedback()
feedback()
print(feedback_waiter)
"""