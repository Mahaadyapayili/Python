def shutdown():
    print ("System Shuting down!!!!")

    user_input = input("Enter your response: ")
    
    if user_input == "yes":
        print("Shutting down")
    elif user_input == "no":
        print("Abort shut down")
    else:
        print("Sorry")

shutdown()