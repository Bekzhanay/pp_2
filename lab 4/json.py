import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("sample-data.json", "r") as js_file:
    j = json.load(js_file)
for x in j["imdata"]:
    print(f"{x["l1PhysIf"]["attributes"]["dn"]}                              {x["l1PhysIf"]["attributes"]["speed"]}   {x["l1PhysIf"]["attributes"]["mtu"]}")