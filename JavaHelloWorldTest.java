
public class JavaHelloWorldTest {

	@Test(expceted=UnsupportedOperationException.class)
	public void showImmutabilityAdd() throws Exception {
		List<Integer> inlist = List.of(1,2,3);
		inlist.add(99);
		
	}
}