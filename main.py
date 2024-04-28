import json
import pickle
import gzip


class OrderProcessingService:
    def __init__(self):
        self.data_to_export = {
            "order_id": 12345,
            "customer_name": "John Doe",
            "items": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1},
                {"product_id": 3, "quantity": 3}
            ],
            "total_price": 100.50
        }

    def export_data_to_json(self):
        with open("order_data.json", "w") as json_file:
            json.dump(self.data_to_export, json_file)
        print("Дані експортовано успішно.")

    def process_order_data(self):
        with open("order_data.json", "r") as json_file:
            data = json.load(json_file)

        print("Замовлення ID:", data["order_id"])
        print("Ім'я клієнта:", data["customer_name"])
        print("Товари:")
        for item in data["items"]:
            print("  - Товар ID:", item["product_id"], "| Кількість:", item["quantity"])
        print("Загальна вартість:", data["total_price"])


order_service = OrderProcessingService()
order_service.export_data_to_json()
order_service.process_order_data()


# Завдання 2
class Survey:
    def __init__(self, survey_name, questions):
        self.survey_name = survey_name
        self.questions = questions

    def conduct_survey(self):
        print("===", self.survey_name, "===")
        answers = {}
        for question in self.questions:
            answer = input(question + " ")
            answers[question] = answer
        return answers

    def save_survey_results(self, answers):
        file_name = self.survey_name.replace(" ", "_").lower() + "_results.json"
        with open(file_name, "a") as file:
            json.dump(answers, file)
            file.write("\n")
        print("Результати опитування збережено у файлі", file_name)


survey_name = "Спільнота користувачів OpenAI"
questions = [
    "Як ви оцінюєте ваш досвід використання OpenAI?",
    "Які можливості ви хотіли б бачити у майбутніх версіях OpenAI?",
    "Чи берете ви участь у спільноті OpenAI на форумах або в інших онлайн-спільнотах?"
]

openai_survey = Survey(survey_name, questions)

survey_answers = openai_survey.conduct_survey()
openai_survey.save_survey_results(survey_answers)


# Завдання 3
class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.events = []

    def add_event(self, event_name):
        self.events.append(event_name)

    def save_data_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(vars(self), f)
        print("Данні збережені", filename, "в JSON формат.")

    def save_data_pickle(self, filename):
        with gzip.open(filename, 'wb') as f:
            pickle.dump(vars(self), f)
        print("Данні збережені", filename, "в Pickle формат.")

    @staticmethod
    def load_data_json(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        stadium = Stadium(data['name'], data['capacity'])
        stadium.events = data['events']
        print("Данні завантажені", filename, "з JSON формату.")
        return stadium

    @staticmethod
    def load_data_pickle(filename):
        with gzip.open(filename, 'rb') as f:
            data = pickle.load(f)
        stadium = Stadium(data['name'], data['capacity'])
        stadium.events = data['events']
        print("Данні завантаженні", filename, "з Pickle формату.")
        return stadium


stadium = Stadium("Camp Nou", 99000)
stadium.add_event("Football match")
stadium.add_event("Concert")

stadium.save_data_json("stadium_data.json")

stadium.save_data_pickle("stadium_data.pkl.gz")

loaded_stadium_json = Stadium.load_data_json("stadium_data.json")
print("Завантаження данних з JSON:", vars(loaded_stadium_json))

loaded_stadium_pickle = Stadium.load_data_pickle("stadium_data.pkl.gz")
print("Завантаження данних з Pickle:", vars(loaded_stadium_pickle))
