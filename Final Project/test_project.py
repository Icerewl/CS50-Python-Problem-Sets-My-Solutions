from project import aliexpress,login_website,create_a_post
import pytest
def main():
    test_aliexpress()
    test_login_website()
    test_create_a_post()





def test_login_website():
    #assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert login_website("Test mail","Test pw") == "Successfuly Logged in"
    assert login_website("harvard@edu.com","Massachusets") == "Successfuly Logged in"
    assert login_website("Test mail",12345678) == "Failed to log in.Login info cannot be integers"
    

def test_create_a_post():
    with pytest.raises(TypeError):
        create_a_post("Three")
    assert create_a_post("2") == True
    assert create_a_post("Two") == False

def test_aliexpress():
    assert aliexpress("men shirt","3") == True
    with pytest.raises(TypeError):
        create_a_post("Women shirt","Three")







if __name__ == "__main__":
    main()