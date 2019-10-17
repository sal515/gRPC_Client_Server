import csv
import json

NDBench_testing = "workload_data/NDBench-testing.csv"
NDBench_training = "workload_data/NDBench-training.csv"
DVD_testing = "workload_data/DVD-testing.csv"
DVD_training = "workload_data/DVD-training.csv"

NDBench_testing_json = "workload_data_json/NDBench-testing.json"
NDBench_training_json = "workload_data_json/NDBench-training.json"
DVD_testing_json = "workload_data_json/DVD-testing.json"
DVD_training_json = "workload_data_json/DVD-training.json"


# Open the CSV
def generate_json_from_csv(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, 'r') as f:
            # Change each field name to the appropriate field name
            reader = csv.DictReader(f, fieldnames=(
                "CPU",
                "NetworkIn",
                "NetworkOut",
                "Memory",
                "Final_Target"
            ))
            # Parse the CSV into JSON
            output = json.dumps([row for row in reader])
            # print("JSON parsed!")
            # f.close()
    except:
        print("Couldn't open CSV file")

    # print(f"Test: {output}")

    try:
        with open(json_file_path, 'w') as f:
            # Save the JSON
            f.write(output)
            # f.close()
            # print("JSON saved!")
    except:
        print("Couldn't save the JSON file")


generate_json_from_csv(NDBench_testing, NDBench_testing_json)
generate_json_from_csv(NDBench_training, NDBench_training_json)
generate_json_from_csv(DVD_testing, DVD_testing_json)
generate_json_from_csv(DVD_training, DVD_training_json)