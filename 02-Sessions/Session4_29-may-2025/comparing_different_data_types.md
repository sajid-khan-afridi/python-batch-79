Here's a well-structured comparison of **List**, **Tuple**, **Dictionary**, and **Set** in Python — highlighting both **common features** and **unique points** using clear headings:

---

### ✅ 1. **List**

A list is an **ordered collection of items**, typically used to store multiple values in a single variable.

| Feature               | Description                                        |
| --------------------- | -------------------------------------------------- |
| ✅ Ordered            | Items retain the order of insertion.               |
| ✅ Mutable            | Elements can be added, removed, or changed.        |
| ✅ Indexed            | Accessed using indices (e.g., `list[0]`).          |
| ✅ Allows Duplicates  | Can contain duplicate elements.                    |
| ✅ Heterogeneous      | Can contain different data types (int, str, etc.). |
| 🔁 Supports Iteration | You can loop over it easily.                       |

🔸 **Example:**

```python
my_list = [1, 2, 3, 4, 2]
```

---

### ✅ 2. **Tuple**

A tuple is an **ordered and immutable collection** of elements.

| Feature                       | Description                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| ✅ Ordered                    | Retains insertion order.                                      |
| ❌ Immutable                  | Cannot be changed after creation.                             |
| ✅ Indexed                    | Accessed using indices (e.g., `tuple[1]`).                    |
| ✅ Allows Duplicates          | Can contain repeated values.                                  |
| ✅ Heterogeneous              | Can hold mixed data types.                                    |
| ✅ Hashable (if elements are) | Can be used as dictionary keys if all elements are immutable. |

🔸 **Example:**

```python
my_tuple = (1, "apple", 3.14)
```

---

### ✅ 3. **Dictionary**

A dictionary is a **collection of key-value pairs** for mapping information.

| Feature                | Description                                   |
| ---------------------- | --------------------------------------------- |
| ✅ Ordered (since 3.7) | Maintains insertion order.                    |
| ✅ Mutable             | Keys/values can be added or modified.         |
| ❌ Not Indexed         | Accessed via keys, not numeric indexes.       |
| ❌ No Duplicate Keys   | Keys must be unique; values may duplicate.    |
| ✅ Fast Lookup         | Ideal for key-based retrievals.               |
| ✅ Nested Allowed      | Values can be other dictionaries, lists, etc. |

🔸 **Example:**

```python
my_dict = {"name": "Sikandar", "age": 30}
```

---

### ✅ 4. **Set**

A set is an **unordered collection of unique elements**.

| Feature                          | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| ❌ Unordered                     | No guarantee of item order.                    |
| ✅ Mutable                       | Can add or remove elements.                    |
| ❌ Not Indexed                   | Elements not accessed by index.                |
| ❌ No Duplicates                 | Automatically removes duplicates.              |
| ✅ Optimized for Membership Test | Very fast for checking if an item exists.      |
| ✅ Set Operations                | Supports union, intersection, difference, etc. |

🔸 **Example:**

```python
my_set = {1, 2, 3, 2}  # Duplicate '2' will be removed
```

---

### 🔄 Summary Table

| Feature / Type       | List | Tuple | Dictionary | Set |
| -------------------- | ---- | ----- | ---------- | --- |
| Ordered              | ✅   | ✅    | ✅ (3.7+)  | ❌  |
| Mutable              | ✅   | ❌    | ✅         | ✅  |
| Indexed              | ✅   | ✅    | ❌         | ❌  |
| Allows Duplicates    | ✅   | ✅    | ❌ (keys)  | ❌  |
| Heterogeneous        | ✅   | ✅    | ✅         | ✅  |
| Hashable             | ❌   | ✅\*  | ❌         | ❌  |
| Fast Membership Test | ❌   | ❌    | ✅         | ✅  |
| Use as Dict Key      | ❌   | ✅\*  | N/A        | ❌  |

> **Note:** Tuples are hashable only if all their elements are immutable.
