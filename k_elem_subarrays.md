Looking for subarrays with `K` elements. Currently looking at subarray 
`[a:a+k]` for some `K < k`. It is known that there are `K + c, c > 0` 
distinct elements in `[a:a + n]`, where `k<n`. Can there be `K` distinct 
elements in `[a:a+k]`?

For example, take array
```
[1, 4, 6, 8, 4, 6, 7, 3, 9, 2, 8, 5, 0, 7, 1, 8, 8]
```
with `K=3`, `a=2`, `k=7`, `n=10`. 

We then have 
```
[a:a+n] = [2:12] = [6, 8, 4, 6, 7, 3, 9, 2, 8, 5]
[a:a+k] = [2:9] = [6, 8, 4, 6, 7, 3, 9]
c = 5
```

The fact that there `8` are distinct elements in `[2:12]` means that only two 
elements in `[2:12]` repeat. Even if all of those repeating elements are 
within `[2:9]` that still leaves us with the minimum of `(9 - 2) - 2 = 5` 
elements. So there is no way that there are `3` elements in `[2:9]`.

More broadly, `K + c` distinct elements in `[a:a+n]` 
⇒ `n - (K + c)` elements in `[a:a+n]` repeat 
⇒ at most `n - (K + c)` elements repeat in `[a:a+k]` 
⇒ the amount of distinct elements in `[a:a+k]` is at least 
`k - (n - (K + c))`. So for there to be `K` elements in 
`[a:a+k]` we must have `k - n + K + c <= K` or, 
equivalently, `k + c <= n`

So, to have a chance of encountering a subarray of length `k` with `K` 
distinct elements, we must advance `a` by `n - (k + c)`


If there are `K - c` elements in `[a:a+n]` then there can't possibly be 
`K` elements in `[a:a+k]`, in fact there can't possibly be `K` elements in 
`[a+s:a+s+k]` for any `s` such that `a + s + k <= a + n`. For there to be `K` 
elements in `[a+s:a+s+k]` we need to have `a + n + c < a + s + k` or, equivalently,
`n + c - k < s`

### Some examples:
####Caterpillar examples
Examples contain slices of `K` elements  

- `s` - start of the slice
- `ś` - the last index such that `[ś:e]` contains `K` elements
- `e` - end of the slice
- `é` - the first such index that `[s:é]` contains `K` elements 
```
K = 4
1 2 3 4 3 2 1 5
^     ^ ^     ^
s     é ś     e

K = 4
1 2 3 4 1 2 3 4 5
^     ^   ^     ^
s     é   ś     e

K = 4
1 2 3 4 1 2 3 4 1 2 3 4 5
^     ^           ^     ^
s     é           ś     e

K = 4
1 2 3 4 5
^ ^   ^ ^
s ś   é e
```