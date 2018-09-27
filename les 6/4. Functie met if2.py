def password(old, new):
    num=False
    for char in new:
        if char in "0123456789":
            num=True

    if old != new and len(new)>5 and num:
        print("Password has been changed")
    else:
        print("Please enter a new password")

old = input("Please enter your old password: ")
new = input("Please enter your new password: ")
password(old,new)