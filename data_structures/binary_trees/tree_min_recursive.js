// Find the minimum node value in a binary tree recursively

class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

const treeMin = (root) => {

    if (root === null) return Infinity;

    const leftMin = treeMin(root.left);
    const righttMin = treeMin(root.right);

    return Math.min(root.val, leftMin, righttMin);
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