import java.util.*;
public class demo2 {
    public static int find(List<Integer> lis){
        System.out.println(lis);
        return 0;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int i;
        int num = sc.nextInt();
        List<Integer> li = new ArrayList<Integer>();
        for(i=0;i<num;i++){
            li.add(sc.nextInt());
        }
        find(li);
    }
    
}
