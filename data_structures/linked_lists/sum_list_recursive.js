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

const sumList = (head) => {
    if (head == null) return 0;
    return head.val + sumList(head.next);
}

console.log(sumList(a));