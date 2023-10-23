run_api:
	uvicorn api.fast:app --reload

run_train:
	python -c 'from interface.main import main_train; main_train()'

reinstall_package:
	@pip uninstall -y what-is-that-fruit-back || :
	@pip install -e .
