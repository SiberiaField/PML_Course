# DA-2-31: Difference between covariation and correlation

In this task, I had to compute covariation over a dataset, draw heatmaps for covariation and correlation,  
then explain the difference between them.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the program

* __Use default parameters__

```bash
python da_2_31.py
```

__Note__: Running with default parameters is not very useful,  
because program just downloads dataset and do caclulations but it doesn't save or show anything.

* __Print help message__

```bash
python da_2_31.py [-h, --help]
```

* __Parameters for reading dataset__

```bash
python da_2_31.py --read_csv_kwargs '{"param_1": value_1, "param_2": value_2, "param_3": "str_1" ...}'
```

__--read_csv_kwargs__ - parameters for pandas.read_csv function. This function is used for reading provided data.  

After __--read_csv_kwargs__ you need to print a python dictionary object between ' ' like in the example above.  
Indeed this string is just converted to the dict type via __json.loads__ function.  

* __Parameters for an image with heatmaps__

```bash
python da_2_31.py --figsize 16 8 --output <dir_path>/<file_name>.[png, jpg, jpeg] --show
```

__--figsize__ - Size of the image in inches. In the exapmle - 16 is height, 8 is width.  

__--output__ - Absolute path to a file where to save the image.  

__--show__ - Boolean parameter. If it's set then show the image on display.
