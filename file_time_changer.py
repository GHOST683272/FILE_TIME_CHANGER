import subprocess
folder_path = str(input("Enter the folder path --> "))
set_time = input("Enter the date and time DD/MM/YYYY HH:MM:SS")
ps_script = r"""
$time = Get-Date "{set_time}"

Get-ChildItem f"{folder_path} -Recurse -Force | ForEach-Object {
    if ($_.PSIsContainer) {
        [System.IO.Directory]::SetCreationTime($_.FullName, $time)
        [System.IO.Directory]::SetLastWriteTime($_.FullName, $time)
        [System.IO.Directory]::SetLastAccessTime($_.FullName, $time)
    } else {
        [System.IO.File]::SetCreationTime($_.FullName, $time)
        [System.IO.File]::SetLastWriteTime($_.FullName, $time)
        [System.IO.File]::SetLastAccessTime($_.FullName, $time)
    }
}
""".format(set_time)

subprocess.run(
    ["powershell", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
    check=True
)

