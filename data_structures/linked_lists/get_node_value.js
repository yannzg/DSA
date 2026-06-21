class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

const a = new Node(2);
const b = new Node(5);
const c = new Node(5);
const d = new Node(6);
  
a.next = b;
b.next = c;
c.next = d;

const getNodeValue = (head, index) => {
    if (head == null) return null;
    if (index == 0) return head.val;
    return getNodeValue(head.next, index - 1);
}

console.log(getNodeValue(a, 1))