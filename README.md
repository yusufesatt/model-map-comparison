# Model mAP Graphs

This project includes a python script that creates graphs by reading data from CSV files of models trained with YOLO. The script generates graphs with mAP50 and mAP50-95 values using the CSV files that YOLO outputs at the end of training (`results.csv`) read from the YAML configuration file.

## Usage

1. **YAML Configuration File**: Edit `config.yaml` and add the file path (`file_path`) and model name (`model_name`) for each model. A sample YAML file:

   ```yaml
   - file_path: "path/to/model1.csv"
     model_name: "Model 1"
   - file_path: "path/to/model2.csv"
     model_name: "Model 2"
   
2. **Running the Script:** Run the following command in the terminal or command client:
   ```commandline
   python main.py
   ```
   The script will generate the charts and display them on the screen.

## Dependencies

- Python 3.x
- Pandas
- Matplotlib
- pyyaml

You can use the following command to install the required libraries:
````commandline
pip install pandas matplotlib pyyaml
````

## License

This project is licensed under the MIT License.

