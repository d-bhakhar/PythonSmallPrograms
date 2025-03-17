def generate_resume(name, email, phone, skills, experience):
    # Define the structure of the resume
    resume = f"""
    --------------- Resume ---------------
    Name: {name}
    Email: {email}
    Phone: {phone}
    
    Skills:
    - {skills}
    
    Experience:
    {experience}
    --------------------------------------
    """
    return resume

def main():
    # Gather user input
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    skills = input("Enter your skills (comma separated): ").split(',')
    experience = input("Enter your experience: ")

    # Generate the resume
    resume = generate_resume(name, email, phone, skills, experience)

    # Print the resume
    print(resume)

if __name__ == "__main__":
    main()
