def password(old, new):
    num="false"
    for char in new:
        if char in "0123456789":
            num="true"

    if old != new and num=="true" and len(new)>5:
        print("Password has been changed")
    else:
        print("Please enter a new password")

old = input("Please enter your old password: ")
new = input("Please enter your new password: ")
password(old,new)