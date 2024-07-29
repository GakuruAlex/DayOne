def band_name_gen(city: str, pet_name: str) -> str:
    """_A function that combines city and pet name to get a band name_

    Args:
        city (str): _City user grew up in_
        pet_name (str): _Name of a pet_

    Returns:
        str: _Band name_
    """
    return city + " " + pet_name


def main()-> None:
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    print(f"Your band name could be {band_name_gen(city, pet)}")

if __name__ == "__main__":
    main()