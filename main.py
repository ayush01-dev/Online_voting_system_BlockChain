from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from blockchainfolder.chain import Chain
import user_data
from fastapi import FastAPI, Request, Depends, Form, Cookie, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
import os
import utils
import sys
import uvicorn
from starlette.middleware.sessions import SessionMiddleware
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables
# Use os.path.join for file paths
config_dir = os.path.join(os.path.dirname(__file__), "config")

os.makedirs(config_dir,exist_ok=True)






def load_organizations_from_file():
    try:
        # Check if file exists, create if not
        if not os.path.exists("config/organizations.txt"):
            os.makedirs("config", exist_ok=True)
            with open("config/organizations.txt", "w") as f:
                pass
            return {}, [], [], []

        details = {}
        orgNames = []
        leaders = []
        codes = []

        with open("config/organizations.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line and ":" in line:
                    parts = line.split(":")
                    if len(parts) >= 3:
                        orgName, leader, code = parts[0], parts[1], parts[2]
                        details[code] = orgName
                        orgNames.append(orgName)
                        leaders.append(leader)
                        codes.append(code)

        return details, orgNames, leaders, codes
    except Exception as e:
        print(f"Error loading organizations: {e}")
        return {}, [], [], []


def save_organizations_to_file():
    try:
        os.makedirs("config", exist_ok=True)
        with open("config/organizations.txt", "w") as f:
            for i in range(len(orgNames)):
                f.write(f"{orgNames[i]}:{leaderNames[i]}:{orgCodes[i]}\n")
        return True
    except Exception as e:
        print(f"Error saving organizations: {e}")
        return False



# Load token from file or environment, create if doesn't exist
if os.path.exists("config/token.txt"):
    with open("config/token.txt", "r") as f:
        token = f.read().strip()
else:
    # Create a random token if not exists
    import secrets
    token = secrets.token_hex(16)
    os.makedirs("config", exist_ok=True)
    with open("config/token.txt", "w") as f:
        f.write(token)
print(f"Admin token: {token}")  # Display once at startup

# Load organizations from file
orgDetails, orgNames, leaderNames, orgCodes = load_organizations_from_file()
print(f"Loaded {len(orgDetails)} organizations")

if len(orgDetails.keys()) < 2:
    print("At least two organisation shoudl be registered")
    sys.exit(1)

chain = Chain(10)
userData = user_data.get_user_data()
# print(userData)
orgVoteCount: "dict[str, list[str]]" = {}
castedVoters : "list[str]" = []
print("Voting system is ready")

controller = {
    "isStarted": False,
    "isStoped": False
}


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="dc53923487140dd1b4ba4d3da9d09411")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def showHome(request: Request):
    return templates.TemplateResponse(
        "item.html", {
            "request": request
        }
    )

@app.get("/confirmation", response_class=HTMLResponse)
def showConfirmation(request: Request):
    return templates.TemplateResponse(
        "confirm.html", {
            "request": request
        }
    )

@app.get("/getOrgDetail")
def getOrgDetail():
    return {
        "orgNames": orgNames,
        "leaderNames": leaderNames,
        "orgCodes": orgCodes,
    }

@app.post("/admin/start")
def startVoting(item: utils.Token):
    if (item.token == token):
        controller["isStarted"] = True
        print("System is running: Voter can cast there vote")
        return {
            "status": "started"
        }

@app.post("/admin/stop")
def stopVoting(item: utils.Token):
    if item.token == token:
        controller["isStoped"] = True
        print("System is stoped")
        return {
            "status": "stoped"
        }

