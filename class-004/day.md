# Find day

### Algo

```markdown
list = [0, 3, 3, 6, 8, 11, 13, 16, 19, 21 24, 26]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

Read date "dd"
Read month "mm"
Read year "yy"

y = yy -1
m = m -1

y = y mod 400

excess_day = ((y / 100) * 5) + (y mod 100) + (y / 4) + list[m] + dd

if(year == leap) and m >= 2
    excess_day += 1
```