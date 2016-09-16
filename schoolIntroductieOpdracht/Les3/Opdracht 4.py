def contain_num(s):
    return any(i.isdigit() for i in s)

def new_password(oldpassword, newpassword):
    if len(newpassword) >= 6 and str(newpassword) != str(oldpassword) and contain_num(newpassword):
        print("True");
    else:
        print("False");

a = input("Oud wachtwoord: ");
b = input("Nieuw wachtwoord: ");

new_password(a,b);