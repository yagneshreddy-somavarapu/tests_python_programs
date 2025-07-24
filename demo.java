import java.util.*;
public class demo
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int temp1,i,j,num,count,temp=0;
	    num = sc.nextInt();
	    count = sc.nextInt();
	    List<Integer> a=new ArrayList<Integer>();
	    for(i=0;i<num;i++){
	        temp = sc.nextInt();
	        a.add(temp);
	    }
	    List<Integer> b=new ArrayList<Integer>(a);
	    Collections.sort(b,Collections.reverseOrder());
	    for(i=0;i<count;i++){
	        temp1 = a.indexOf(b.get(i));
	        a.set(temp1,a.get(i));
	        a.set(i,b.get(i));
	    }
		System.out.println("Array after"+a);
	}
}