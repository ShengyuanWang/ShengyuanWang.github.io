import java.util.* ;


class A_Way_Too_Long_Words{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        for (int i = 0; i <= t; i++){
            String word1 = s.nextLine();
            solve(word1);
        }
        s.close();
    }

    static void solve(String word) {
        int n = word.length();
        if (n > 10) {
            char begin = word.charAt(0);
            char end = word.charAt(n-1);
            Integer a = n-2;
            System.out.println(begin + a.toString() + end);
            return;
        } else {
            System.out.println(word);
            return;
        }
    }
}