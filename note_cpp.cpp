/**********************************************
 * C++ 基础语法记录                            
 * 来自balmung（https://github.com/balmung08） 
 * 主要内容来自菜鸟教程                         
 * //这是一条注释实例                           
 **********************************************/

// 头文件引用引用
#include <iostream>
#include <stdio.h>
#include <limits>
//使用standard命名空间，命名空间后面详述
using namespace std;

//变量数据类型
char c;                           //signed char,unsigned char
int i;                            //unsigned/signed and short/long int自由组合
float f;                          //精度型
double b;                         //双精度型
wchar_t w;                        //宽字节，可放2or4个字节

//数据类型具体性质展示函数
int variable_status()  
{  
    cout << "type: \t\t" << "************size**************"<< endl;  
    cout << "bool: \t\t" << "所占字节数：" << sizeof(bool);  
    cout << "\t最大值：" << (numeric_limits<bool>::max)();  
    cout << "\t\t最小值：" << (numeric_limits<bool>::min)() << endl;  
    cout << "char: \t\t" << "所占字节数：" << sizeof(char);  
    cout << "\t最大值：" << (numeric_limits<char>::max)();  
    cout << "\t\t最小值：" << (numeric_limits<char>::min)() << endl;  
    cout << "signed char: \t" << "所占字节数：" << sizeof(signed char);  
    cout << "\t最大值：" << (numeric_limits<signed char>::max)();  
    cout << "\t\t最小值：" << (numeric_limits<signed char>::min)() << endl;  
    cout << "unsigned char: \t" << "所占字节数：" << sizeof(unsigned char);  
    cout << "\t最大值：" << (numeric_limits<unsigned char>::max)();  
    cout << "\t\t最小值：" << (numeric_limits<unsigned char>::min)() << endl;  
    cout << "wchar_t: \t" << "所占字节数：" << sizeof(wchar_t);  
    cout << "\t最大值：" << (numeric_limits<wchar_t>::max)();  
    cout << "\t\t最小值：" << (numeric_limits<wchar_t>::min)() << endl;  
    cout << "short: \t\t" << "所占字节数：" << sizeof(short);  
    cout << "\t最大值：" << (numeric_limits<short>::max)();  
    cout << "\t\t最小值：" << (numeric_limits<short>::min)() << endl;  
    cout << "int: \t\t" << "所占字节数：" << sizeof(int);  
    cout << "\t最大值：" << (numeric_limits<int>::max)();  
    cout << "\t最小值：" << (numeric_limits<int>::min)() << endl;  
    cout << "unsigned: \t" << "所占字节数：" << sizeof(unsigned);  
    cout << "\t最大值：" << (numeric_limits<unsigned>::max)();  
    cout << "\t最小值：" << (numeric_limits<unsigned>::min)() << endl;  
    cout << "long: \t\t" << "所占字节数：" << sizeof(long);  
    cout << "\t最大值：" << (numeric_limits<long>::max)();  
    cout << "\t最小值：" << (numeric_limits<long>::min)() << endl;  
    cout << "unsigned long: \t" << "所占字节数：" << sizeof(unsigned long);  
    cout << "\t最大值：" << (numeric_limits<unsigned long>::max)();  
    cout << "\t最小值：" << (numeric_limits<unsigned long>::min)() << endl;  
    cout << "double: \t" << "所占字节数：" << sizeof(double);  
    cout << "\t最大值：" << (numeric_limits<double>::max)();  
    cout << "\t最小值：" << (numeric_limits<double>::min)() << endl;  
    cout << "long double: \t" << "所占字节数：" << sizeof(long double);  
    cout << "\t最大值：" << (numeric_limits<long double>::max)();  
    cout << "\t最小值：" << (numeric_limits<long double>::min)() << endl;  
    cout << "float: \t\t" << "所占字节数：" << sizeof(float);  
    cout << "\t最大值：" << (numeric_limits<float>::max)();  
    cout << "\t最小值：" << (numeric_limits<float>::min)() << endl;  
    cout << "size_t: \t" << "所占字节数：" << sizeof(size_t);  
    cout << "\t最大值：" << (numeric_limits<size_t>::max)();  
    cout << "\t最小值：" << (numeric_limits<size_t>::min)() << endl;  
    cout << "string: \t" << "所占字节数：" << sizeof(string) << endl;  
    // << "\t最大值：" << (numeric_limits<string>::max)() << "\t最小值：" << (numeric_limits<string>::min)() << endl;  
    cout << "type: \t\t" << "************size**************"<< endl;  
    return 0;  
}

