# csv_filter

A cli tool to filter rows from a csv file input
Supply the column name and values to filter on like this

```
    python3 -m csv_filter A=55
```

# Selecting multiple values

```
    python3 -m csv_filter B=Smith,Jones
```

# Selecting multiple columns

* Boolean operators or, and work as you would expect them to

```
    python3 -m csv_filter C=Monday,Tuesday or D=3.14
    python3 -m csv_filter C=Saturday,Sunday and D=3.14
```

# Set up the project from source

* use python3.11 as dependency_injection is not supported for 3.12 yet

```
    python3.11 -m venv  .venv
    source .venv/bin/activate
    pip3 install -r csv_filter/requirements.txt
```