from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        start_index = []
        json_string = ""
        start_index_exists = False
        with open(self.input_file) as f:
            line = f.readline()
            count = 0
            while line:
                for a in line:
                    if a == '{':
                        start_index.append(count)
                        start_index_exists = True
                    elif a == '}':
                        start_index.pop()

                if len(start_index) == 0 and start_index_exists:
                    json_string = f'{json_string}{line}'
                    json_string = json_string.rstrip()
                    json_string = json_string.rstrip(',')
                    json_string[:-1]
                    if len(json_string) > 10:
                        message = self.dict_to_binary(json.loads(json_string))
                        # TODO send the correct data
                        self.send(self.topic, message)
                        self.flush()
                        time.sleep(1)                           
                    print(json_string)
                    json_string = ""

                    line = f.readline()
                    count += 1
                    continue

                if start_index_exists:
                    json_string = f'{json_string}{line}'

                line = f.readline()
                count += 1
                #Uncomment to Limit
                #if count > 500:
                #    break

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        json_str = json.dumps(json_dict)
        #binary = ' '.join(format(ord(letter), 'b') for letter in json_str)
        
        return json_str.encode('utf-8')        
        
