from pathlib import Path

#creating a relative path
def create_path():
    path = Path(__file__).parent
    path.mkdir(parents=True, exist_ok=True)
    return path

def main():
    file_path = create_path() / 'dados.txt'

    with file_path.open('w') as file:
        file.writelines(["Ahmad", "roberto"])
    return


if __name__  == '__main__':
    main()