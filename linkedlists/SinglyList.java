package net.sophiale.linkedlists;
import java.util.concurrent.ThreadLocalRandom;

public class SinglyList<T extends Comparable> implements List<T> {
    SinglyNode<T> mHead;

    @Override
    public T getHead() {
        return mHead == null ? null : mHead.val;
    }

    @Override
    public void prepend(T value) {
        final SinglyNode<T> node = new SinglyNode<>(value);
        node.next = mHead;
        mHead = node;
    }

    @Override
    public boolean search(T value) {
        SinglyNode<T> node = mHead;
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
        SinglyNode<T> node = mHead;
        while (node != null) {
            len += 1;
            node = node.next;
        }
        return len;
    }

    @Override
    public T getAtFromHead(int k) {
        SinglyNode<T> node = mHead;
        while (k > 0 && node != null){
            node = node.next;
            k -= 1;
        }

        return k == 0 ? node.val : null;
    }

    @Override
    public T getTail() {
        if (mHead == null) {
            return null;
        }

        SinglyNode<T> node = mHead;
        while (node.next != null) {
            node = node.next;
        }
        return node.val;
    }

    @Override
    public void append(T value) {
        final SinglyNode<T> node = new SinglyNode<>(value);
        if (mHead == null) {
            mHead = node;
        }

        SinglyNode<T> cur = mHead;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = node;
    }

    @Override
    public T max() {
        if (mHead == null) {
            return null;
        }
        T maxVal = mHead.val;
        SinglyNode<T> node = mHead.next;
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
        SinglyNode<T> pre = mHead;
        SinglyNode<T> cur = mHead.next;
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
        if (mHead == null || mHead.next == null) {
            return;
        }

        SinglyNode<T> pre = null;
        SinglyNode<T> cur = mHead;
        SinglyNode<T> nex = mHead.next;

        while (nex != null) {
            cur.next = pre;
            pre = cur;
            cur = nex;
            nex = nex.next;
        }
        cur.next = pre;
        mHead = cur;
    }

    @Override
    public void print() {
        if (mHead == null) {
            System.out.print("null");
            return;
        }

        StringBuilder sb = new StringBuilder();
        SinglyNode<T> node = mHead;
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

        SinglyNode<T> tor = mHead;
        SinglyNode<T> har = mHead;
        while (har.next != null && har.next.next != null) {
            tor = tor.next;
            har = har.next.next;
        }
        return tor.val;
    }

    @Override
    public T getAtFromTail(int k) {
        if (mHead == null) {
            return null;
        }

        SinglyNode<T> fir = mHead;
        SinglyNode<T> sec = null;
        while (fir != null) {
            if (k == 0) {
                sec = (sec == null) ? mHead : sec.next;
            } else {
                k -= 1;
            }
            fir = fir.next;
        }
        return sec == null ? null : sec.val;
    }

    @Override
    public boolean cycleDetection() {
        if (mHead == null) {
            return false;
        }

        SinglyNode<T> tor = mHead;
        SinglyNode<T> har = mHead;
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

        SinglyNode<T> tail = mHead;
        while (tail.next != null) {
            tail = tail.next;
        }

        int len = this.length();
        int k = ThreadLocalRandom.current().nextInt(0, len);
        SinglyNode<T> node = mHead;
        while (k > 0) {
            node = node.next;
            k -= 1;
        }

        tail.next = node;
    }
}
