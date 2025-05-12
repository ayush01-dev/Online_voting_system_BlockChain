from pydantic import BaseModel

class Token(BaseModel):
    token: str

class Vote(BaseModel):
    userId: str
    orgCode: int

def takeOrgDetails() -> "tuple":
    details: "dict[str, str]" = {}
    orgNames: "list[str]" = []
    leaders: "list[str]" = []
    codes: "list[str]" = []
    while (True):
        orgDetail = input("Register Organisation: [Organisation:Leader:Code], ['q' -> exit] : ")
        if orgDetail == "q":
            break
        elif len(orgDetail.split(":")) > 3:
            print("Enter valid details")
        else:
            orgName, leader, code = orgDetail.split(":")
            details[code] = orgName
            orgNames.append(orgName)
            leaders.append(leader)
            codes.append(code)
    return (details, orgNames, leaders, codes)