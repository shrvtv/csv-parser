# CSV Parser
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=shrvtv_csv-parser&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=shrvtv_csv-parser)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=shrvtv_csv-parser&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=shrvtv_csv-parser)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=shrvtv_csv-parser&metric=bugs)](https://sonarcloud.io/summary/new_code?id=shrvtv_csv-parser)

This is a CLI tool that compares CSV files and generates a statistical report based on their data.

### Usage
```shell
python3 main.py --files tests/fixtures/physics.csv tests/fixtures/math.csv tests/fixtures/programming.csv --report median_coffee
```
You MUST specify at least one relative file path.

If multiple are provided, they are merged and analyzed together instead of on per-file basis.

As of 2026-03-29, only median function is supported and all entries are sorted high-to-low in the output.

### Output example
```shell
+-------------------+-----------------+
| student           |   median_coffee |
+===================+=================+
| Иван Кузнецов     |             700 |
+-------------------+-----------------+
| Дмитрий Морозов   |             610 |
+-------------------+-----------------+
| Михаил Павлов     |             590 |
+-------------------+-----------------+
| Никита Соловьев   |             560 |
+-------------------+-----------------+
| Алексей Смирнов   |             530 |
+-------------------+-----------------+
| Сергей Козлов     |             480 |
+-------------------+-----------------+
| Павел Новиков     |             450 |
+-------------------+-----------------+
| Артем Григорьев   |             420 |
+-------------------+-----------------+
| Елена Волкова     |             340 |
+-------------------+-----------------+
| Дарья Петрова     |             310 |
+-------------------+-----------------+
| Татьяна Васильева |             270 |
+-------------------+-----------------+
| Анна Белова       |             210 |
+-------------------+-----------------+
| Ольга Новикова    |             200 |
+-------------------+-----------------+
| Виктория Федорова |             150 |
+-------------------+-----------------+
| Мария Соколова    |             140 |
+-------------------+-----------------+
```