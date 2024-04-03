import requests
import json
from frappe.utils import validate_url, validate_email_address, validate_phone_number


def ntfy(site:str="https://ntfy.sh/", topic:str="", message:str="", title:str="", tags:list=[], priority:int=3, actions:list=[], click:str="", attach:str="", markdown:bool=True, icon:str="", filename:str="", delay:str="", email:str="", call:str=""):
    
    # Validation checks
    validate_url(site, throw=True)
    if click:
        validate_url(click, throw=True)
    if attach:
        validate_url(attach, throw=True)
    if email:
        validate_email_address(email, throw=True)
    if call:
        validate_phone_number(call, throw=True)
    
    
    # JSON payload
    response = requests.post(site,
        data=json.dumps({
            "topic": topic,
            "message": message,
            "title": title,
            "tags": tags,
            "priority": priority,
            "actions": actions,
            "click": click,
            "attach": attach,
            "markdown": markdown,
            "icon": icon,
            "filename": filename,
            "delay": delay,
            "email": email,
            "call": call
        })
    )
    
    return response
    
    
    
    
