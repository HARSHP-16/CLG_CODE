import java.util.Stack;
import java.util.Scanner;

public class stack {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
     
        System.out.print("Enter a string to reverse: ");
        String input = scanner.nextLine();

       
        Stack<Character> stack = new Stack<>();

        
        for (int i = 0; i < input.length(); i++) {
            stack.push(input.charAt(i));
        }

        
        StringBuilder reversed = new StringBuilder();
        while (!stack.isEmpty()) {
            reversed.append(stack.pop());
        }

      
        System.out.println("Reversed string: " + reversed.toString());

        scanner.close();
    }
}
