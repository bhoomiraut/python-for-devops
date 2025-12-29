#main file for log analyzer script, containing logic to parse and analyze log files

def analyze_log_file(log_file):
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        with open(log_file, 'r') as input_file:
            lines = input_file.readlines()

            if not lines:
                print("Log/ Input file is empty!")
                return 
            
            for line in lines:
                if "INFO" in line:
                    log_count["INFO"] += 1
                elif "WARNING" in line:
                    log_count["WARNING"] += 1   
                elif "ERROR" in line:
                    log_count["ERROR"] += 1
            
            print("Log Analysis Summary:")
            print("INFO: ", log_count["INFO"])
            print("WARNING: ", log_count["WARNING"])
            print("ERROR: ", log_count["ERROR"])

            write_summary_to_file(log_count)
        
    except FileNotFoundError:
        print("Log file not found!")

    except Exception as e:
        print("Unexpected error occurred", e)

def write_summary_to_file(summary):
    try:
        with open("log_summary.txt", "w") as output_file:
            output_file.write("Log Analysis Summary:\n")
            output_file.write(f"INFO: {summary['INFO']}\n")
            output_file.write(f"WARNING: {summary['WARNING']}\n")
            output_file.write(f"ERROR: {summary['ERROR']}\n")

    except Exception as e:
        print("Error while writing summary to file", e)
        
    
def main():
    analyze_log_file("app.log")

if __name__ == "__main__":
    main()