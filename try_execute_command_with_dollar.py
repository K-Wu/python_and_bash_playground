import subprocess

if __name__ == "__main__":
    output = subprocess.check_output("date | awk '{ print $1 }'", shell=True)
    print(output)
