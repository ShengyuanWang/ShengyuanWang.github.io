import java.util.*;


class A_Watermelon{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        s.close();
        solve(n);

    }

    static void solve(int n) {
        if (n == 2) {
            System.out.println("NO");
            return;
        }
        if (n % 2 == 0) {
            System.out.println("YES");
            return;
        } else {
            System.out.println("NO");
            return;
        }

    }
}