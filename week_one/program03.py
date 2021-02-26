available_rooms = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

time = int(input("V kolik hodin si chcete zarezervovat meetingovou místnost?"))

if time in available_rooms:
    print(len(available_rooms[time]))
