from lark import Lark

# Define SQL grammar
sql_grammar = """
       start: statement+

statement: select_statement
        | insert_statement
        | update_statement
        | delete_statement
        | create_table_statement
        | alter_table_statement
        | drop_table_statement
        | transaction_statement

select_statement: "SELECT" select_list "FROM" table_name join_clause? where_clause? group_by_clause? order_by_clause? limit_clause? end_statement

insert_statement: "INSERT INTO" table_name "(" column_name ("," column_name)* ")" "VALUES" "(" literal_value ("," literal_value)* ")" end_statement

update_statement: "UPDATE" table_name "SET" column_name "=" literal_value where_clause end_statement

delete_statement: "DELETE FROM" table_name where_clause end_statement

create_table_statement: "CREATE TABLE" table_name "(" column_definition ("," column_definition)* ")" end_statement

alter_table_statement: "ALTER TABLE" table_name add_column_statement end_statement

drop_table_statement: "DROP TABLE" table_name end_statement

transaction_statement: "TRANSACTION" "BEGIN" end_statement
                      | "TRANSACTION" "COMMIT" end_statement
                      | "TRANSACTION" "ROLLBACK" end_statement

join_clause: "JOIN" table_name "ON" join_condition

join_condition: column_name "=" column_name

where_clause: "WHERE" expression

group_by_clause: "GROUP BY" column_name ("," column_name)*

order_by_clause: "ORDER BY" column_name ("ASC" | "DESC")?

select_list: select_list_item ("," select_list_item)*

select_list_item: column_name

add_column_statement: "ADD" column_definition

column_definition: column_name data_type

data_type: "INT" | "VARCHAR" "(" SIGNED_INT ")" | "DATE"

table_name: CNAME

column_name: CNAME

literal_value: ESCAPED_STRING | SIGNED_INT

expression: column_name "=" literal_value

end_statement: ";"

limit_clause: "LIMIT" limit_value

limit_value: SIGNED_INT

%import common.CNAME
%import common.ESCAPED_STRING
%import common.SIGNED_INT
%import common.WS
%ignore WS


"""

parser = Lark(sql_grammar, start='start', parser='lalr', transformer=None)


# Create Lark parser
parser = Lark(sql_grammar, start='start', parser='lalr', transformer=None)

# Prompt user for SQL query
query = input("Enter a SQL query: ")

# Parse SQL query
try:
    parsed_query = parser.parse(query)
    print("Parsed query:", parsed_query.pretty())
except Exception as e:
    print("Error:", e)
