from extract_tests_data import run_extract_test_data
from pathlib import Path

result_path = f'/home/wanderson/Documentos/tcc/tool/data_generated/experiment-date-02-05-25-time-20-45-33-904'

folder = Path(f'{result_path}/repetition_0/SMARTS/generated_tests')
filtered_files = [
    file.name for file in folder.iterdir()
    if file.is_file() and file.name.startswith("EvoMaster") and file.name.endswith("Test.py")
]
            
run_extract_test_data(Path(f'{result_path}/repetition_0/SMARTS'), filtered_files, result_path)