package prog7;
import java.util.*;
public interface resume{
	public void biodata();
}
class teacher implements resume
{
	String name,qual,gen,add,mail,exp;
	int mob;
	public void biodata()
	{
		Scanner s1=new Scanner(System.in);
		System.out.print("Name");
		name=s1.next();
		System.out.print("qualification");
		qual=s1.next();
		System.out.print("gender");
		gen=s1.next();
		System.out.print("address");
		add=s1.next();
		System.out.print("mail id");
		mail=s1.next();
		System.out.print("mob no");
		mob=s1.nextInt();
		System.out.print("experience");
		exp=s1.next();
		System.out.print(" ");
		System.out.print("*******************************");
		System.out.print("     biodata-teacher    ");
		System.out.print("********************************");
		System.out.print("-----------------------------------");
		System.out.print("name  |:"+name );
		System.out.print("qualification   |:"+qual);
		System.out.print("gender    |:"+gen);
		System.out.print("address|:"+add);
		System.out.print("mail id   |:"+mail);
		System.out.print("mobno   |:"+mob);
		System.out.print("experrs |:"+exp);
		System.out.print("**************************** ");
	}
}
class student implements resume
{
	String name,res,des,sec,gen,add;
	int rollno;
	public void biodata()
	{
		Scanner s1=new Scanner(System.in);
		System.out.print("Name");
		name=s1.next();
		System.out.print("result");
		res=s1.next();
		System.out.print("gender");
		gen=s1.next();
		System.out.print("address");
		add=s1.next();
		System.out.print("section");
		sec=s1.next();
		System.out.print("desciplain");
		des=s1.next();
		System.out.print("rollno");
		rollno=s1.nextInt();
		System.out.print(" ");
		System.out.print("*******************************");
		System.out.print("     biodata-student    ");
		System.out.print("********************************");
		System.out.print("-----------------------------------");
		System.out.print("Name   |:"+name);
		System.out.print("result    |:"+res);
		System.out.print("gender   |:"+gen);
		System.out.print("address    |:"+add);
		System.out.print("section     |:"+sec );
		System.out.print("descpline    |:"+des);
		System.out.print("--------------------------- ");
	}
}
class prog7
{
				public static void main(String args[])
				{
				student stud=new student();
				teacher teach=new teacher();
				Scanner s2=new Scanner(System.in);
				System.out.print("1:student ");
				System.out.print("2;teacher ");
				System.out.print("enter your choice ");
				int choice=s2.nextInt();
				switch(choice)
				{
				case 1: stud.biodata();
				       break;
				case 2: teach.biodata();
				       break;
				 default:System.out.print("invalid choice ");
				}
				}
}
				
			
		
	

