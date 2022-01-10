import polyglotj.Polyglot;
import java.io.*;

class Main {
	public static void main(String[] argv) {
		try {
			Polyglot p = Polyglot.getInstance();
		} catch (IOException e) {
			System.out.println("IOError");
		}
	}
}
