import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os
import yaml

def read_and_process_csv(file_path):
    """
    Removes empty characters from the columns of the given csv file after reading it.

    :param
    file_path: A list of tuples containing file paths and model names. Each tuple should have the format (
    file_path, model_name).
    :return:
    data
    """

    data = pd.read_csv(file_path)
    data.columns = data.columns.str.strip()
    return data


def visualize_combined_data(file_paths):
    """
    Creates two different graphs with mAp-50, epoch, mAp50-95 values in csv file from file path function.

    :param
    file_paths: File path and model names taken from yaml file.
    :return
    None
    """

    # map 50
    max_epoch = 0

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)

    for file_path, model_name in file_paths:
        data = read_and_process_csv(file_path)
        file_max_epoch = max(data["epoch"])
        max_epoch = max(max_epoch, max(data["epoch"]))
        plt.plot(data["epoch"], data["metrics/mAP50(B)"], label=f"{model_name} (mAP50) - {file_max_epoch} epochs")

    plt.xlabel("Epoch", fontsize=12)
    plt.ylabel("mAP50(B)", fontsize=11, rotation=80)
    plt.title("mAP50(B) vs. Epoch")
    plt.legend(loc="best")
    plt.grid(True)

    y_ticks = [i / 100 for i in range(0, 101, 10)]
    plt.yticks(y_ticks)

    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    x_ticks = list(range(min(data["epoch"]), max_epoch + 1, 10))
    plt.xticks(x_ticks)

    # map 50-95
    plt.subplot(2, 1, 2)

    for file_path, model_name in file_paths:
        data = read_and_process_csv(file_path)
        file_max_epoch = max(data["epoch"])
        max_epoch = max(max_epoch, max(data["epoch"]))
        plt.plot(data["epoch"], data["metrics/mAP50-95(B)"], label=f"{model_name} (mAP95) - {file_max_epoch} epochs",)

    plt.xlabel("Epoch", fontsize=12)
    plt.ylabel("mAP95(B)", fontsize=11, rotation=80)
    plt.title("mAP95(B) vs. Epoch")
    plt.legend(loc="best")
    plt.grid(True)

    y_ticks = [i / 100 for i in range(0, 101, 10)]
    plt.yticks(y_ticks)

    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    x_ticks = list(range(min(data["epoch"]), max_epoch + 1, 10))
    plt.xticks(x_ticks)

    plt.tight_layout()  # Prevents graphics from being cramped

    plt.show()

def read_yaml_config(config_file):
    """
    Converts the data in the yaml file to python type and assigns it to the config_data variable, returns an error if
    config is empty

    :param
    config_file: The path to the YAML configuration file.

    :return
    config_data: Translates from yaml file to list.
    """
    try:
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        return config_data
    except FileNotFoundError:
        print(f"The config file '{config_file}' was not found.")
        return []

def main():
    config_file = 'config.yaml'
    config_data = read_yaml_config(config_file)

    if not config_data:
        print("No CSV files were added in the config file. The program has ended.")
        return

    file_paths = [(entry['file_path'], entry['model_name']) for entry in config_data]
    visualize_combined_data(file_paths)


if __name__ == "__main__":
    main()
