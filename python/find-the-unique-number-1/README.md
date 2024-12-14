# Find the unique number
There is an array with some numbers. All numbers are equal except for one. Try to find it!

```javascript
findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
```

```swift
findUniq([ 1, 1, 1, 2, 1, 1 ]) == 2
findUniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

```ruby
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

```python
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

```java
Kata.findUniq(new double[]{ 1, 1, 1, 2, 1, 1 }); // => 2
Kata.findUniq(new double[]{ 0, 0, 0.55, 0, 0 }); // => 0.55
```

```haskell
getUnique [1, 1, 1, 2, 1, 1] -- Result is 2
getUnique [0, 0, 0.55, 0, 0] -- Result is 0.55
```

```fsharp
findUniq([ 1; 1; 1; 2; 1; 1 ]) = 2
findUniq([ 0; 0; 0.55; 0; 0 ]) = 0.55
```

```c
finduniq((const float[]){1, 1, 1, 2, 1, 1}, 5); /* --> 2 */
finduniq((const float[]){0, 0, 0.55, 0, 0}, 5); /* --> 0.55 */
```
```nasm
nums:  dd  1., 1., 1., 2., 1., 1.

mov rdi, nums
mov rsi, 6
call finduniq       ; XMM0 <- 2


nums:   dd  0., 0., 0.55, 0., 0.

mov rdi, nums
mov rsi, 6
call finduniq       ; XMM0 <- 0.55
```
```cpp
find_uniq(std::vector<float>{1, 1, 1, 2, 1, 1});  // --> 2
find_uniq(std::vector<float>{0, 0, 0.55, 0, 0});  // --> 0.55
```

```rust
find_uniq(&[1.0, 1.0, 1.0, 2.0, 1.0, 1.0]) // => 2.0
find_uniq(&[0.0, 0.0, 0.55, 0.0, 0.0]) // => 0.55
```

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

1. Find the unique number (this kata)
2. [Find the unique string](https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)
3. [Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)


## Información del Kata realizado:
Creado por: isqua

Publicado el: 12/23/2016

URL: [Haz click aquí para ir al Kata](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)