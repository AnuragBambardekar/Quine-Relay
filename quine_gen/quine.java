public class quine {
 public static void main(String[] args) {
  String[] data = {
 "public class quine {",
 " public static void main(String[] args) {",
 "  String[] data = {",
 "  };",
 "  int boundary = 3;",
 "  int a = 0; int b = boundary; int c = data.length;",
 "  char quote = (char) 34; char space = (char) 32; char separator = (char) 44;",
 "  for (int k = a; k < b; k++)",
 "    System.out.println(data[k]);",
 "  for (String line : data)",
 "    System.out.println(String.valueOf(space) + quote + line + quote + separator);",
 "  for (int k = b; k < c; k++)",
 "    System.out.println(data[k]);",
 " }",
 "}",
  };
  int boundary = 3;
  int a = 0; int b = boundary; int c = data.length;
  char quote = (char) 34; char space = (char) 32; char separator = (char) 44;
  for (int k = a; k < b; k++)
    System.out.println(data[k]);
  for (String line : data)
    System.out.println(String.valueOf(space) + quote + line + quote + separator);
  for (int k = b; k < c; k++)
    System.out.println(data[k]);
 }
}
