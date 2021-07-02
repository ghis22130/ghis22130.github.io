---
layout: post
title: LeetCode 226. Invert Binary Tree
comments: true
tags: [Argorithm, Swift]
category: [Swift]
---


## 문제 설명
Given the `root` of a binary tree, invert the tree, and return its root.



**Note**: A leaf is a node with no children.


# Example 1:

<img src = "https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg">

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

# Example 2:

<img src = "https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg">

```
Input: root = [2,1,3]
Output: [2,3,1]
```

# Example 3:

```
Input: root = []
Output: []
```

# Constraints:

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## 문제풀이

BFS와 DFS 모두 구현하여 풀어보았다.

```swift

class Solution {
    
    func BFS(_ root: TreeNode?) {
        guard let root = root else { return }
        var queue: [TreeNode] = [root]
        
        while !queue.isEmpty {
            for _ in queue {
                let node = queue.removeFirst()
                swap(&node.left, &node.right)
                if let leftNode = node.left { queue.append(leftNode) }
                if let rightNode = node.right { queue.append(rightNode) }
            }
        }
        
    }
    
    func DFS(_ root: TreeNode?) {
        guard let root = root else { return }
        swap(&root.right, &root.left)
        
        DFS(root.left)
        DFS(root.right)
    }
    
    func invertTree(_ root: TreeNode?) -> TreeNode? {
        BFS(root)
        //DFS(root)
        return root
    }
}
```

참고 : <https://leetcode.com/problems/invert-binary-tree/>