# Build a Quick Sort Algorithm

## Objective

Create a program that sorts a list of numbers using the **Quick Sort** algorithm.

The goal is to practice recursion, list manipulation, comparison logic, and the process of dividing a problem into smaller subproblems.

## Concepts Practiced

* Functions
* Recursion
* Conditional statements (`if`)
* `for` loops
* Lists
* List concatenation
* Comparison operators
* Return values
* Divide-and-conquer algorithms
* Base cases in recursive functions

## How It Works

The algorithm selects the first element of the list as a reference (pivot) and divides the remaining elements into three groups:

* `less_ref`: elements smaller than the reference
* `equal_ref`: elements equal to the reference
* `greater_ref`: elements greater than the reference

The function then recursively sorts the `less_ref` and `greater_ref` lists.

Finally, the three lists are concatenated to produce the sorted list.

## Example

```python
quick_sort([83, 4, 24, 2])
```

Returns:

```text
[2, 4, 24, 83]
```
