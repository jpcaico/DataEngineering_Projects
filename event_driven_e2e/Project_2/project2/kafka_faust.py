import faust

app = faust.App(
    'kafka_faust',
    broker='localhost:9092',
    value_serializer='raw',
)

greetings_topic = app.topic('greetings')

# @app.agent(greetings_topic)
# async def greet(greetings):
#     async for greeting in greetings:
#         print(greeting)