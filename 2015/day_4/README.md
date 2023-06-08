# The Ideal Stocking Stuffer

> Life is short, [the] craft long, opprotunity fleeting, experiment treacherous, judgement difficult.


## Part I

Santa needs helps [mining](https://en.wikipedia.org/wiki/Bitcoin#Mining) some AdventCoins (very similar to [Bitcoin](https://en.wikipedia.org/wiki/Bitcoin) ) to use as gift for all the economically forward-thinking little girls and boys.

To do this, he needs to find [MD5](https://en.wikipedia.org/wiki/MD5) hashes which, in [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal), start with at least *five zeros*. The input to the MD5 hash in some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeros: `1`, `2`, `3`, ...) that produces such a hash.

For example: 

- If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash of `abcdef609043` starts with five zeros (`000001dbfa...`), and it is the lowest such number to do so.

- If your secret key is `pqrstuv`, the lowest number it combines with to make an MD5 hash starting with five zeros is `1048970`; that is, the MD5 of `pqrstuv1048970` looks like `00000613ef...`.

## Part II 

Now find one that starts with *six zeros*.
