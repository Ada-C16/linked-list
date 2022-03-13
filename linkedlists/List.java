package net.sophiale.linkedlists;

public interface List<T extends Comparable> {
    T getHead();

    void prepend(T value);

    boolean search(T value);

    int length();

    T getAtFromHead(int k);

    T getTail();

    void append(T value);

    T max();

    boolean removeFirstOccur(T value);

    void reverse();

    void print();

    T getMid();

    T getAtFromTail(int k);

    boolean cycleDetection();

    void createCycle();
}
