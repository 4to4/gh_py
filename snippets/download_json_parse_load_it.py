import wget, os, sys, pprint, requests, json
from pprint import pprint

src_url = r"https://data.baltimorecity.gov/resource/27w9-urtv.json"
# src_url = r"https://api.github.com/users/4to4"
out_dir = os.getenv('temp', default=None)
out_file_name = None
out_file_name = wget.download(src_url, out=out_dir)
print(f"Env variable %temp% not found. Using current directoy") if (out_dir == None) else ()


def download_with_wget():
    with (open(wget.download(src_url, out=out_dir), 'r', encoding=None)) as f:
        for i in f:
            print(f"> {i}")


def download_load_whole_file_in_var():
    resp = requests.get(src_url, params=None)
    () if (resp.status_code == 200) else sys.exit(-1)
    list_of_dicts = resp.json()
    for d in list_of_dicts:  # json method directly converts the object to a dict and in this case to list of dicts
        # pprint(d)
        pass

    for d in list_of_dicts:
        for attr in ("amountdue lot propertyaddress propertyid".split()):
            print(f"{attr} => {d.get(attr, None)}")
        print("-----------------------------------")


def main():
    # download_with_wget()
    download_load_whole_file_in_var()


if (__name__ == "__main__"):
    main()
