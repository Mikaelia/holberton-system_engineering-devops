# 0x01. Shell, permissions
  
An introductory project on:
#### Permissions
- What do the commands chmod, sudo, su, chown, chgrp do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- How to change user ID or become superuser
#### Other man pages
- How to create a user
- How to create a group
- How to print real and effective user and group IDs
- How to print the groups a user is in
- How to print the effective userid
## Requirements
- Allowed editors: emacs
- All scripts tested on Ubuntu 14.04 LTS
## File Descriptions
### Mandatory
**[0-iam_betty](0-iam_betty)** - Create a script that changes your user ID to betty.

**[1-who_am_i](1-who_am_i)** - Write a script that prints the effective userid of the current user.

**[2-groups](2-groups)** - Write a script that prints all the groups the current user is part of.

**[3-new_owner](3-new_owner)** - Write a script that changes the owner of the file hello to the user betty.

**[4-empty](4-empty)** - Write a script that creates an empty file called hello.

**[5-execute](5-execute)** - Write a script that adds execute permission to the owner of the file hello.

**[6-multiple_permissions](6-multiple_permissions)** - Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
* You’re not allowed to use `sed`

**[7-everybody](7-everybody)** - Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello.
- You are not allowed to use commas for this script.

**[8-James_Bond](8-James_Bond)** - Write a script that sets the permission to the file hello as follows:
- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions
The file hello will be in the working directory You are not allowed to use commas for this script.

**[9-John_Doe](9-John_Doe)** - Write a script that sets the mode of the file hello to this, without using commas:

`-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`

**[10-mirror_permissions](10-mirror_permissions)** - Write a script that sets the mode of the file `hello` the same as `olleh`’s mode

**[11-directories_permissions](11-directories_permissions)** - Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

**[12-directory_permissions](12-directory_permissions)** - Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.

**[13-change_group](13-change_group)** - Write a script that changes the group owner to `holberton` for the file `hello`.

**[14-change_owner_and_group](14-change_owner_and_group)** - Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.

**[15-symbolic_link_permissions](15-symbolic_link_permissions)** - Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively.

**[16-whatsnext](16-whatsnext)** - Write a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.

### Advanced
**[100-Star_Wars](100-Star_Wars)** - Write a script that will play the StarWars IV episode in the terminal.
