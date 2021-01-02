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

The fact that there `8` distinct elements in `[2:12]` means that only two 
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