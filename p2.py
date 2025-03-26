hotel_room=1000
tax=hotel_room*0.18
total=hotel_room+tax
service1=1500
service2=2000
service3=750
service4=1250
total_service=service1+service2+service3+service4
grand_total=total+total_service
per_person_cost=grand_total/4
print("per person cost of stay in our hotel is:"+str(per_person_cost))
