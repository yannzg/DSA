// Find the minimum node value in a binary tree

class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

const treeMin = (root) => {
    let smallest = Infinity;
    stack = [ root ];

    while (stack.length > 0) {
        const current = stack.pop();

        if (current.val < smallest) smallest = current.val;

        if (current.left !== null) stack.push(current.left); 
        if (current.right !== null) stack.push(current.right);
    }

    return smallest;
}

const a = new Node(3);
const b = new Node(11);
const c = new Node(4);
const d = new Node(4);
const e = new Node(-2);
const f = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

console.log(treeMin(a));