![RabbitMQ Logo](https://www.rabbitmq.com/img/rabbitmq-logo-with-name.svg)
# MessageBroker_RabbitMQ
this project is a simple test to send and recieve a message with a qeue 



## ***Do the following steps in order***

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

- give the user 'root' administrator permission
```bash
  sudo rabbitmqctl set_user_tags root administrator 
```


- give the user 'root' virtual host access (/)
```bash
  sudo rabbitmqctl set_permissions -p / root ".*" ".*" ".*" 
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