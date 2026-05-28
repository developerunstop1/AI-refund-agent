from fastapi import APIRouter

router = APIRouter()

@router.get("/logs")
def get_logs():
    return {
        "logs": [
            "Customer verified",
            "Policy checked",
            "Refund decision generated"
        ]
    }