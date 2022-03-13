package net.sophiale.linkedlists;

public class DoublyNode<T> {
    T val;
    DoublyNode<T> next;
    DoublyNode<T> prev;

    public DoublyNode(T val) {
        this.val = val;
    }
}
