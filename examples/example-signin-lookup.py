from pyonepassword import (
    OP,
    OPSigninException,
    OPLookupException,
    OPNotFoundException
)
import getpass
import os
import sys
parent_path = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
if parent_path not in sys.path:
    sys.path.append(parent_path)


def do_signin():
    # If you've already signed in at least once, you don't need to provide all
    # account details on future sign-ins. Just master password
    my_password = getpass.getpass(prompt="1Password master password:\n")
    return OP(password=my_password)


if __name__ == "__main__":
    try:
        op = do_signin()
    except OPSigninException as opse:
        print("1Password sign-in failed.")
        print(opse.err_output)
        exit(opse.returncode)
    except OPNotFoundException as opnf:
        print("Uh oh. Couldn't find 'op'")
        print(opnf)
        exit(opnf.errno)

    print("Signed in.")
    print("Looking up \"Example Login\"...")
    try:
        item_password = op.get_item_password("Example Login")
        print(item_password)
        print("")
        print("\"Example Login\" can also be looked up by its uuid")
        print("")
        print("Looking up uuid \"ykhsbhhv2vf6hn2u4qwblfrmg4\"...")
        item_password = op.get_item_password("ykhsbhhv2vf6hn2u4qwblfrmg4")
        print(item_password)
    except OPLookupException as ople:
        print("1Password lookup failed: {}".format(ople))
        print(ople.err_output)
        exit(ople.returncode)
    except OPNotFoundException as opnf:
        print("Uh oh. Couldn't find 'op'")
        print(opnf)
        exit(opnf.errno)