typedef int num;                  //typedef取别名 使用num当作int的别名使用

//enum枚举，使得变量名称只能在规定的值范围内选取;此时变量的值只能是整数
int enum_test()
{
    enum color{ 
        red, blue=5, green
    } test_variable;
    // 默认值从0开始依次加1,未定义时在前一个基础上加1;此时r=0,b=5,g=6
    test_variable = red;                   //此处不再用定义变量类型
    printf("red:%d\n",test_variable);
    test_variable = blue;         
    printf("blue:%d\n",test_variable);
    test_variable = green;         
    printf("green:%d\n",test_variable);
    return 0;
}

//数据类型转换
int variablie_cast()
{   // 静态转换是将一种数据类型的值强制转换为另一种数据类型的值。
    // 静态转换通常用于比较类型相似的对象之间的转换，例如将 int 类型转换为 float 类型。
    // 静态转换不进行任何运行时类型检查，因此可能会导致运行时错误。
    int i = 1;
    float n = static_cast<float>(i); // 静态将int类型转换为float类型
    printf("int1静态转换为float:%f\n",n);
    // 动态转换通常用于将一个基类指针或引用转换为派生类指针或引用。
    // 动态转换在运行时进行类型检查，如果不能进行转换则返回空指针或引发异常。
    // Derived* ptr_derived = dynamic_cast<Derived*>(ptr_base); 
    printf("动态转换一直报错故忽略实例\n");
    // 常量转换可将常量转换为变量,即去掉其只读属性
    const int a = 10;
    int r = const_cast<int&>(a); // 常量转换，将const int转换为int 
    printf("常量10的解锁与加1:%d\n",++r);
    // 重新解释转换完全不进行检查且范围极广,甚至可以把变量转换为指针,最不安全!
    int c = 10;
    float d = reinterpret_cast<float&>(c); // 重新解释将int类型转换为float类型
    printf("int10重解释转换为float:%f,宏观上与静态表现相同,但其转换范围更大\n",d);
    return 0;
}

//常量处理
int const_test()
{   //常量前缀指定基数：0x 或 0X 表示十六进制，0 表示八进制，不带前缀则默认表示十进制
    //常量后缀U表示无符号整数，L表示长整数;后缀可大写可小写，U和L的顺序任意
    //部分转义字符表见目录下图片
    //浮点常量由整数部分、小数点、小数部分和指数部分组成;3.14159实际上等于314159E-5L
    float f = 314159E-5L;
    cout << "指数形式小数测试输出:" << f << endl;
    //字符串使用"",与python不同,cpp的字符串不能作为变量;'\'可把一个很长的字符串常量进行分行
    string greeting = "hello,\
                        runoob";
    cout << greeting << endl;
    printf("%s\n",greeting.c_str());  //printf的%s不能直接输出,需要使用c_str进行转换才能使用
    //定义常量的两种方式:const与define
    //const给变量赋予只读,修改时报错;define在后面变量定义时若与常量重名时直接报错
    const int i = 1;
    #define var_test 10
    cout << i << ' ' << var_test << endl;
    return 0;
}

//static存储类
//static修饰局部变量时,可以在函数调用之间保持局部变量的值
//static修饰全局变量时,会使变量的作用域限制在声明它的文件内
//static用在类数据成员上时，static修饰的变量先于对象存在,故它需要在类外部先进行初始化

//extern存储类
//如果变量的使用在定义以前，可以使用extern预先声明
//另外如果在另外一个文件中建立函数与全局变量,不需要include即可使用extern声明后直接调用

