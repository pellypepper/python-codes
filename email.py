"""
creating a email stimulator that allows the user to read,
 view unread and 
 quit the email
"""

class Email:
 
    inbox = []

    def __init__ (self, email_address, subject_line, email_content) :
        """
        this is the constructor of the class Email
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        self.inbox = []


    def mark_as_read(self):
        """
        this instance method mark the email as read by setting the
        """
        self.has_been_read = True
    
    
    def populate_inbox(self):
      """
      this instannce method create a dictionary of the email 
      and append it to the inbox list
      """
      email_store = {
         "email_address": self.email_address,
         "subject_line": self.subject_line,
         "email_content": self.email_content,
        "has_been_read": self.has_been_read
      }
      Email.inbox.append(email_store)

       
    @classmethod
    def list_emails(cls):
     """
     this class method list all the emails in the inbox 
     list by displaying the subject line only
      """
     for i, email in enumerate(cls.inbox, start=1):
            status = "(Unread)" if not email["has_been_read"] else "(Read)"
            print(f"{i} - {email['subject_line']} {status}")


    @classmethod
    def view_unread_emails(cls):
        """
          this class method list all the unread emails in the inbox
          by checking the has_been_read key in the dictionary
        """
        unread_emails = [email for email in cls.inbox if not email["has_been_read"]]
        if not unread_emails:
            print("No unread emails.")
        else:
            for i, email in enumerate(unread_emails, start=1):
                print(f"{i} - {email['subject_line']} (From: {email['email_address']})")


    @classmethod
    def read_email(cls, box):
            """
            this class method read the email idnex inputted by user and   display the email address, 
            subject line and email content
            """
            
            email = cls.inbox[box - 1]
            print(f"From: {email['email_address']}")
            print(f"Subject: {email['subject_line']}")
            print(f"Content: {email['email_content']}")
            email["has_been_read"] = True

        
   
def main ():
        # create an instance of the Email class
        check_email = Email("ppe@gmail.com", "Welcome to HyperionDev!", "fjjdjdcjkvdvkd")
        check_email1 = Email("aae@gmail.com", "Great work on the bootcamp!", "fjjdjdcjkvdvkd")
        check_email2 = Email("bbe@gmail.com", "Your excellent marks!", "fjjdjdcjkvdvkd")
        check_email.populate_inbox()
        check_email1.populate_inbox()
        check_email2.populate_inbox()


        while True:
            print("Welcome to your inbox!")
            print("1. Read your email")
            print("2. view unread emai")
            print("3. Quit email")
            option1 = int(input("Choose an Option: "))
   
            # check the option selected by the user and call the appropriate method
            if option1 == 1:
                Email.list_emails()
                box = int(input("Enter the number of the email you want to read: "))
                Email.read_email(box)
            elif option1 == 2:
                Email.view_unread_emails()
            elif option1 == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
                option1 = int(input("Enter the number of the option you want to select: "))

# call the main function
if __name__ == "__main__":
    main()