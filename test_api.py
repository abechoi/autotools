import requests
import sys
import csv

def main():

    if len(sys.argv) == 1:
    
        test_tenants = []

        with open("files/test_tenants.csv") as file:
            
            reader = csv.DictReader(file)

            for row in reader:
                test_tenants.append(row)

        print("\nCohort Number | Tenant Name\n---------------------------")

        for test_tenant in test_tenants:
            print(test_tenant["cohort"], test_tenant["tenant_name"].strip())

        cohort_number = int(input("---------------------------\nEnter Cohort Number, 0 - 5, to test: "))

        match cohort_number:
            case 0:
                test_api(test_tenants[0]["tenant_name"], test_tenants[0]["api_key"], cohort_number)
            case 1:
                test_api(test_tenants[1]["tenant_name"], test_tenants[1]["api_key"], cohort_number)
            case 2:
                test_api(test_tenants[2]["tenant_name"], test_tenants[2]["api_key"], cohort_number)
            case 3:
                test_api(test_tenants[3]["tenant_name"], test_tenants[3]["api_key"], cohort_number)
            case 4:
                test_api(test_tenants[4]["tenant_name"], test_tenants[4]["api_key"], cohort_number)
            case 5:
                test_api(test_tenants[5]["tenant_name"], test_tenants[5]["api_key"], cohort_number)


    elif len(sys.argv) == 3:

        tenant_name = sys.argv[1]
        api_key = sys.argv[2]

        test_api(tenant_name, api_key)

    else:

        print("ERROR: Please provide a tenant name and api key via command line or hard code them in the script!")
        print("Usage: python test_api.py <tenant_name> <api_key>")
        sys.exit(1)
    

def test_api(tenant_name, api_key, cohort_number=None):

    url = "https://api.servicetitan.com/v1/jobs?serviceTitanApiKey=" + api_key

    try:
    
        r = requests.get(url)
    
    finally:

        if cohort_number:
            print(f"\ntesting api key for {tenant_name} in cohort {cohort_number}...\n")
        else:
            print(f"\ntesting api key for {tenant_name}...\n")
    
        if r.status_code == 200:
            print(f"{tenant_name}: SUCCESS")
            print(f"status code: {r.status_code}")
        else:  
            print(f"{tenant_name}: FAILED")
            print(f"status code: {r.status_code}")

    sys.exit(0)

if __name__ == "__main__":
    main()