//运算符
// &&,||,!为逻辑与或非;&,|,~为位运算与或非,^为位异或
// 算术运算符,赋值运算符,杂项运算符与运算符优先级见图片

//循环,判断与函数定义这些程序基础结构完全与C语言一致

//数学计算:需要引入特殊头文件,计算函数见图
#include <cmath>
int math_test ()
{
   //数字定义
   short  s = 10;
   int    i = -1000;
   long   l = 100000;
   float  f = 230.47;
   double d = 200.374;
   //数学运算
   cout << "sin(d) :" << sin(d) << endl;
   cout << "abs(i)  :" << abs(i) << endl;
   cout << "floor(d) :" << floor(d) << endl; 
   cout << "sqrt(f) :" << sqrt(f) << endl;
   cout << "pow( d, 2) :" << pow(d, 2) << endl;
   return 0;
}

//数组也和C语言相同
#include <iomanip> //用于引入setw函数
int num_group()
{
   int n[ 10 ]; // n 是一个包含 10 个整数的数组
   // 初始化数组元素          
   for ( int i = 0; i < 10; i++ )
   {
      n[ i ] = i + 100; 
   }
   //setw函数用于设置宽度,如果后面的字符或数字宽度大于设定值则无视,若小于则补空格到预定宽度
   cout << "Element" << setw( 13 ) << "Value" << endl;
   // 输出数组中每个元素的值                     
   for ( int j = 0; j < 10; j++ )
   {
      cout << setw( 7 )<< j << setw( 13 ) << n[ j ] << endl;
   }
   return 0;
}

//字符串
//可以按照C语言的字符数组思路进行操作,也可以使用C++带有的STR操作函数,需要引入头文件
#include <cstring>
int str_test ()
{
    char site[7] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    cout << site << '\n';
    cout << site[1] << endl;

    char str1[13] = "runoob";
    char str2[13] = "google";
    char str3[13];
    int  len ;
    // 复制 str1 到 str3
    strcpy( str3, str1);
    cout << "strcpy( str3, str1) : " << str3 << endl;
    // 连接 str1 和 str2
    strcat( str1, str2);
    cout << "strcat( str1, str2): " << str1 << endl;
    // 连接后，str1 的总长度
    len = strlen(str1);
    cout << "strlen(str1) : " << len << endl;
    //strcmp用于比较字符串是否相同
    //strchr用于指向字符串中字符第一次出现的位置
    //strstr用于指向字符串中字符串第一次出现的位置
    return 0;
}

//指针也与C语言中一致
int point()
{
   int  var = 20;   // 实际变量的声明
   int  *ip;        // 指针变量的声明
   ip = &var;       // 在指针变量中存储 var 的地址
   cout << "Value of var variable: ";
   cout << var << endl;
   // 输出在指针变量中存储的地址
   cout << "Address stored in ip variable: ";
   cout << ip << endl;
   // 访问指针中地址的值
   cout << "Value of *ip variable: ";
   cout << *ip << endl;
   return 0;
}

//引用:相当于给某个地址除了变量名以外赋予第二个标签
int reference ()
{
   // 声明简单的变量
   int    i;
   double d;
   // 声明引用变量,即在后面使用&符号
   int&    r = i;
   double& s = d;
   i = 5;
   cout << "Value of i : " << i << endl;
   cout << "Value of i reference : " << r  << endl;
   d = 11.7;
   cout << "Value of d : " << d << endl;
   cout << "Value of d reference : " << s  << endl;
   return 0;
}

//输入与输出,分为cin,cout,cerr与clog
//在小型项目中并不重要,但在大型程序中非常需要注意输出的区分
int out_test()
{   
    char name[50];
    cin >> name;
    cout << "out message:" << name << endl;
    cerr << "Error message:" << name << endl;
    clog << "log message:" << name << endl;
    return 0;
}

