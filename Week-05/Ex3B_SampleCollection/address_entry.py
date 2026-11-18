#Stephanie Y. Lopez Chavoya

contact_info = {"name": "Stephanie Chavoya",
                "address": "3028 James street",
                "city": "Seattle",
                "state": "Washington",
                "zip": "26767"}

print(f"""{contact_info['name']}{contact_info['address']} {contact_info['city']} {contact_info['state']}{contact_info['zip']}""")

#using delete
del contact_info["name"]

#full name
full_name = {
    "first name": "Stephanie",
    "last name": "Chavoya"
}

#honorific
full_name.update({"honorific": "Ms."})

#updating info
contact_info.update({"full_name": full_name})

#updated format for address
print(f"""{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")