@app.post("/voter/vote")
async def CastVote(request: Request):
    formData = await request.form()
    formDict = formData._dict
    print(formData)
    print("Reached")
    print(formDict["userId"])
    print(userData.keys())
    if controller["isStarted"]:
        if formDict["userId"] in userData.keys():
            if formDict["password"] == userData[formDict["userId"]]:
                if formDict["userId"] not in castedVoters:
                    try:
                        orgName = orgDetails[formDict["orgCode"]]
                        chain.add_to_pool(orgName)
                        hash: str = chain.mine()
                        try:
                            votes = orgVoteCount[orgName]
                            votes.append(hash)
                            orgVoteCount[orgName] = votes
                        except KeyError:
                            orgVoteCount[orgName] = [hash]
                        castedVoters.append(formDict["userId"])
                        return templates.TemplateResponse(
                            "confirm.html", {
                                "request": request,
                                "status": "successfull",
                                "organisation": orgName,
                                "description": "Hash -> " + hash
                            }
                        )
                    except KeyError:
                        return templates.TemplateResponse(
                            "confirm.html", {
                                "request": request,
                                "status": "unsuccessful",
                                "description": "Invalid Organisation Details"
                            }
                        )
                else:
                    return templates.TemplateResponse(
                        "confirm.html", {
                            "request": request,
                            "status": "unsuccessful",
                            "description": "you have already casted your vote"
                        }
                    )
            else:
                return templates.TemplateResponse(
                    "confirm.html", {
                        "request": request,
                        "status": "unsuccessful",
                        "description": "wrong password"
                    }
                )
        else:
            return templates.TemplateResponse(
                "confirm.html", {
                    "request": request,
                    "status": "unsuccessful",
                    "description": "Unregistered user"
                }
            )
    else:
        return templates.TemplateResponse(
                    "confirm.html", {
                        "request": request,
                        "status": "unsuccessful",
                        "description": "Voting is closed or it is not started"
                    }
                )


@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    is_authenticated = request.session.get("admin_authenticated", False)
    if not is_authenticated:
        return templates.TemplateResponse("admin_login.html", {"request": request})

    # Convert zip to list before passing to template
    orgs_list = list(zip(orgNames, leaderNames, orgCodes))

    return templates.TemplateResponse(
        "admin_panel.html", {
            "request": request,
            "organizations": orgs_list,  # Now a list instead of zip iterator
            "voting_status": "Running" if controller["isStarted"] else "Not Started",
            "voting_ended": controller["isStoped"]
        }
    )

@app.post("/admin/login")
async def admin_login(request: Request):
    form = await request.form()
    if form.get("token") == token:
        request.session["admin_authenticated"] = True
        return RedirectResponse("/admin", status_code=303)
    return templates.TemplateResponse(
        "admin_login.html",
        {"request": request, "error": "Invalid token"}
    )


@app.post("/admin/add_organization")
async def add_organization(request: Request):
    if not request.session.get("admin_authenticated", False):
        return JSONResponse({"error": "Not authenticated"})

    form = await request.form()
    org_name = form.get("org_name")
    leader_name = form.get("leader_name")
    org_code = form.get("org_code")

    if not org_name or not leader_name or not org_code:
        return JSONResponse({"error": "All fields are required"})

    if org_code in orgDetails:
        return JSONResponse({"error": "Organization code already exists"})

    orgDetails[org_code] = org_name
    orgNames.append(org_name)
    leaderNames.append(leader_name)
    orgCodes.append(org_code)

    # Save to file
    save_organizations_to_file()

    return JSONResponse({"success": True})
@app.get("/getvotes")
def getTotalVotes():
    if not controller["isStoped"]:
        return {
            "total_votes": 0,
            "status": "Voting is currently running"
        }
    return {
        "total_votes" : len(chain.blocks)-1,
        "status": "voting has been stoped"
    }


@app.post("/admin/delete_organization")
async def delete_organization(request: Request):
    # Check authentication
    if not request.session.get("admin_authenticated", False):
        return JSONResponse({"error": "Not authenticated"})

    # Get request data
    data = await request.json()
    org_code = data.get("org_code")
    admin_token = data.get("token")

    # Validate token
    if admin_token != token:
        return JSONResponse({"error": "Invalid admin token"})

    # Check if organization exists
    if org_code not in orgDetails:
        return JSONResponse({"error": "Organization not found"})

    # Find index of the organization
    try:
        index = orgCodes.index(org_code)

        # Remove from all lists
        del orgDetails[org_code]
        del orgNames[index]
        del leaderNames[index]
        del orgCodes[index]

        # Save changes to file
        save_organizations_to_file()

        return JSONResponse({"success": True})
    except ValueError:
        return JSONResponse({"error": "Error finding organization"})
    except Exception as e:
        return JSONResponse({"error": f"Error deleting organization: {str(e)}"})


@app.get("/getvotesbyorg")
def getVotesByOrg():
    if not controller["isStoped"]:
        return {
            "status": "Voting is currently running"
        }
    result = {}
    for i in range(len(orgVoteCount.keys())):
        org = list(orgVoteCount.keys())[i]
        count = len(list(orgVoteCount.values())[i])
        result[org] = count
    return result



if __name__ == "__main__":
    uvicorn.run(app)

