# ROS笔记
> 基础笔记见http://www.autolabor.com.cn/book/ROSTutorials/
## 【1】程序预配置流程
> 以新建一个名为ros_test的工作空间与名为demo的功能包为例<br>
另外，新建功能包以后需要执行以下流程7-12，更新功能包需要执行9-12
1. 新建一个名为ros_test的文件夹，并在其中新建一个名为src的文件夹
2. 执行下列代码：<br>
<code>cd ros_test<br>catkin_make
</code><br>
以创建工作空间
3. 执行下列代码：<br>
<code>cd ros_test<br>code .
</code><br>
以在此目录下打开vscode
4. ctrl+shift+B在vscode中进行ros系统编译
5. 在vscode文件目录中选定ros_test下的src右键选择create catkin package进行新建功能包，选择功能包名称并添加依赖。其中，基本依赖有roscpp，rospy，std_msgs等
6. 在功能包中新建scripts文件夹并在其中编写python文件（cpp文件放在功能包src中）
7. 配置Cmake文件：<br><code>
catkin_install_python(PROGRAMS scripts/自定义文件名.py<br>
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)</code><br>
需要将这段代码的自定义文件名.py改为你需要使用的文件，可以写好几个scripts/xx.py
8. 给python文件添加可执行权限，指令如下<br>
<code>cd ros_test/demo/scripts<br>
chmod +x *.py
</code><br>
9. 再次ctrl+shift+B在vscode中进行ros系统编译
10. 启动roscore，使用vscode则会自动启动
11. 声明环节变量文件，指令如下：<br>
<code>source ./devel/setup.bash
</code><br>
12. 使用rosrun或者roslaunch运行程序
## 【2】ROS节点通信
* **话题通信**
1. 注意接收方需要些<code>rospy.spin()</code>来循环调用回调函数，如果需要按频率发送，需要新建<code>rate=rospy.Rate</code>并使用<code>rate.sleep()</code>
2. 话题通信中断的异常标志函数名为<code>rospy.ROSInterruptException</code>
3. 如果先打开接收端，后打开发送端，则发送端在注册过程中可能已经开始发送信息而此时接收端无法接收导致丢失信息。可选的解决方法是在注册完成以后进行一小段延迟
4. ROS的python节点与cpp节点完全解耦合，在话题相同的情况下可以实现通信而不需要进行额外操作
5. 自定义数据类型的操作如下：<br>
   1. 在功能包文件夹中新建msg文件夹并新建自定义的xx.msg文件，随后修改package.xml中的<code><build_depend> <exec_depend></code>两项，分别添加<code>message_generation message_runtime</code>（一对一）<br>
    2. 修改cmake文件的<code>find_package</code>（依赖项）,添加<code>message_generation</code><br>
    3. 找到<code>add_message_files</code>处，将FILES以下的文件改为自己建立的msg文件名称<br>
    4. 将<code>generate_messages</code>的注释放开（上面所有修改都需要把注释放开）<br>
    5. 将<code>catkin_package</code>处的<code>CATKIN_DEPENDS</code>后面添加<code>message_runtime</code>并将这一行的注释打开即可进行编译<br>
    6. 找到生成的python中间文件，其路径在<code>工作空间/devel/lib/python3/dist-packages</code>处，获取该文件的绝对路径并打开vscode的setting.json，填到<code>python.autoComplete.extraPaths</code>处以获取自动补齐功能<br>
    7. 导包的时候<code>from 功能包.msg import msg文件名</code>作为新的数据类型（这导的包本身就是个数据类型！）
* **服务通信**
1. 服务端必须比客户端优先启动，客户端先启动会抛出异常标志函数名为<code>rospy.service.ServiceException</code>，除了异常处理以外也可以使用<code>client.wait_for_service()</code>或<code>rospy.wait_for_service("话题名")</code>来使得检测到没有服务端时客户端挂起
2. 添加与使用自定义数据载体srv文件与上面的自定义msg类似，不过新建的文件夹要变为srv，<code>add_message_files</code>要变为<code>add_service_files</code>，另外生成的中间文件在devel的srv文件夹中，其他一致；导包时使用<code>from 功能包.srv import *</code>，因为其内部包含服务端客户端等三种数据形式，分别引入很麻烦，不如直接用这种方式全部引入
* **参数服务器**
1. 由于底层使用RPC通信，不适合高速大量通信情况，最好适用于对静态数据的增删改查
2. 相对来说不需要复杂的自定义数据配置过程
* **常用指令**
> 以下指令是在ros系统启动以后的动态操作指令
1. rosnode：获取节点信息的指令，节点名是初始化的时候的名称而非文件名
2. rostopic：显示信息并进行信息交互
3. rosservice：用于显示和查询服务端的指令
4. rosmsg/rossrv：消息载体查询指令；查询自定义消息载体需要先进入工作空间
5. rosparam：在参数服务器上获取与设置参数
* **通信方式比较**<br>
> 参数服务器是一种数据共享机制，话题通信与服务通信是数据传递机制；参数服务器适用于对静态数据的增删改查；话题通信适用于连续高频的数据发布与接收；服务通信适用于偶尔调用执行某一项功能
## 【3】ROS通信机制进阶
* **常用API**
1. <code>init_node(name, argv=None, anonymous=False, log_level=None, disable_rostime=False, disable_rosout=False, disable_signals=False, xmlrpc_port=0, tcpros_port=0):</code><br>
作用是节点初始化，其详细参数如下：<br>
@param name: 节点名称，必须保证节点名称唯一，节点名称中不能使用命名空间(不能包含 '/')<br>
@argv: 封装节点时传递的参数，可以按照ros指定的语法格式传参，ros进行解析与使用<br>
@anonymous: 取值为 true 时，为节点名称后缀随机编号，目的是为了可以使得一个节点启动多次<br>
2. <code>class Publisher(Topic):<br>
    def __init__(self, name, data_class, subscriber_listener=None, tcp_nodelay=False, latch=False, headers=None, queue_size=None):</code><br>
