"""
Functions Deep Dive - *args and **kwargs

CONCEPTS:
- *args: Accept any number of positional arguments
- **kwargs: Accept any number of keyword arguments
- Both together: Maximum flexibility

REAL-WORLD USE:
- print() uses *args (any number of things to print)
- requests.get() uses **kwargs (any number of options)
- Web frameworks use both extensively
"""

def sum_numbers(*args):
    """Add any number of numbers together"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(5))
print(sum_numbers(5, 10))
print(sum_numbers(5, 10, 15, 20))

def create_profile(**kwargs):
    """Create a user profile with any attributes"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user1 = create_profile(name="Darshan", age=15)
user2 = create_profile(name="Darshan", age=15, email="123@gmail.com", city="Banglore")

print(user1)
print(user2)

def flexible_function(*args, **kwargs):
    """Accept both positional and keyword arguments"""
    print("Arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

flexible_function(1, 2, 3, name="Darshan", age=15)

"""
class Math:
    @staticmethod
    def add(*args):
        total = 0
        for num in args:
            total += num
        return total
    
print(Math.add(5))
print(Math.add(5,5))
print(Math.add(5,5,5))

class Profile:
    @staticmethod
    def create_profile(**kwargs):
        Profile = {}
        for key, value in kwargs.items():
            Profile[key]=value
        return Profile
    
user1 = Profile.create_profile(name = "Darshan", age = 15)
user2 = Profile.create_profile(name = "Darshan", age = 15, DOB = "01-01-2000")

print(user1)
print(user2)

class function:
    @staticmethod
    def flexible_function(*args, **kwargs):
        print("Arguments (*args):", args)
        print("Keyword arguments (**kwargs):", kwargs)


function.flexible_function(1, 2, 3, name="John", age=25)
"""