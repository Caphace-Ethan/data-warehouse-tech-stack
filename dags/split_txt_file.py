from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import time

import pandas as pd
import contextlib
data_path = './data/I80_davis.txt'
csv_path = './dbt/data/batch_'
txt_path = "./data/batch_"
_new_file = './data/batch'

# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join('./scripts')))
# from scripts.prepare_txt_data import split_text, cloud_get_text_corpus_to_csv


def _create_small_txt_files():
	l = 3 * 10 ** 6  # lines per split file
	with contextlib.ExitStack() as stack:
		try:
			fd_in = stack.enter_context(open(data_path))
			for i, line in enumerate(fd_in):
				print(f" Progress: {round((i * 100) / l, 2)} %")
				if not i % l:
					file_split = '{}_{}.txt'.format(_new_file, i // l)
					fd_out = stack.enter_context(open(file_split, 'w'))
				fd_out.write('{}\n'.format(line))
			loggs = "Reading large txt file successfully,  Splitting file to small files successfully"
		except Exception as e:
			loggs = "Read txt file Un-successfully, error: " + e
	return loggs
	# split_text()
	# return "Process Completed"


def _create_batches_csv_files(i):
	with open(txt_path + i + ".txt") as f:
		contents = f.readlines()
		list_data = []
		n = 0
		for line in contents:
			list_text = {}
			list_text["sentence"] = line
			list_data.append(list_text)
			print(f" Progress: {round((n * 100) / len(contents), 2)} %")
			n += 1
		f.close()

		try:
			df = pd.DataFrame.from_dict(list_data)
			df['id'] = df.index
			df.to_csv(csv_path + i + '.csv', index=False)
			e = "CSV Created"
		except Exception as e:
			print(e)

	return e
	# cloud_get_text_corpus_to_csv()
	# return "Process Completed"


with DAG("split_txt_file", start_date=datetime(2021, 9, 21),
		 schedule_interval="@daily", catchup=False) as dag:

	splitting_large_txt_file = PythonOperator(
		task_id="creating_small_txt",
		python_callable=_create_small_txt_files
	)

	creating_csv_from_txt = PythonOperator(
		task_id="creating_csv_from_txt",
		python_callable=_create_batches_csv_files
	)

	splitting_large_txt_file >> creating_csv_from_txt
