# Existing list of registered students
registered_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]

# New registrations
new_registrations = ["Katie", "Liam", "Mia", "Nina", "Oscar"]

# Add new registrations to the existing list
registered_students.extend(new_registrations)

# Create a sublist of the first 10 students for the workshop
workshop_invites = registered_students[:10]

# Print the results
print("Updated List of Registered Students:", registered_students)
print("Workshop Invitations (First 10 Students):", workshop_invites)