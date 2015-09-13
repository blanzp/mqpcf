
# REST interface abstraction over MQSeries PCF

[MQ PCF] [1] is the administration API for MQSeries.  This is a [Flask Restful] [2] rest service that
 implements a [Swagger] [2] defined API.  The API can be tested using the included [Swagger UI] [4]. The code is generated 
 with [Swagger codegen] [5]

[1]: http://www-01.ibm.com/support/knowledgecenter/SSFKSJ_7.0.1/com.ibm.mq.csqzac.doc/pc10600_.htm?lang=en "PCF Commands" 
[2]: https://flask-restful.readthedocs.org/en/0.3.4/ "Flask Restful"
[3]: http://swagger.io "Swagger"
[4]: http://localhost:5000/static/swagger-ui/index.html "Swagger UI interface"
[5]: https://github.com/swagger-api/swagger-codegen "Swagger codegen"