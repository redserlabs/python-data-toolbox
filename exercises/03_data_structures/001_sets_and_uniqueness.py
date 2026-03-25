ticket_segments = [
    "vip",
    "individual",
    "subscriber",
    "vip",
    "partner",
    "individual",
    "vip"
]

unique_segments = set(ticket_segments)

print("SETS AND UNIQUENESS")
print("-------------------")
print(f"Original segments: {ticket_segments}")
print(f"Unique segments: {unique_segments}")
print(f"Number of unique segments: {len(unique_segments)}")