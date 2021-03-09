// learning source: Traversy Media (YouTube)

class Stack {
    constructor() {
        this.items = [];
        this.count = 0;
    }

    push(item) {
        this.items[this.count] = item;
        console.log(`${item} pushed to ${this.count}`);
        this.count++;
        return this.count - 1;
    }

    pop() {
        // check if stack is empty or not
        if (this.count == 0) return null;
        let deletedItem = this.items[this.count - 1]; // take the top item
        console.log(`${deletedItem} removed`);
        this.count--;
        return deletedItem;
    }

    getLast() {
        console.log(`Last item is: ${this.items[this.count-1]}`);
        return this.items[this.count - 1];
    }

    isEmpty() {
        console.log(this.count == 0 ? 'Stack is empty' : 'Stack is NOT empty');
        return this.count == 0; // true or false that the size of stack is 0
    }

    size() {
        console.log(`Size of the stack: ${this.count}`);
        return this.count;
    }

    print() {
        let stack = 'ITEM\t-\tINDEX\n';
        for (let i=this.count-1; i>=0; i--) {
            stack += this.items[i] + `\t-\t${i}\n`;
        }
        return stack;
    }

    clear() {
        this.items = [];
        this.count = 0;
        console.log('Stack cleared');
        return this.items;
    }
}

const stack = new Stack();

stack.push(100);
stack.push(200);
stack.push(300);
stack.push(400);

console.log(stack.print());

stack.pop();
stack.pop();

console.log(stack.print());

stack.size();
stack.getLast();