话题通信发布方API；重点关注latch参数，如果为 true,该话题发布的最后一条消息将被保存，并且后期当有订阅者连接时会将该消息发送给订阅者<br>
3. <code>rospy.spin()</code>：不断循环执行前面的代码，不会执行到此函数后的代码
4. 时间相关API
   * 基准起始时刻：1970-1-1 00:00
   * to_sec是浮点数，secs是整型(秒数)，to_nsec是纳秒数
   * <code>rospy.Time(1234,567891011)=rospy.Time(1234.567891011)</code>，前者逗号后面的值就是小数点后的数据；time类型有两个数据，分别为sec和nsec；如果使用<code>rospy.Time.from_sec</code>，则此函数仅有一个传入参数，即sec。实际上这两个函数用法差不多，都是用于创建时间对象
   * <code>t = rospy.Duration(5)<br>
    rospy.sleep(t)</code><br>
    实现程序休眠五秒；另外，time和duration可以实现加减法，duration和duration也可以加减，但time和time之间不能进行加减运算
   * <code>r = rospy.Rate(5)<br>
    r.sleep()</code><br>sleep写在循环里，rospy会尽可能让循环频率为5HZ而自适应修改延迟
   * 定时器<code>rospy.Timer(period, callback, oneshot=False, reset=False)：</code><br>
   period：写duration，使得时隔x秒执行一次回调函数<br>
   callback：回调函数（不写括号）；回调函数自带一个event属性(<code>callback(event)</code>)，event属性包含一些与执行回调函数时的时间相关的属性<br>
   oneshot：True时定时器为一次性
5. 其他函数
    * 节点状态判断：<code>rospy.is_shutdown()</code>，返回布尔值
    * 节点关闭指令：<code>rospy.signal_shutdown(reason)</code>，
    reason是一个字符串，可以提示函数关闭的原因；
    * <code>rospy.on_shutdown(h)</code>，也是节点关闭指令，但是关闭时会执行h回调函数（此函数不能传参）
    * 日志信息输出：loginfo白色，logwarn黄色，logerr和logfatal红色
  * **python模块导入**<br>rosrun的默认执行路径不是功能包的scripts目录而是工作空间路径，故需要使用<code>path = os.path.abspath(".")<br>
sys.path.insert(0,path + "/src/功能包名称/scripts")</code>把参考路径转到脚本文件夹里
## 【4】ROS运行管理
* **元功能包**<br>
> 进行项目封装的时候需要作为目录使用以便于用户安装
* **launch文件**
1. launch标签：是所有launch文件的根标签
2. node标签：指定ROS节点
3. include标签：在launch文件中引入其他的launch文件
4. remap标签：用于话题重命名，写在node节点的头尾之间位置
5. param标签：在参数服务器上设置参数；写在launch标签中间和node标签中间有区别，在node标签中间时name会包含命名空间，变为<code>/节点名/参数名</code>
6. rosparam标签：从YAML导入参数或将参数导出到YAML文件，写在node标签中时也会包含私有命名空间
7. group标签：可以把节点归于某个命名空间，除了launch标签以外的最高级标签，写在此标签中的节点全部包含此标签的命名空间前缀
8. arg标签：适用于传参，设定一个arg并在下面的节点启动使用arg，修改arg参数值等于修改所有传参位置
* **工作空间覆盖**
> 指在不同工作空间中存在同名功能包的情况或自定义功能包与系统内置功能包重名
1. 如果在bashrc文件中刷新了多个环境变量，则后配置的具有更高的优先级，调用时优先调用
2. 最好尽量避免出现工作空间覆盖的情况
* **节点名称重名**
> 解决方法是命名空间（加前缀）或者名称重映射（起别名）
1. rosrun命令
    * 添加命名空间：<code>rosrun 功能包 文件名 __ns:=/xxx</code>
    * 名称重映射：<code> rosrun 功能包 文件名 __name:=新名称</code>
    * 以上两者方式可以叠加使用
