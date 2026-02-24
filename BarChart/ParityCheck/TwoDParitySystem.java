import java.util.Scanner;

public class TwoDParitySystem {

//Sender
    public static int[][] sender(int[][] data, int rows, int cols) {

        int[][] frame = new int[rows + 1][cols + 1];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                frame[i][j] = data[i][j];
            }
        }

        for (int i = 0; i < rows; i++) {
            int sum = 0;
            for (int j = 0; j < cols; j++) {
                sum += frame[i][j];
            }
            frame[i][cols] = sum % 2; 
        }


        for (int j = 0; j < cols; j++) {
            int sum = 0;
            for (int i = 0; i < rows; i++) {
                sum += frame[i][j];
            }
            frame[rows][j] = sum % 2;  
        }

        int total = 0;
        for (int i = 0; i < rows; i++) {
            total += frame[i][cols];
        }
        frame[rows][cols] = total % 2;

        return frame;
    }


    public static void receiver(int[][] frame, int rows, int cols) {

        boolean error = false;

        for (int i = 0; i <= rows; i++) {
            int sum = 0;
            for (int j = 0; j <= cols; j++) {
                sum += frame[i][j];
            }
            if (sum % 2 != 0) {
                System.out.println("Error detected in Row: " + i);
                error = true;
            }
        }

        
        for (int j = 0; j <= cols; j++) {
            int sum = 0;
            for (int i = 0; i <= rows; i++) {
                sum += frame[i][j];
            }
            if (sum % 2 != 0) {
                System.out.println("Error detected in Column: " + j);
                error = true;
            }
        }

        if (!error) {
            System.out.println("No Error Detected. Data Received Correctly.");
        }
    }


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of rows: ");
        int rows = sc.nextInt();

        System.out.print("Enter number of columns: ");
        int cols = sc.nextInt();

        int[][] data = new int[rows][cols];

        System.out.println("Enter data bits (0 or 1):");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                data[i][j] = sc.nextInt();
            }
        }

        // Sender Side
        int[][] frame = sender(data, rows, cols);

        System.out.println("\nTransmitted Frame:");
        for (int i = 0; i <= rows; i++) {
            for (int j = 0; j <= cols; j++) {
                System.out.print(frame[i][j] + " ");
            }
            System.out.println();
        }

        // Receiver Side
        System.out.println("\nChecking at Receiver Side...");
        receiver(frame, rows, cols);

        sc.close();
    }
}