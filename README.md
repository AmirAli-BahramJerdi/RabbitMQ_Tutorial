![RabbitMQ Logo](https://www.rabbitmq.com/img/rabbitmq-logo-with-name.svg)
# MessageBroker_RabbitMQ
this is RabbitMQ tutorial with python, step by step of documentation.



## ***Do the following steps in order for "Hello world"***

![RabbitMQ Logo](https://solace.com/wp-content/uploads/2015/10/mapping-amqp-to-solace_1.png)





- activate the virtual environment

```bash
  source venv/bin/activate
```
- Install requirements

```bash
  pip install -r requirements.txt
```

- create an admin that username='root' and password='root'
```bash
  sudo rabbitmqctl add_user "root" "root"   
```
## Listing queues
You may wish to see what queues RabbitMQ has and how many messages are in them. You can do it (as a privileged user) using the rabbitmqctl tool:

```bash
  sudo rabbitmqctl list_queues   
```

On Windows, omit the sudo:
```bash
  rabbitmqctl.bat list_queues
```

 
- Change directory to Hello World

```bash
  cd HelloWorld/  
```

 
- run sender.py and reciever in two separate terminals

```bash
  python sender.py
```

```bash
  python reciever.py
```



## Source/Documentation

[RabbitMQ](https://www.rabbitmq.com/)

[pika](https://pika.readthedocs.io/en/stable/)




## Author

- [@Amirali-Bahramjerdi](https://github.com/AmirAli-BahramJerdi)

# ***Hope to enjoy it :)***