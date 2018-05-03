
public class JavaHelloWorld {
	public static void main(String[] args) {
	int temp= 5;
	for (int i = 0; i < temp; i++) {
		System.out.println("This rocks! ");
	}
	private final AtomicLong count  = new AtomicLong();
	public long getCount() { return count.get();}

	public void service(ServetReuqest req, ServletResponse resp){
		BigInteger i = extractFromRequest(req);
		BigInteger[] factors = factor(i);
		count.incrementAndGet();
		encodeIntoResponse(resp, factors);	
	}

	
	}
}
