#include <iostream>
using namespace std;

class CircularQueue {
    int *arr;
    int front, rear, size, capacity;

public:
    CircularQueue(int c) {
        capacity = c;
        arr = new int[capacity];
        front = rear = -1;
    }

    bool isFull() {
        return (front == 0 && rear == capacity - 1) || (rear == (front - 1) % (capacity - 1));
    }

    bool isEmpty() {
        return front == -1;
    }

    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue is Full!\n";
            return;
        }
        if (front == -1)
            front = 0;
        rear = (rear + 1) % capacity;
        arr[rear] = value;
        cout << value << " inserted.\n";
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is Empty!\n";
            return;
        }
        cout << arr[front] << " removed.\n";
        if (front == rear)
            front = rear = -1;
        else
            front = (front + 1) % capacity;
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is Empty!\n";
            return;
        }
        cout << "Queue Elements: ";
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear) break;
            i = (i + 1) % capacity;
        }
        cout << "\n";
    }
};

int main() {
    int n;
    cout << "Enter queue size: ";
    cin >> n;
    CircularQueue q(n);
    int ch, val;

    while (true) {
        cout << "\n1.Enqueue 2.Dequeue 3.Display 4.Exit\nEnter choice: ";
        cin >> ch;
        if (ch == 1) {
            cout << "Enter value: ";
            cin >> val;
            q.enqueue(val);
        } else if (ch == 2)
            q.dequeue();
        else if (ch == 3)
            q.display();
        else
            break;
    }
    return 0;
}
