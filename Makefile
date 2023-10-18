run_api:
	uvicorn api.fast:app --reload

run_train:
	python -c 'from interface.main import main_train; main_train()'
