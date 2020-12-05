public class GenericArrayStack<E> implements Stack<E> {
   
   private E[] elements;
   private int top;

   @SuppressWarnings("unchecked")

   // Constructor
    public GenericArrayStack( int capacity ) {
        
        elements = (E[]) new Object[capacity];
        top=0;
    }


    // Returns true if this ArrayStack is empty
    public boolean isEmpty() {
        
        return top==0;
    }


    public void push( E elem ) {
        
        elements[top] = elem;
        top++;
    }


    public E pop() {
        
        E temp;

        top--;
        temp=elements[top];
        elements[top] = null;

        return temp;
    }


    public E peek() {
        
        return elements[top-1];
    }
}