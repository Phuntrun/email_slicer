def emailinput():
    email=str(input("nhap email cua ban:"));
    return email;
def emailprocess(email):
    email_username = email[0:email.index('@')];
    email_domain = email[email.index('@')+1:];
    return [email_username,email_domain];
def emailoutput(email_username, email_domain):
    print("usename:",email_username);
    print("domain:",email_domain);


def main():
    email = emailinput();
    [email_username, email_domain]=emailprocess(email);
    emailoutput(email_username, email_domain);



if (__name__ == "__main__") :
    main()