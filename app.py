#import necessary libraries
from concurrent import futures
import logging

#libraries for grpc
import grpc
#generated code from proto file
import inventory_pb2
import inventory_pb2_grpc

#function to calculate percentile
def calculate_percentile(data, percentile):


    sorted_data = sorted(data)

    index = int((percentile / 100) * len(sorted_data))

    index = min(max(index, 0), len(sorted_data) - 1)

    value = sorted_data[index]

    return value

#class to implement the service
class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
    #initialize the data
    def __init__(self):

        self.inventory_data = {
            "IN0001": {
                "inventory_id": "IN0001",
                "name": "Item 1",
                "description": "Desc 1",
                "unit_price": 51,
                "quantity_in_stock": 25,
                "inventory_value": 1275,
                "reorder_level": 29,
                "reorder_time": 13,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0002": {
                "inventory_id": "IN0002",
                "name": "Item 2",
                "description": "Desc 2",
                "unit_price": 93,
                "quantity_in_stock": 132,
                "inventory_value": 12276,
                "reorder_level": 231,
                "reorder_time": 4,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0003": {
                "inventory_id": "IN0003",
                "name": "Item 3",
                "description": "Desc 3",
                "unit_price": 57,
                "quantity_in_stock": 151,
                "inventory_value": 8607,
                "reorder_level": 114,
                "reorder_time": 11,
                "reorder_quantity": 150,
                "discontinued": False,
            },
            "IN0004": {
                "inventory_id": "IN0004",
                "name": "Item 4",
                "description": "Desc 4",
                "unit_price": 19,
                "quantity_in_stock": 186,
                "inventory_value": 3534,
                "reorder_level": 158,
                "reorder_time": 6,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0005": {
                "inventory_id": "IN0005",
                "name": "Item 5",
                "description": "Desc 5",
                "unit_price": 75,
                "quantity_in_stock": 62,
                "inventory_value": 4650,
                "reorder_level": 39,
                "reorder_time": 12,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0006": {
                "inventory_id": "IN0006",
                "name": "Item 6",
                "description": "Desc 6",
                "unit_price": 11,
                "quantity_in_stock": 5,
                "inventory_value": 55,
                "reorder_level": 9,
                "reorder_time": 13,
                "reorder_quantity": 150,
                "discontinued": False,
            },
            "IN0007": {
                "inventory_id": "IN0007",
                "name": "Item 7",
                "description": "Desc 7",
                "unit_price": 56,
                "quantity_in_stock": 58,
                "inventory_value": 3248,
                "reorder_level": 109,
                "reorder_time": 7,
                "reorder_quantity": 100,
                "discontinued": True,
            },
            "IN0008": {
                "inventory_id": "IN0008",
                "name": "Item 8",
                "description": "Desc 8",
                "unit_price": 38,
                "quantity_in_stock": 101,
                "inventory_value": 3838,
                "reorder_level": 162,
                "reorder_time": 3,
                "reorder_quantity": 100,
                "discontinued": False,
            },
            "IN0009": {
                "inventory_id": "IN0009",
                "name": "Item 9",
                "description": "Desc 9",
                "unit_price": 59,
                "quantity_in_stock": 122,
                "inventory_value": 7198,
                "reorder_level": 82,
                "reorder_time": 3,
                "reorder_quantity": 150,
                "discontinued": False,
            },
            "IN0010": {
                "inventory_id": "IN0010",
                "name": "Item 10",
                "description": "Desc 10",
                "unit_price": 50,
                "quantity_in_stock": 175,
                "inventory_value": 8750,
                "reorder_level": 283,
                "reorder_time": 8,
                "reorder_quantity": 150,
                "discontinued": False,
            },
            "IN0011": {
                "inventory_id": "IN0011",
                "name": "Item 11",
                "description": "Desc 11",
                "unit_price": 59,
                "quantity_in_stock": 176,
                "inventory_value": 10384,
                "reorder_level": 229,
                "reorder_time": 1,
                "reorder_quantity": 100,
                "discontinued": False,
            },
            "IN0012": {
                "inventory_id": "IN0012",
                "name": "Item 12",
                "description": "Desc 12",
                "unit_price": 18,
                "quantity_in_stock": 22,
                "inventory_value": 396,
                "reorder_level": 36,
                "reorder_time": 12,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0013": {
                "inventory_id": "IN0013",
                "name": "Item 13",
                "description": "Desc 13",
                "unit_price": 26,
                "quantity_in_stock": 72,
                "inventory_value": 1872,
                "reorder_level": 102,
                "reorder_time": 9,
                "reorder_quantity": 100,
                "discontinued": False,
            },
            "IN0014": {
                "inventory_id": "IN0014",
                "name": "Item 14",
                "description": "Desc 14",
                "unit_price": 42,
                "quantity_in_stock": 62,
                "inventory_value": 2604,
                "reorder_level": 83,
                "reorder_time": 2,
                "reorder_quantity": 100,
                "discontinued": False,
            },
            "IN0015": {
                "inventory_id": "IN0015",
                "name": "Item 15",
                "description": "Desc 15",
                "unit_price": 32,
                "quantity_in_stock": 46,
                "inventory_value": 1472,
                "reorder_level": 23,
                "reorder_time": 16,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0016": {
                "inventory_id": "IN0016",
                "name": "Item 16",
                "description": "Desc 16",
                "unit_price": 90,
                "quantity_in_stock": 96,
                "inventory_value": 8640,
                "reorder_level": 180,
                "reorder_time": 3,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0017": {
                "inventory_id": "IN0017",
                "name": "Item 17",
                "description": "Desc 17",
                "unit_price": 97,
                "quantity_in_stock": 57,
                "inventory_value": 5529,
                "reorder_level": 98,
                "reorder_time": 12,
                "reorder_quantity": 50,
                "discontinued": True,
            },
            "IN0018": {
                "inventory_id": "IN0018",
                "name": "Item 18",
                "description": "Desc 18",
                "unit_price": 12,
                "quantity_in_stock": 6,
                "inventory_value": 72,
                "reorder_level": 7,
                "reorder_time": 13,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0019": {
                "inventory_id": "IN0019",
                "name": "Item 19",
                "description": "Desc 19",
                "unit_price": 82,
                "quantity_in_stock": 143,
                "inventory_value": 11726,
                "reorder_level": 164,
                "reorder_time": 12,
                "reorder_quantity": 150,
                "discontinued": False,
            },
            "IN0020": {
                "inventory_id": "IN0020",
                "name": "Item 20",
                "description": "Desc 20",
                "unit_price": 16,
                "quantity_in_stock": 124,
                "inventory_value": 1984,
                "reorder_level": 113,
                "reorder_time": 14,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0021": {
                "inventory_id": "IN0021",
                "name": "Item 21",
                "description": "Desc 21",
                "unit_price": 19,
                "quantity_in_stock": 112,
                "inventory_value": 2128,
                "reorder_level": 75,
                "reorder_time": 11,
                "reorder_quantity": 50,
                "discontinued": False,
            },
            "IN0022": {
                "inventory_id": "IN0022",
                "name": "Item 22",
                "description": "Desc 22",
                "unit_price": 24,
                "quantity_in_stock": 182,
                "inventory_value": 4368,
                "reorder_level": 132,
                "reorder_time": 15,
                "reorder_quantity": 150,
                "discontinued": False,
            },
            "IN0023": {
                "inventory_id": "IN0023",
                "name": "Item 23",
                "description": "Desc 23",
                "unit_price": 29,
                "quantity_in_stock": 106,
                "inventory_value": 3074,
                "reorder_level": 142,
                "reorder_time": 1,
                "reorder_quantity": 150,
                "discontinued": True,
            },
            "IN0024": {
                "inventory_id": "IN0024",
                "name": "Item 24",
                "description": "Desc 24",
                "unit_price": 75,
                "quantity_in_stock": 173,
                "inventory_value": 12975,
                "reorder_level": 127,
                "reorder_time": 9,
                "reorder_quantity": 100,
                "discontinued": False,
            },
            "IN0025": {
                "inventory_id": "IN0025",
                "name": "Item 25",
                "description": "Desc 25",
                "unit_price": 14,
                "quantity_in_stock": 28,
                "inventory_value": 392,
                "reorder_level": 21,
                "reorder_time": 8,
                "reorder_quantity": 50,
                "discontinued": False,
            }
        }
    
    #implement the service function - search by id
    def SearchById(self, request, context):
        inventory_id = request.id
        
        if inventory_id in self.inventory_data:
            return inventory_pb2.SearchByIdResponse(inventory= inventory_pb2.Inventory(**self.inventory_data[inventory_id]))
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Inventory record not found")
    
    #implement the service function - search
    def Search(self, request, context):
        key_name = request.key_name
        key_value = request.key_value

        matching_records = [record for record in self.inventory_data.values() if record[key_name] == key_value]

        if len(matching_records) != 0:
            return inventory_pb2.SearchResponse(inventories=[inventory_pb2.Inventory(**record) for record in matching_records])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Inventory records not found")
    
    #implement the service function - search in range
    def SearchInRange(self, request, context):
        key_name = request.key_name;
        key_value_min = request.min_value;
        key_value_max = request.max_value;

        matching_records = [record for record in self.inventory_data.values() if key_value_min <= record[key_name] <= key_value_max]

        if len(matching_records) != 0:
            return inventory_pb2.SearchInRangeResponse(inventories=[inventory_pb2.Inventory(**record) for record in matching_records])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Inventory records not found")
    
    #implement the service function - get distribution
    def GetDistribution(self, request, context):
        
        key_name = request.key_name
        percentile = request.percentile

        key_values = [record[key_name] for record in self.inventory_data.values() if key_name in record]

        if key_values:
            value = calculate_percentile(key_values, percentile)
        else:
            value = None

        if value is not None:
            return inventory_pb2.GetDistributionResponse(percentile=value)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Key '{key}' not found or unsupported")
            return inventory_service_pb2.GetDistributionResponse(value=None)
    
    #implement the service function - update
    def Update(self, request, context):
        key_name = request.key_name
        key_value = request.key_value
        update_key_name = request.update_key_name
        update_value = request.update_value


        for record in self.inventory_data.values():
            if key_name in record:
                if record[key_name] == key_value:
                    record[update_key_name] = update_value
                    print(record)
                    return inventory_pb2.UpdateResponse(updated= True)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Inventory not found")
                return inventory_pb2.UpdateResponse(updated= False)

#function to serve the service
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

#main function
if __name__ == "__main__":
    logging.basicConfig()
    serve()
