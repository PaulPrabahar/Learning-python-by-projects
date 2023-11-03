# collect email from user
# split the email using @, the first part as the user name, the second part as a domain name
# split dmain using .

def name_domainname_domain_slicer(email):
    (username, domain) = email.split("@")
    (domain_name, domain_value) = domain.split(".")
    return username, domain_name, domain_value


email_input = input("Enter your email: ")

username, domain_name, domain_value = name_domainname_domain_slicer(
    email_input)

print("Username: ", username)
print("Domainname: ", domain_name)
print("Domain: ", domain_value)

print("")