2. launch文件
    * 直接改node标签的ns和name即可；也可以使用group标签修改命名空间
3. node_init时写作<code>rospy.init_node(节点名,anonymous=True)</code>，会在节点名称后缀时间戳
* **话题名称设置**
1. rosrun命令：<code>rorun 包名 文件名 话题名:=新话题名称</code>
2. launch文件：remap标签进行话题重命名
> 话题可以分为三类：全局（<code>/话题名</code>），相对（<code>/命名空间/话题名</code>），私有（<code>/命名空间/节点名/话题名</code>）在自定义话题时，/开头的话题为绝对话题，无开头符号的是相对话题，~开头的是私有话题
* **参数名称设置**
> 不能重映射，只能添加命名空间
1. rosrun方式：<code>rosrun 包名 文件名 _参数名:=参数值</code>，参数为私有模式
2. launch文件：使用param标签，根据位置可以设为不同的类型
3. 代码内set_param时根据前缀不同可以设为不同类型，前缀与话题的前缀相同
* **分布式通信**
1. 保证设备处于同一网络中并最好固定IP（如果不知道怎么设置就ifconfig看一下随机分配的IP，直接填到IP地址位置），虚拟机网络调为桥接模式
2. 修改不同计算机的<code>/etc/hosts</code> 文件，在该文件中加入其他设备的IP地址和设备名（设备名可以使用hostname指令查看），之后最好进行设备重启；使用<code>ping ip</code>或<code>ping 设备名</code>可以测试通信是否正常
3. bashrc文件中配置主从机ip，启动roscore的设备是主机；<br>
主机在bashrc中添加<code>export ROS_MASTER_URI=http://~~主机IP~~:11311<br>
export ROS_HOSTNAME=~~主机IP~~
</code><br>
从机在bashrc中添加<code>export ROS_MASTER_URI=http://~~主机IP~~:11311<br>
export ROS_HOSTNAME=~~从机IP~~
</code><br>
4. 在主机启动roscore，进行通信测试即可
## 【5】ROS常用组件
* **TF坐标变换**
1. 坐标msg消息
    * 坐标系：偏移量表示平动；四元数表示坐标系姿态，和欧拉角起到类似的作用
    * 坐标点：三轴坐标
2.  静态坐标变换：两个坐标系的相对位置固定
    * 发布方：发布两个坐标系的相对关系；**header里写父坐标系**；四元数通过对欧拉角进行转换来获取，只有此函数是tf，其他函数都是tf2包里的
    * 接收方：传入被转换的坐标点并进行转换（**将子坐标系的坐标点转换为父坐标系的坐标点**）；仍旧可能出现接收方先打开而发布方为开始，解决方法是给延迟或使用try来异常处理
    * 可以使用预设程序完成此功能<code>rosrun tf2_ros static_transform_publisher x偏移量 y偏移量 z偏移量 z偏航角度 y俯仰角度 x翻滚角度 父级坐标系 子级坐标系</code>，此方案更简单
    * 可以使用rviz工具进行坐标变换可视化
3. 动态坐标变换：两个坐标系的相对位置变化
    * 发布方参数为变化值
    * 发布与接收方的时间戳隔得太远，ros系统会报错；将坐标点程序时间戳设置为0可以让ros认为时间不重要从而不报错
4. 多坐标变换：s1（子）——w（父）——s2（子）坐标系的变换关系已知，此时已知s1系内点的坐标，求其在s2坐标系内的坐标
    * 调用时还是写s1系与s2系，中间的转换ros系统内部完成
5. 坐标系关系查看
    * rviz进行图形化显示
    * tf2_tools生成包含坐标系树形结构的pdf文件；启动坐标系的发布方后运行<code>rosrun tf2_tools view_frames.py</code>，其会监听已经发布的坐标变换并在当前路径下生成pdf文件
* **rosbag**
> 实现数据的留存与读取
1. 命令行实现：<code>rosbag record -a -O 目标文件</code>，目标文件是bag文件的文件名；保存了roscore里录制期间的所有topic消息；<code>rosbag play 文件名
</code>可以重放topic消息。修改-a等可以实现订阅指定节点等功能
2. py文件内使用rosbag包也可以实现实时数据的存储与读取（写入时可以按照指定话题存入，读取也可以按照指定话题读取）
* **rqt工具箱**
> 使用基于QT的图形化操作代替命令行来调用工具，即【ROS QT】；命令行直接键入rqt即可启动
## 【6】机器人系统仿真
> 包含URDF机器人建模、Gazebo创建仿真环境、Rviz感知环境等部分


