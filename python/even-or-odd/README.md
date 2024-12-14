# Even or Odd
~~~if-not:sql,shell
Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.
~~~

~~~if:sql
You will be given a table `numbers`, with one column `number`.</br>

Return a dataset with two columns: `number` and `is_even`, where `number` contains the original input value, and `is_even` containing `"Even"` or `"Odd"` depending on `number` column values.

### Numbers table schema

```text
* number INT
```

### Output table schema

```text
* number  INT
* is_even STRING
```
~~~

~~~if:shell
Write a script that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.
~~~


## Información del Kata realizado:
Creado por: suuuzi

Publicado el: 7/31/2014

URL: [Haz click aquí para ir al Kata](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)