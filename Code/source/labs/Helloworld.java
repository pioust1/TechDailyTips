/**
 * 
 */
package labs;

/**
 * @author pious.tiwari
 *
 */
import java.time.*;
public class Helloworld {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(" Hello "+args[0]+"\n");
		String a = " HELLO PIOUS  ";
		String c,d;
		System.out.println("a"+a+"\n");
		a = a.trim();
		/*String manipulation*/
		System.out.println("a"+a+"\n");
		a = a.concat(" why ");
		System.out.println("a"+a+"\n");
		/*left to right*/
		c="u"+1+1;
		System.out.println("c"+c+"\n");
		d=1+1+"u";
		System.out.println("d "+d+"\n");
		/*String Indexing*/
		int b=a.lastIndexOf('o');
		System.out.println("b"+b+"\n");
		
		/*String Builder*/
		
		StringBuilder sb = new StringBuilder();
		System.out.println("sb.capacity() "+sb.capacity());
		int stringCapacity = sb.capacity();
		System.out.println("stringCapacity "+stringCapacity);
		sb.insert(0,'h');
		System.out.println("stringCapacity "+stringCapacity);
		
		/*Method chaining*/
		
		String a1=a.concat(" hello !").substring(1,7);
		
		System.out.println("a1 "+a1);
		/*use of java time package*/
		LocalDateTime currentDateTime = LocalDateTime.now();
		System.out.println("currentDateTime "+currentDateTime);
		
	}

}
