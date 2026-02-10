import 'dart:io';
import 'dart:math';

void main() {
  
  double num1;
  while (true) {
    print('Введите первое число:');
    try {
      num1 = double.parse(stdin.readLineSync()!);
      break;
    } catch (e) {
      print('Ошибка! Введите корректное число.');
    }
  }
  
  double num2;
  while (true) {
    print('Введите второе число:');
    try {
      num2 = double.parse(stdin.readLineSync()!);
      break;
    } catch (e) {
      print('Ошибка! Введите корректное число.');
    }
  }
  
  double sum = num1 + num2;
  print('$num1 + $num2 = $sum');
  
  double difference = num1 - num2;
  print('$num1 - $num2 = $difference');
  
  double product = num1 * num2;
  print('$num1 * $num2 = $product');
  
  if (num2 != 0) {
    double quotient = num1 / num2;
    print('$num1 / $num2 = $quotient');
  } else {
    print('$num1 / $num2 = Деление на ноль невозможно');
  }
  
  if (num2 != 0) {
    int intDivision = num1 ~/ num2;
    print('$num1 ~/ $num2 = $intDivision');
  } else {
    print('$num1 ~/ $num2 = Деление на ноль невозможно');
  }
  
  if (num2 != 0) {
    double remainder = num1 % num2;
    print('$num1 % $num2 = $remainder');
  } else {
    print('$num1 % $num2 = Деление на ноль невозможно');
  }
  
  num powerResult = pow(num1, num2);
  print('pow($num1, $num2) = $powerResult');
  
  bool isEqual = num1 == num2;
  print('$num1 == $num2 = $isEqual');
  
  bool isNotEqual = num1 != num2;
  print('$num1 != $num2 = $isNotEqual');
  
  bool isGreater = num1 > num2;
  print('$num1 > $num2 = $isGreater');
  
  bool isLess = num1 < num2;
  print('$num1 < $num2 = $isLess');
  
  bool isGreaterOrEqual = num1 >= num2;
  print('$num1 >= $num2 = $isGreaterOrEqual');
  
  bool isLessOrEqual = num1 <= num2;
  print('$num1 <= $num2 = $isLessOrEqual');
  
  if (num1 == num2) {
    print('Числа равны');
  } else if (num1 > num2) {
    print('Первое число ($num1) больше второго ($num2)');
  } else {
    print('Первое число ($num1) меньше второго ($num2)');
  }
}