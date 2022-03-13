package net.sophiale.linkedlists;
import java.util.concurrent.ThreadLocalRandom;

public class DoublyList<T extends Comparable> implements List<T> {
    DoublyNode<T> mHead;
    DoublyNode<T> mTail;

    @Override
    public T getHead() {
        return mHead == null ? null : mHead.val;
    }

    @Override
    public void prepend(T value) {
        DoublyNode<T> node = new DoublyNode<>(value);
        node.next = mHead;
        mHead.prev = node;
        mHead = node;
    }

    @Override
    public boolean search(T value) {
        DoublyNode<T> node = mHead;
        while (node != null) {
            if (node.val == value) {
                return true;
            }
            node = node.next;
        }
        return false;
    }

    @Override
    public int length() {
        int len = 0;
        DoublyNode<T> node = mHead;
        while (node != null) {
            len += 1;
            node = node.next;
        }
        return len;
    }

    @Override
    public T getAtFromHead(int k) {
        DoublyNode<T> node = mHead;
        while (k > 0 && node != null){
            node = node.next;
            k -= 1;
        }

        return k == 0 ? node.val : null;
    }

    @Override
    public T getTail() {
        return mTail == null ? null : mTail.val;
    }

    @Override
    public void append(T value) {
        DoublyNode<T> node = new DoublyNode<>(value);
        mTail.next = node;
        mTail = node;
    }

    @Override
    public T max() {
        if (mHead == null) {
            return null;
        }
        T maxVal = mHead.val;
        DoublyNode<T> node = mHead.next;
        while (node != null) {
            if (maxVal.compareTo(node.val) < 0) {
                maxVal = node.val;
            }

            node = node.next;
        }
        return maxVal;
    }

    @Override
    public boolean removeFirstOccur(T value) {
        if (mHead.val == value) {
            mHead = mHead.next;
        }
        DoublyNode<T> pre = mHead;
        DoublyNode<T> cur = mHead.next;
        while (cur != null) {
            if (cur.val == value) {
                pre.next = cur.next;
                return true;
            }
            pre = pre.next;
            cur = cur.next;
        }
        return false;
    }

    @Override
    public void reverse() {
        if (mHead == null || mHead == mTail) {
            return;
        }

        DoublyNode<T> node = mHead;
        DoublyNode<T> tail = mTail;
        while (node != null) {
            DoublyNode<T> nex = node.next;
            DoublyNode<T> pre = node.prev;

            node.next = pre;
            node.prev = nex;

            node = node.prev;
        }

        mTail = mHead;
        mHead = tail;
    }

    @Override
    public void print() {
        if (mHead == null) {
            System.out.print("null");
            return;
        }

        StringBuilder sb = new StringBuilder();
        DoublyNode<T> node = mHead;
        while (node != null) {
            sb.append(node.val);
            if (node.next != null) {
                sb.append(',');
            }
            node = node.next;
        }
        System.out.print(sb);
    }

    @Override
    public T getMid() {
        if (mHead == null) {
            return null;
        }

        DoublyNode<T> tor = mHead;
        DoublyNode<T> har = mHead;
        while (har.next != null && har.next.next != null) {
            tor = tor.next;
            har = har.next.next;
        }
        return tor.val;
    }

    @Override
    public T getAtFromTail(int k) {
        DoublyNode<T> node = mTail;
        while (k > 0 && node != null){
            node = node.prev;
            k -= 1;
        }

        return k == 0 ? node.val : null;
    }

    @Override
    public boolean cycleDetection() {
        if (mHead == null) {
            return false;
        }

        DoublyNode<T> tor = mHead;
        DoublyNode<T> har = mHead;
        while (har.next != null && har.next.next != null) {
            tor = tor.next;
            har = har.next.next;
            if (tor == har) {
                return true;
            }
        }
        return false;
    }

    @Override
    public void createCycle() {
        if (mHead == null) {
            return;
        }

        if (this.cycleDetection()) {
            return;
        }

        int len = this.length();
        int k = ThreadLocalRandom.current().nextInt(0, len);
        DoublyNode<T> node = mHead;
        while (k > 0) {
            node = node.next;
            k -= 1;
        }

        mTail.next = node;
    }
}
