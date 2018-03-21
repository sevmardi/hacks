object Demo {


	def main(args : Array[String]){


		var list1 = range(1,10)
		var list2 = range(10,20)

		
		val seq = List.tabulate(6)(n => n * n)

		println("seq:" + seq)

		val mul = List.tabulate(4,5)(_ * _)
		println("mul: " + mul)

		



	}




}