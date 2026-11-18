# DFS Comparison Summary 

| Feature | Preorder | Postorder |
|---------|----------|-----------|
| Visit Timing | Record node on first entry. | Record node on last exit. |
| Primary Use | Tree cloning, prefix notation, serialization. | Node deletion, postfix notation, topological sort (via RPO). |
| Graph Property | Reflects discovery order. | Ensures all successors are processed first. |
| Reversal Relation | Reverse preorder is not postorder in graphs. | Reverse postorder is not preorder in graphs. |
