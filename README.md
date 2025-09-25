# Tasks

This branch contains solutions of some basic tasks from the PLM course

## Task 1: Feature variance analysis

In this task, I had to compute variance over each column in a dataset using pandas.  
And then print the three highest results.

### Run the program

* __Use default parameters__

```bash
python task_1.py
```

* __Use custom parameters__

```bash
python task_1.py --read_csv_kwargs '{"param_1": value_1, "param_2": value_2, "param_3": "str_1" ...}'
```

After __--read_csv_kwargs__ you need to print a python dictionary object between ' ' like in the example above.  
Indeed this string is just converted to the dict type via __json.loads__ function.
