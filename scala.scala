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

    // val arr = Array(1, 2, 3,5,6,7,8)
    // val lst = List(7.2, 89)
    // val c = Vector.tabulate(10)(i => i*i)

    // // arr.foreach(println)

    // b.find(_ == 8)

    delayed(time())
  }

  def addInt(a: Int, b: Int): Int = {

    var sum: Int = 0

    sum = a + b

    return sum
  }

  def time() = {
    println("Getting time in nano seconds")

    System.nanoTime

  }
  def delayed(t: => Long) = {
    println("In delayed method")
    println("Param" + t)
  }

  def printStrings(args: String*) = {
    var i: Int = 0
    for (arg <- args) {
      println("Arg value[" + i + "] = " + arg)

      i += 1

    }
  }
}
