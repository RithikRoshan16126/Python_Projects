# Lab Exercise 13: CSV-Based Payroll Management System
# Student: Rithik Roshan| USN: 25BTRAD090
import csv

INPUT_FILE = "employees.csv"
OUTPUT_FILE = "payroll_summary.csv"

def main():
    total_gross = 0
    total_deductions = 0
    total_net = 0

    try:
        with open(INPUT_FILE, newline="", encoding="utf-8") as source:
            reader = csv.DictReader(source)
            results = []

            for row in reader:
                hours = float(row["hours"])
                rate = float(row["rate"])
                tax_rate = float(row["tax_rate"])

                if hours < 0 or rate < 0 or not 0 <= tax_rate <= 1:
                    raise ValueError(f"Invalid payroll data for {row['name']}")

                gross = hours * rate
                deductions = gross * tax_rate
                net = gross - deductions

                results.append({
                    "id": row["id"],
                    "name": row["name"],
                    "gross": f"{gross:.2f}",
                    "deductions": f"{deductions:.2f}",
                    "net": f"{net:.2f}"
                })

                total_gross += gross
                total_deductions += deductions
                total_net += net

        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as output:
            fields = ["id", "name", "gross", "deductions", "net"]
            writer = csv.DictWriter(output, fieldnames=fields)
            writer.writeheader()
            writer.writerows(results)

        print(f"Employees processed: {len(results)}")
        print(f"Total gross:      {total_gross:.2f}")
        print(f"Total deductions: {total_deductions:.2f}")
        print(f"Total net pay:    {total_net:.2f}")
        print(f"Saved details to {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Could not find {INPUT_FILE}.")
    except (KeyError, ValueError) as error:
        print(f"Check the CSV columns and values: {error}")

if __name__ == "__main__":
    main()
