<div align="center">
  <h1>AirBnB clone - The Console <img src="https://i.imgur.com/elr4ah9.png" width=55 align=center> </h1>
  <h4>
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone#storage">Storage</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone#console">Console</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone#execution">Execution</a>
    •
    <a href="https://github.com/Juanesduque1/holbertonschool-AirBnB_clone#tests">Tests</a>
  </h4>
</div>

<img align="center" src="https://i.imgur.com/MQq3ABc.png" alt="Logo">

## Description

This project is the first version of the AirBnB project, which is an AirBnB clone that includes design, layout, infrastructure and database. In this repository you will find the AirBnB console, which executes specific commands (shown below) to make specific actions.

<img src="https://i.imgur.com/4biBGlj.png" alt="Project">

## Console

The console is used to manage the storage of class instances (`file.json`), this console can be used and executed in two ways, which are interactive and non-interactive mode.

The following table shows all the commands for storage management and explains how to use them by its format:

| Command     | Description | Format |
| ----------- |:------------| :-------|
| help        | Shows all allowed commands or gives information about a specific command. | `help` / `help <command>` |
| quit or EOF | Exits the program. | `quit` |
| create      | Creates a new instance. | `create <classname>` |
| show        | Shows a specific instance by its `classname` and its `id`. | `show <classname> <id>` |
| all         | Displays all stored instances or all stored instances of a specific class by its `classname`. | `all` / `all <classname>` |
| update      | Updates an instance (adds or modifies attributes) by its `classname`, `id`, `attribute` and its `value` to add/modify.  | `update <classname> <id> <attribute> <attrvalue>` |
| destroy     | Deletes an instance by its `classname` and its `id`. | `destroy <classname> <id>` |


## Execution

`Interactive mode`

```shell
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$
```

`Non-Interactive Mode`

```shell
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
```

`Examples using the Hbnb console`

Console execution and `help` command implementation to get information about `quit` command:

<img src="https://i.imgur.com/DCpKxZa.gif" width=550 alt="Example gif">

`Create`, `update` and `show` command implementation to create and display a new instance:

<img src="https://i.imgur.com/SZQqSYb.gif" width=550 alt="Example gif">

`Create`, `destroy` and `all` command implementation to display how the `destroy` command works:

<img src="https://i.imgur.com/Auuj3TI.gif" width=550 alt="Example gif">
