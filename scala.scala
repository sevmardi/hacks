import java.io._
import scala.util.control._
class Point(val xc: Int, val yc: Int)
{
	var x: Int = xc
	var y: Int = yc

	def move(dx: Int, dy: Int) {
		x = x + dx
		y = y + dy
		println ("Point x location : " + x);
		println ("Point y location : " + y);
	}
}

object Demo {
	def main(args: Array[String]) {
		
		var a = 10;
		var b = 0;
		val numlist = List(1,2,3,4,5)

		val loop = new Breaks;
		loop.breakable{

			for (a <- numlist)
			{
				println("value of a: " + a)
				if (a == 4)
					loop.break;

			}
		}

	}
}
