/*
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <mysql/mysql.h>
#include <time.h>
#include <math.h>
*/
#include "thread_temp.h"
#define DBHOST "localhost"
#define DBUSER "root"
#define DBPASS "YOURPASSWORD"
#define DBNAME "demofarmdb"

MYSQL *connector;
MYSQL_RES *result;
MYSQL_ROW row;

int send_db(int temp)
{
  // MySQL connection
  connector = mysql_init(NULL);
  if (!mysql_real_connect(connector, DBHOST, DBUSER, DBPASS, DBNAME, 3306, NULL, 0))
  {
    fprintf(stderr, "%s\n", mysql_error(connector));
    return 0;
  }

  printf("MySQL(rpidb) opened.\n");
  char query[1024];
  sprintf(query,"insert into tempdata(data, regdate) values(%d, now())",temp);

  if(mysql_query(connector, query))
  {
	  fprintf(stderr, "%s\n", mysql_error(connector));
	  printf("Write DB error\n");
  }
  delay(1000); //1sec delay

  mysql_close(connector);

  return 0;
}




