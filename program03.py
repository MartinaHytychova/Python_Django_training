available_rooms = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

time = int(input("V kolik hodin si chcete zarezervovat meetingovou místnost?"))

for key, value in available_rooms.items():
    if time in available_rooms.keys():
        print(len(available_rooms[time]))
        break
