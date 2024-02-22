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
