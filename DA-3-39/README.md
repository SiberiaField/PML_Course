# DA-3-39: Create and Analyze Interaction Feature

In this task, I had to create an interaction feature between a numerical and a categorical column, visualize the results using boxplots, and save or display the output.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the program

* __Use default parameters__

```bash
python da_3_39.py
```

__Note__: Running with default parameters generates synthetic data, creates an interaction feature, and displays boxplots.

* __Print help message__

```bash
python da_3_39.py [-h, --help]
```

* __Parameters for reading dataset__

```bash
python da_3_39.py --data <path_to_csv> --read_csv_kwargs '{"param_1": value_1, "param_2": value_2, "param_3": "str_1" ...}'
```

__--data__ - Path to the input CSV file. If not provided, synthetic data is generated.  
__--read_csv_kwargs__ - Parameters for pandas.read_csv function. Provide a dictionary as a string.

* __Parameters for data generation and processing__

```bash
python da_3_39.py --samples 1000 --num_col "numerical_feature" --cat_col "categorical_feature"
```

__--samples__ - Number of samples in synthetic data (default: 1000).  
__--num_col__ - Name of the numerical feature column (default: "numerical_feature").  
__--cat_col__ - Name of the categorical feature column (default: "categorical_feature").

* __Output options__

```bash
python da_3_39.py --output_data <path_to_csv> --output_plot <path_to_image> --show_plot
```

__--output_data__ - Save the processed data to a CSV file.  
__--output_plot__ - Save the boxplot visualization to an image file (PNG, JPG, JPEG).  
__--show_plot__ - Display the boxplot on screen.
