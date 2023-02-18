from searchGenerator import searchGenerator, searchMonkey, searchMobile
from signIn import signIn
from setup import setup

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup()
    searchGenerator()
    driver = signIn()
    driver = searchMonkey(driver)
    searchMobile("driver")
