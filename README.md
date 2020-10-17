# String-Builder

An experiment in time complexity versus real world performance

## Results

Sample Output:

```text
Runtime of join_words_cat was 5.8871 seconds
Runtime of join_words_builder was 29.0302 seconds
Runtime of join_words_join was 0.5058 seconds
```

Concatenation-based string building is [known to be inefficient in some cases](https://pellegrino.link/2015/08/22/string-concatenation-with-java-8.html). In the real world, concatenation seems to work just fine for small scale string building. In this example, the additional overhead of a custom string building class far outweighs the benefits of its reduced time complexity. Python's `str.join()` method is shown to be the simplest and most efficient option, boosted by it's efficient algorithm and [C implementation](http://svn.python.org/projects/python/trunk/Objects/stringobject.c).