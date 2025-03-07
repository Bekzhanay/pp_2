import os

def f(path):

    print("Directory:")
    with os.scandir(path) as it:
        for x in it:
            if (x.is_dir()):
                print(x.name)

    print("\nFiles:")
    with os.scandir(path) as it:
        for x in it:
            if (not x.is_dir()):
                print(x.name)

    print("\nDirectories and files:")            
    with os.scandir(path) as it:
        for x in it:
            if (x.is_dir()):
                print(f"\n{x.name}:")
                y = os.path.join(path, x.name)
                with os.scandir(y) as itr:
                    for i in itr:
                        print(i.name)
    

path = input()
f(path)