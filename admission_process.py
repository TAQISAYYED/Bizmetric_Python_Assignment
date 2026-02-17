# class YesError(Exception):
#     pass

# def Total_cost():
    
    
#     try:
#         L1 = ['HR', 'Finance', 'Marketing', 'DS']
#         print[print(L1)]
#         stream = input("Enter your stream: ").upper()
#         analytics = input("Enter analytics (Y/N): ").upper()
#         hostel = input("Enter hostel (Y/N): ").upper()
#         food_months = input("Enter food months in digit : ")
#         transport = input("Enter transport (semester/annual): ").lower()
     
#         total_cost = 0

#         if stream not in L1:
#             return "Wrong Stream Chosen"

#         course_fee = 200000

#         if analytics not in ['Y', 'N']:
#             raise YesError("Enter proper choice")
#         elif stream != 'DS' and analytics == 'Y':
#             total_cost += course_fee * 1.10
#         else:
#             total_cost += course_fee

#         if hostel == 'Y':
#             total_cost += 200000
#         elif hostel != 'N':
#             return "Wrong Hostel Chosen"

#         if food_months.isdigit() and int(food_months) > 0:
#             total_cost += int(food_months) * 2000
#         else:
#             return "Wrong Food_month Chosen"

#         if transport == 'semester':
#             total_cost += 13000
#         elif transport == 'annual':
#             total_cost += 26000
#         else:
#             return "Wrong Transportation Chosen"

#         return total_cost

#     except ValueError:
#         print("food_months expects int input")
#     except YesError as e:
#         print(e)
#     except Exception:
#         print("Something went wrong")
#     finally:
#         print("All code executed")

# result = Total_cost()
# print(result)


# ----------------------
class AdmissionProcess:
    course_fee = 200000

    def __init__(self):
        self.total = AdmissionProcess.course_fee
        self.stream = input("Enter Stream: ").upper()
        self.analytics = input("Analytics (Y/N): ").upper()
        self.hostel = input("Hostel Required (Y/N): ").upper()
        self.food = int(input("Food Months: "))
        self.transport = input("Transport (semester/annual): ").lower()


    def analytics_cost(self):
        if self.stream != 'DS' and self.analytics == 'Y':
            return 20000
        return 0

    def hostel_cost(self):
        if self.hostel == 'Y':
            return 200000
        return 0

    def food_cost(self):
        return self.food * 2000


    def transport_cost(self):
        if self.transport == 'semester':
            return 13000
        elif self.transport == 'annual':
            return 26000
        return 0

    def total_cost(self):
        total = self.total
        total += self.analytics_cost()
        total += self.hostel_cost()
        total += self.food_cost()
        total += self.transport_cost()
        return total

obj = AdmissionProcess()
print("Total Cost =", obj.total_cost())
