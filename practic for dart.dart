import 'dart:io';
import 'dart:math';

void main() {
  print("Калькулятор");
  print("1 - Арифметические операции");
  print("2 - Операции сравнения");
  
  stdout.write("Выберите (1 или 2): ");
  int choice = int.parse(stdin.readLineSync()!);
  
  // Арифметика
  if (choice == 1) {
    stdout.write("a = ");
    double a = double.parse(stdin.readLineSync()!);
    
    stdout.write("b = ");
    double b = double.parse(stdin.readLineSync()!);
    
    stdout.write("Операция (+ - * / ~/ % ^): ");
    String operation = stdin.readLineSync()!;
    
    if (operation == "+") {
      print("Результат: ${a + b}");
    } else if (operation == "-") {
      print("Результат: ${a - b}");
    } else if (operation == "*") {
      print("Результат: ${a * b}");
    } else if (operation == "/") {
      if (b == 0) {
        print("Ошибка: деление на ноль!");
      } else {
        print("Результат: ${a / b}");
      }
    } else if (operation == "~/") {
      if (b == 0) {
        print("Ошибка: деление на ноль!");
      } else {
        print("Результат: ${a ~/ b}");
      }
    } else if (operation == "%") {
      if (b == 0) {
        print("Ошибка: деление на ноль!");
      } else {
        print("Результат: ${a % b}");
      }
    } else if (operation == "^") {
      print("Результат: ${pow(a, b)}");
    } else {
      print("Не знаю такой операции");
    }
    
  // Сравнение
  } else if (choice == 2) {
    print('Выберите нужный режим');
    print('1- если сравнение: == равно != не равно');
    print('2- если сравнение: > больше < меньше');
    print('3- если сравнение:>= больше или равно <= меньше или равно');
    stdout.write('Введите число: ');
  int choiceOfCompare = int.parse(stdin.readLineSync()!);
  
  
  if (choiceOfCompare == 1) {
    stdout.write('Введите первое число: ');
    int a = int.parse(stdin.readLineSync()!);
    
    stdout.write('Введите второе число: ');
    int b = int.parse(stdin.readLineSync()!);
    
    if (a == b) {
      print('$a==$b, числа равны');
    } else if (a != b) {
      print('$a!=$b, числа не равны');
    }
    
  // Режим 2: > и <
  } else if (choiceOfCompare == 2) {
    stdout.write('Введите первое число: ');
    int a = int.parse(stdin.readLineSync()!);
    
    stdout.write('Введите второе число: ');
    int b = int.parse(stdin.readLineSync()!);
    
    if (a > b) {
      print('$a>$b, первое число больше второго');
    } else if (a < b) {
      print('$a<$b, первое число меньше второго');
    } else if (a == b) {
      print('ошибка, в данном режиме это не выполняется');
    }
    
  // Режим 3: >= и <=
  } else if (choiceOfCompare == 3) {
    stdout.write('Введите первое число: ');
    int a = int.parse(stdin.readLineSync()!);
    
    stdout.write('Введите второе число: ');
    int b = int.parse(stdin.readLineSync()!);
    
    if (a > b) {
      print('$a>$b, первое число больше второго');
    } else if (a < b) {
      print('$a<$b, первое число меньше второго');
    } else if (a == b) {
      print('$a==$b, числа равны');
    }
    
  } else {
    print('Не туда нажал, чел');
  }
    
  }
}