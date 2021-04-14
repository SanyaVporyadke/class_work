import requests


#1 задание.
def find_max(li):
    return int(max(li))


def max_():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.json()['Valute']
    values = []
    for k, v in data.items():
        values.append(v["Value"])
        if int(v["Value"]) == find_max(values):
            return v["Name"]
    return values

# 2 задание.

class Rate:
    def __init__(self, format_='value', prev='value', diff=True):
        self.format = format_
        self.prev = prev
        self.diff = diff

    def exchange_rates(self):
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()["Valute"]
    def make_format(self, currency):
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]
            if self.format == 'value':
                return response[currency]['Value']
        return 'Error'
    def make_prev(self, prev):
        response = self.exchange_rates()
        if prev in response:
            if self.format == 'value':
                return response[prev]['Previous']
        return 'Error'
    def eur(self):
        if self.diff == True:
            return (self.make_prev('EUR') - self.make_format('EUR'))
    def usd(self):
        if self.diff == True:
            return (self.make_prev('USD') - self.make_format('USD'))
    def brl(self):
        if self.diff == True:
            return (self.make_prev('BRL') - self.make_format('BRL'))

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
print(response.text)

#3 задание

class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority

        self.grade = 1
    
    def grade_up(self):
        self.grade += 1

    def publish_grade(self):
        print(self.grade, self.grade)
    
    def check_if_it_is_time_for_upgrade(self):
        pass

class Designer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)
    
    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 2

        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()