//结构体,基本规则与C语言相同
int struct_test()
{
    struct Books
    {
    char  title[50];
    char  author[50];
    char  subject[100];
    int   book_id;
    };
    Books Book1;        // 定义结构体类型 Books 的变量 Book1
    Books Book2;        // 定义结构体类型 Books 的变量 Book2
    // Book1 详述
    strcpy( Book1.title, "C++ 教程");
    strcpy( Book1.author, "Runoob"); 
    strcpy( Book1.subject, "编程语言");
    Book1.book_id = 12345;
    // Book2 详述
    strcpy( Book2.title, "CSS 教程");
    strcpy( Book2.author, "Runoob");
    strcpy( Book2.subject, "前端技术");
    Book2.book_id = 12346;
    // 输出 Book1 信息
    cout << "第一本书标题 : " << Book1.title <<endl;
    cout << "第一本书作者 : " << Book1.author <<endl;
    cout << "第一本书类目 : " << Book1.subject <<endl;
    cout << "第一本书 ID : " << Book1.book_id <<endl;
    // 输出 Book2 信息
    cout << "第二本书标题 : " << Book2.title <<endl;
    cout << "第二本书作者 : " << Book2.author <<endl;
    cout << "第二本书类目 : " << Book2.subject <<endl;
    cout << "第二本书 ID : " << Book2.book_id <<endl;
    return 0;
}

//类(对象)
//演示类的定义,类成员函数,类访问修饰符,类的派生;构造函数与析构函数,友元函数

//类的定义与类成员函数定义
class Box
    {
        public:
            double length;   //长度
            double breadth;  //宽度
            double height;   //高度
            //成员函数声明
            double get(void);
            void set( double len, double bre, double hei );
    };         
double Box::get(void)  //成员函数定义
    {
        return length * breadth * height;
    }
void Box::set( double len, double bre, double hei) //成员函数定义
    {
        length = len;
        breadth = bre;
        height = hei;
    }
int object_init()
{
    Box Box1;        // 声明 Box1，类型为 Box
    double volume = 0.0;     // 用于存储体积
    // box 1 详述
    Box1.height = 5.0; 
    Box1.length = 6.0; 
    Box1.breadth = 7.0;
    // box 1 的体积
    volume = Box1.height * Box1.length * Box1.breadth;
    cout << "Box1 的体积：" << volume <<endl;
    Box1.set(16.0, 8.0, 12.0);
    volume = Box1.height * Box1.length * Box1.breadth;
    cout << "Box1 的体积：" << volume <<endl;
    return 0;
}

//成员访问修饰符
//public:共有成员在函数外部可以使用类似S.x直接进行访问和定义
//private:私有变量与函数在类的外部仅通过友元函数才能访问;不指定修饰的变量与函数都默认私有
//protected:与私有性质相似,但是受保护的变量在派生类中可以访问

//类的派生与继承
class Box
{
    protected:
        double width;
};
class SmallBox:Box // SmallBox 是派生类
{
    public:
        void setSmallWidth( double wid );
        double getSmallWidth( void );
};

//构造函数与析构函数
//构造函数名称与类名称完全相同且没有任何返回,在创建类时自动执行;通常用于给变量设初值
//析构函数是在构造函数名前加~,在删除类时自动执行,有助于在跳出程序前释放资源
class Line
{
   public:
      void setLength( double len );
      double getLength( void );
      Line();   // 这是构造函数声明
      ~Line();  // 这是析构函数声明
   private:
      double length;
};
Line::Line(void)//构造函数
{
    cout << "Object is being created" << endl;
}
Line::~Line(void)//析构函数
{
    cout << "Object is being deleted" << endl;
}

//友元函数
//类的友元函数是定义在类外部，但有权访问类的所有私有成员和保护成员
//尽管友元函数的原型有在类的定义中出现过，但是友元函数并不是成员函数
class Box
{
    double width;//此处width是默认的private
    public:
        friend void printWidth( Box box );
        void setWidth( double wid );
};
void Box::setWidth( double wid )
{
    width = wid;//可以使用私有成员
}


int main()
{
    return 0;
}
