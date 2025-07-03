# main_dict={}
# while True:
#     choice=int(input("1.Add contact\n2.View contact\n3.Update contact\n4.Dlt contact\n5.Exit\nEnter your choice:"))
#     if choice == 1:
#         sub_dict={}
#         na=input("enter the name:")
#         sub_dict["name"]=na
#         ph=int(input("Enter the phno:"))
#         sub_dict['phno']=ph
#         em=input("Enter the email:")
#         sub_dict['email']=em
#         main_dict[na]=sub_dict
#         print("Added successsfulllyyyyy.....")
#     elif choice ==2:
#         ch=int(input("1.view all contact\n2.View single contact\nEnter your choice:"))
#         if ch==1:
#             print(main_dict)
#         elif ch==2:
#             x=input("Enter the contact you have to view")
#             if x in main_dict:
#                 print(main_dict[x])
#             else:
#                 print("contact does not exist")
#         else:
#             print("Invalid choice")
#     elif choice==3:
#         y=input("Enter the contact you have to update:")
#         if y in main_dict:
#             print(main_dict[y])
#             ch=int(input("1.update name\n2.update phno\n3.update email\nEnter your choice:"))
#             if ch==1:
#                 new_name=input("enter the new name:")
#                 main_dict[y]['name']=new_name
#                 sub=main_dict.pop(y)
#                 main_dict[new_name]=sub
#                 print(main_dict[new_name])
#             elif ch==2:
#                 new_ph=int(input("Enter the new phno:"))
#                 main_dict[y]['phno']=new_ph
#                 print(main_dict[y])
#             elif ch==3:
#                 new_em=input("Enter the new email:")
#                 main_dict[y]['email']=new_em
#                 print(main_dict[y])
#             else:
#                 print("invalid choice")
#         else:
#             print("contact not exist")
#     elif choice==4:
#         z=input("Enter the contact you have to delete:")
#         if z in main_dict:
#             print(main_dict[z])
#             ch=int(input("1.dlt name\n2.dlt phno\n3.dlt email\nEnter your choice:"))
#             if ch==1:
#                 del main_dict[z] 
#                 print(main_dict)
#             elif ch==2:
#                 del main_dict[z]['phno']
#                 print(main_dict[z])
#             elif choice==3:
#                 del main_dict[z]['email']
#                 print(main_dict[z])
    #         else:
    #             print("invalid choice")
    #     else:
    #         print("contact does not exist")
    # elif choice==5:
    #     break
    # else:
    #     print("Invalid choice")



# /////////////////////////////////////////////////////////////////////////////


main_dict={}
while True:
    choice=int(input("1.Add contact\n2.View contact\n3.Update contact\n4.Delete contact\n5.Exit\nEnter your choice:"))
    if choice==1:
        sub_dict={}
        na=input("Enter the name")
        sub_dict['name']=na
        ph_list=[]
        x=int(input("how many phone number you have to add"))
        for i in range(x):
            ph=int(input("Enter the phone numbers"))
            ph_list.append(ph)
        sub_dict['phone']=ph_list
        email_list=[]
        x=int(input("Enter how many email you have to add"))
        for i in range(x):
            email=input("Enter the emails")
            email_list.append(email)
        sub_dict['email']=email_list
        main_dict[na]=sub_dict
        print("Added successfullyyy....")
    elif choice==2:
        ch=int(input("1.view all contact\n2.view one contact\nEnter your choice"))
        if ch==1:
            print(main_dict)
        elif ch==2:
            x=input("Enter the contact you have to view")
            if x in main_dict:
                print(main_dict(x))
            else:
                print("contact does not exist")
        else:
            print("Invalid choice")
    elif choice==3:
        y=input("Enter the contact you have to update")
        if y in main_dict:
            print(main_dict[y])
            ch=int(input("1.update name\n2.update phno\n3.update email\nEnter your choice:"))
            if ch==1:
                new_name=input("Enter the new name")
                main_dict[y]['name']=new_name
                z=main_dict.pop(y)
                main_dict[new_name]=z
                print(main_dict[new_name])
            elif ch==2:
                print(main_dict[y]['phone'])
                pos=int(input("enter the nmber you have to delete:"))
                pos-=1
                new_num=int(input("enter the new nummber:"))
                main_dict[y]['phone'][pos]=new_num
                print(main_dict[y]['phone'])
            elif ch==3:
                print(main_dict[y]['email'])
                pos=int(input("Enter the email you have to update"))
                pos-=1
                new_email=input("Enter the new email")
                main_dict[y]['email'][pos]=new_email
                print(main_dict[y]['email'])
            else:
                print("Invalid choice")
        else:
            print("Contact doesnot exist")
    elif choice==4:
        y=input("Enter the contact you have to delete:")
        if y in main_dict:
            print(main_dict[y])
            ch=int(input("1.delete name\n2.delete phno\n3.delete email\nEnter your choice"))
            if ch==1:
                del main_dict[y]
            elif ch==2:
                print(main_dict[y]['phone'])
                z=int(input("enter the number you have to delete"))
                z-=1
                del main_dict[y]['phone'][z]
                print(main_dict[y])
            elif ch==3:
                print(main_dict[y]['email'])
                z=int(input("Enter the email you have to del"))
                z-=1
                del main_dict[y]['email'][z]
                print(main_dict[y])
            else:
                print("Invalid choice")
        else:
            print("Contact does note exist")
    elif choice==5:
        break
    else:
        print("invalid choice")

                       
