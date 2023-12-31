run_main:
	uvicorn Backend.FastAPI.main:app --reload

run_users:
	uvicorn Backend.FastAPI.users:app --reload
