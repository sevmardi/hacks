import java.io._
import scala.util.control._
class Point(val xc: Int, val yc: Int) {
  var x: Int = xc
  var y: Int = yc

  def move(dx: Int, dy: Int) {
    x = x + dx
    y = y + dy
    println("Point x location : " + x);
    println("Point y location : " + y);
  }
}

object Demo {
  def main(args: Array[String]) {

    val arr = Array(1, 2, 3)

    val lst = List(7.2,89)

    arr(0)

    
  }



}
