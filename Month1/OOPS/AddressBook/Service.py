import json
from re import search


class Service:
    def __init__(self):
        self.person_data = []
        self.file_name = None

    def create(self):
        try:
            file_name = input("Enter file name for creating new json file : ").strip()
            if search("[a-zA-Z]", file_name) != None:
                f = open(file_name + ".json", 'w+')
                f.closed
            else:
                raise ValueError
        except ValueError:
            print("File name should be alphabet only")

    def open(self):
        file_name = input("Enter file name :  ").strip().lower()
        try:
            with open(file_name + ".json") as data:
                self.person_data = json.load(data)
                self.file_name = file_name
                data.closed
        except Exception:
            print("File not found.")

    def save(self):
        try:
            with open(self.file_name + ".json") as data:
                json.dump(self.person_data, data)
                data.closed
        except Exception:
            print("You have not yet open any file. ")



    def save_as(self):
        file_name = input("Enter file name with extension json or txt : ").strip()
        json_patt = search("\.json", file_name)
        txt_patt = search("\.txt", file_name)
        print(json_patt)
        if json_patt is not None and json_patt.group() == ".json":
            select = 1
        elif txt_patt is not None and txt_patt.group() == ".txt":
            select = 2
        else:
            print("You enter wrong file extension.")
            return

        with open(file_name, 'w+') as data:
            if select == 1:
                json.dump(self.person_data, data)
            elif select == 2:
                data.write(str(self.person_data))

    def add_person(self):
        first_name = input("Enter first name : ").strip().upper()
        last_name = input("Enter last name : ").strip().upper()
        address = input("Enter address : ").strip().upper()
        city = input("Enter city : ").strip().upper()
        state = input("Enter state : ").strip().upper()
        zip_code = input("Enter zip code : ").strip()
        phone_number = input("Enter phone number : ").strip()
        new_person = {"data": {}}

        new_person["data"]["address"] = address
        new_person["data"]["city"] = city
        new_person["data"]["state"] = state
        new_person["data"]["zip_code"] = zip_code
        new_person["data"]["phone_number"] = phone_number
        new_person["first_name"] = first_name
        new_person["last_name"] = last_name
        flag = True
        for i in self.person_data:
            if i["first_name"] == first_name and i["last_name"] == last_name:
                print("Duplicate data.")
                flag = False
                break
        if flag:
            self.person_data.append(new_person)
        print(self.person_data)

    def delete_person(self):
        first_name = input("Enter first name : ").strip().upper()
        last_name = input("Enter last name : ").strip().upper()

        for i in range(len(self.person_data)):
            if self.person_data[i]["first_name"] == first_name and self.person_data[i]["last_name"] == last_name:
                self.person_data.remove(self.person_data[i])
                print("Data deleted.")
                break

    def edit_person(self):
        print("Enter data for editing")
        first_name = input("Enter first name : ").strip().upper()
        last_name = input("Enter last name : ").strip().upper()
        flag = True
        for i in range(len(self.person_data)):
            if self.person_data[i]["first_name"] == first_name and self.person_data[i]["last_name"] == last_name:
                flag = False
                while True:
                    choice = int(input(
                        "\t1.First Name\n\t2.Last Name\n\t3.Addresss\n\t4.City\n\t5.State\n\t6.Zip Code\n\t7.Mobile Number\n\t8.Nothing want to change\n\tSelect choice : "))
                    if choice == 1:
                        first = input("Enter first name : ").strip().upper()
                        self.person_data[i]["first_name"] = first
                    elif choice == 2:
                        last = input("Enter last name : ").strip().upper()
                        self.person_data[i]["last_name"] = last
                    elif choice == 3:
                        addr = input("Enter address : ").strip().upper()
                        self.person_data[i]["data"]["address"] = addr
                    elif choice == 4:
                        city = input("Enter city : ").strip().upper()
                        self.person_data[i]["data"]["city"] = city
                    elif choice == 5:
                        state = input("Enter state : ").strip().upper()
                        self.person_data[i]["data"]["state"] = state
                    elif choice == 6:
                        zip_code = input("Enter zip code : ").strip()
                        self.person_data[i]["data"]["zip_code"] = zip_code
                    elif choice == 7:
                        phone_number = input("Enter phone number : ").strip()
                        self.person_data[i]["data"]["phone_number"] = phone_number
                    elif choice == 8:
                        return
                    else:
                        print("You selected wrong choice.")
        if flag:
            print("Data not available.")


if __name__ == "__main__":
    s = Service()
    s.open()
    s.edit_person()
    s.save()
