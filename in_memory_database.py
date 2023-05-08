class InMemoryDatabase:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, columns):
        self.tables[table_name] = {
            'columns': columns,
            'rows': []
        }

    def insert(self, table_name, columns, values):
        if table_name not in self.tables:
            self.create_table(table_name, columns)
        else:
            existing_columns = self.tables[table_name]['columns']
            if columns != existing_columns:
                raise ValueError(f"Column mismatch in table {table_name}. Expected {existing_columns}, got {columns}.")
        row = dict(zip(columns, values))
        self.tables[table_name]['rows'].append(row)

    def update(self, table_name, set_clause, where_clause=None):
        rows = self.tables[table_name]['rows']
        for row in rows:
            if not where_clause or self.evaluate(where_clause, row):
                row.update(set_clause)

    def delete(self, table_name, where_clause=None):
        rows = self.tables[table_name]['rows']
        self.tables[table_name]['rows'] = [row for row in rows if not where_clause or not self.evaluate(where_clause, row)]

    def select(self, table_name, columns, where_clause=None, order_by_clause=None, limit_clause=None):
        if not columns:
            columns = self.tables[table_name]['columns']
        rows = self.tables[table_name]['rows']
        if where_clause:
            rows = [row for row in rows if self.evaluate(where_clause, row)]
        if order_by_clause:
            column, order = order_by_clause
            rows = sorted(rows, key=lambda row: row[column], reverse=(order == 'DESC'))
        if limit_clause:
            rows = rows[:limit_clause]
        result = [list(row[column] for column in columns) for row in rows]
        return result

    def evaluate(self, expression, row):
        op = expression.op
        if op == 'AND':
            return self.evaluate(expression.left, row) and self.evaluate(expression.right, row)
        elif op == 'OR':
            return self.evaluate(expression.left, row) or self.evaluate(expression.right, row)
        elif op == '=':
            return self.evaluate(expression.left, row) == self.evaluate(expression.right, row)
        elif op == '!=':
            return self.evaluate(expression.left, row) != self.evaluate(expression.right, row)
        elif op == '<':
            return self.evaluate(expression.left, row) < self.evaluate(expression.right, row)
        elif op == '>':
            return self.evaluate(expression.left, row) > self.evaluate(expression.right, row)
        elif op == '<=':
            return self.evaluate(expression.left, row) <= self.evaluate(expression.right, row)
        elif op == '>=':
            return self.evaluate(expression.left, row) >= self.evaluate(expression.right, row)
        elif op == 'IS NULL':
            return self.evaluate(expression.left, row) is None
        elif op == 'IS NOT NULL':
            return self.evaluate(expression.left, row) is not None
        else:
            return expression.value

