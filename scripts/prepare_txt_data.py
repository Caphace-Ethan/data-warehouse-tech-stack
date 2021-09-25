import math
import pandas as pd
import contextlib
data_path = './data/I80_davis.txt'
csv_path = './data/batch_'
csv_path1 = './dbt/data/sensors_data.csv'
txt_path = "./data/batch_"
_new_file = './data/batch'


def split_text():
	l = 3 * 10 ** 6  # lines per split file
	with contextlib.ExitStack() as stack:
		try:
			fd_in = stack.enter_context(open(data_path))
			for i, line in enumerate(fd_in):
				print(f" Progress: {round((i*100)/l,2)} %")
				if not i % l:
					file_split = '{}_{}.txt'.format(_new_file, i // l)
					fd_out = stack.enter_context(open(file_split, 'w'))
				fd_out.write('{}\n'.format(line))
			loggs = "Reading large txt file successfully,  Splitting file to small files successfully"
		except Exception as e:
			loggs = "Read txt file Un-successfully, error: "+ e

	return loggs


def _get_text_corpus_to_csv(ii):

	csv_file = pd.read_csv(txt_path+str(ii)+".txt", header=None)
	# csv_file.columns = ['utc_time_id', 'source_ref', 'source_id',]

	# sed	1d batch_ *.csv > ../dbt/data/all_sensor_data.csv

	return csv_file


if __name__ == "__main__":

	if (True):
		for i in range(12):
			print(f" Progress: {round((i * 100) / 12, 2)} % ...")
			returned_list = _get_text_corpus_to_csv(i)
			try:
				returned_list.to_csv(csv_path+str(i)+'.csv', index=False)

				e = "CSV Created"
			except Exception as e:
				print(e)
			print(e)

	if (False):
		split_text()

