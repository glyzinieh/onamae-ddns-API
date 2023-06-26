from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, RedirectResponse

from client import OnamaeDDNSError, update_domain_ip

app = FastAPI()


@app.get("/")
def root():
    return RedirectResponse("/docs")


@app.get("/update/")
def update(userid: str, password: str, hostname: str, domname: str, ip: str):
    env = {
        "USERID": userid,
        "PASSWORD": password,
        "HOSTNAME": hostname,
        "DOMNAME": domname,
    }
    try:
        update_domain_ip(env, ip)
    except OnamaeDDNSError as e:
        if str(e) == "Failed to login: 002 LOGIN ERROR":
            status_code = status.HTTP_401_UNAUTHORIZED
        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse({"message": str(e)}, status_code=status_code)
    except Exception:
        return JSONResponse(
            {"message": "An unexpected error has occurred"},
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    else:
        return JSONResponse({"message": "Successfull"}, status_code=status.HTTP_200_OK)
