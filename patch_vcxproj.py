import sys


def main():
    """
    Patches .vcxproj to allow it to compile in Windows kernel mode code.
    """

    file_path = sys.argv[1]
    with open(file_path) as f:
        contents = f.readlines()

    contents.insert(2, "  <Target Name=\"GetDriverProjectAttributes\" Returns=\"@(DriverProjectAttributes)\"/>\n")
    contents.insert(3, "  <Target Name=\"GetPackageFiles\" Returns=\"@(FullyQualifiedFilesToPackage)\"/>\n")

    for i, line in enumerate(contents):
        if "<BasicRuntimeChecks>EnableFastChecks</BasicRuntimeChecks>" in line:
            contents.pop(i)
            break

    with open(file_path, "w") as f:
        f.writelines(contents)


if "__main__" == __name__:
    main()
