import java.io._
import scala.util.control._
import java.util.Date
import Array._

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

    // list of strings
    val fruit: List[String] = List("Apples", "oragnes", "pears")
    // list of integers
    val nums: List[Int] = List(1, 2, 3, 4)


    // println("head of fruit: " + fruit.tail)

    val fruit1 = "apples" :: ("oranges" :: ("pears" :: Nil))


    // println("Fruit: " +fruit)
    val fruit2 = "apples" :: ("oranges" :: ("pears" :: Nil))
    println("After reverse fuit: " + fruit.reverse)
    
  }

}

