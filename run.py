import subprocess
def main():
    cmd="streamlit run display.py"
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main()