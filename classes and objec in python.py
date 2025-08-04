# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def display_brand(self):
#         print("The car brand is", self.brand)

# my_car = Car(str(input("Enter the car brand: ")))
# my_car.display_brand()

# # -------------------------------------------------------------
# # Car with Features
# class CarFeature:
#     def __init__(self, brand, features):
#         self.brand = brand # Store car brand
#         self.features = features # Store list of features

    
# # Method to display brand of the car
#     def display_brand(self):
#         print("The car brand is", self.brand)


# # Method to display features of the car
#     def display_feature(self):
#         if len(self.features) <= 0:
#             print("No features available for this car ")
#         else:
#             print("Features: ")
#             for feature in self.features: # Loop through the list and print each feature
#                 print("-", feature)    


# # Input Section

# brand = input("Enter the car brand: ")

# # ASk user how many features they want to add

# num = int(input("How many features do you want to add? "))
# features = [] # Initialize an empty list to store features

# # if user wants to add features
# if  num > 0:
#     for i in range(num):
#         feat = input(f"Enter feature {i+1}: ") # Take input one by one 
#         features.append(feat) # Add to list


# my_car = CarFeature(brand, features) # Create an instance of CarFeature
# my_car.display_brand()
# my_car.display_feature()

# # -------------------------------------------------------------







