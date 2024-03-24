
public class MultipleThreads {

	private MultipleThreads() {
		System.out.println("starting multiple threads");
		for (int i=0; i < 10; i++) {
//			MyThread mt = new MyThread(i);
//			mt.start();
			Thread t = new Thread(new MyThread(i));
			t.start();
		}
		System.out.println("ending multiple threads");
	}

	public static void main(String [] args) {
		new MultipleThreads();
	}
}

class MyThread implements Runnable { //extends Thread {
	private int num;
	public MyThread(int num) {
		this.num = num;
	}

	public void run() {
		System.out.println("Thread " + num + " is running");
		System.out.println("Thread " + num + " line #2");
		System.out.println("Thread " + num + " is done");
	}
}