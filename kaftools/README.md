Here's some quick kafka tools.  I'm using Confluent Kafka which
differs from Apache Kafka in some command names, etc.

note: gradually moving everything to its own repo:
https://github.com/marhar/kafka

superkaf -- local instance laptop convenience 
=============================================

I'll roll this into kaft later.

Here's a quick tool that makes it handy to play with a local kafka
on a mac.

```
superkaf start
superkaf stop
```

starts and stops the zookeeper and kafa servers.  If you're in Terminal
on a Mac it does it in new tabs, nice and tidy.

```
superkaf status
superkaf help
```

gives the status (as best as I can tell), and gives some handy kafka
commands to get started.

Edit the file and set KAFDIR if you've got it installed in a different
place than me.
