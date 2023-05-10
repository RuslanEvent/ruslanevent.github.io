from typing import Optional
from telegram import Bot, LabeledPrice

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

INVOICE_TOKEN = '371317599:TEST:1683704970035'


class Order(BaseModel):
    order_data: list
    comment: Optional[str] = None
    user_id: int
    user_hash: str


goods = [
    {
        'id': 1,
        'name': 'Barbucks dark',
        'price': 30
    },
    {
        'id': 2,
        'name': 'Barbucks dalightrk',
        'price': 41
    },
    {
        'id': 3,
        'name': 'Barbucks split',
        'price': 23
    },
    {
        'id': 4,
        'name': 'Barbucks weight',
        'price': 33
    },
    {
        'id': 5,
        'name': 'Barbucks strong',
        'price': 54
    },
    {
        'id': 6,
        'name': 'Barbucks odd',
        'price': 65
    },
    {
        'id': 7,
        'name': 'Barbucks milk',
        'price': 91
    },
    {
        'id': 8,
        'name': 'Barbucks lolipop',
        'price': 54
    },
    {
        'id': 9,
        'name': 'Barbucks hot',
        'price': 65
    },
    {
        'id': 10,
        'name': 'Barbucks height',
        'price': 59
    },
    {
        'id': 11,
        'name': 'Barbucks green',
        'price': 55
    },
    {
        'id': 12,
        'name': 'Barbucks red',
        'price': 37
    },
    {
        'id': 13,
        'name': 'Barbucks purple',
        'price': 80
    },
    {
        'id': 14,
        'name': 'Barbucks greenzen',
        'price': 80
    },
    {
        'id': 15,
        'name': 'Barbucks yellow',
        'price': 80
    },
    {
        'id': 16,
        'name': 'Barbucks orange',
        'price': 80
    },
]
    


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ruslanevent.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/api/invoice')
async def createInvoice(order: Order):
    bot = Bot('5838841823:AAGUMz01lYyPqVBsTO-Xx9jvvDw7xcWD8Fo')
    prices = map(create_labeled_price, order.order_data)
    url = await bot.create_invoice_link(
        title='Оплатить заказ', 
        description='Оплатить заказ в Barbucks', 
        payload=order.user_hash, 
        provider_token=INVOICE_TOKEN,
        currency='UZS',
        prices=prices
    )

    return {'url': url}


def create_labeled_price(order_item: dict):
    found_goods = filter(lambda x: x['id'] == order_item['id'], goods)
    if len(found_goods) == 0:
        raise Exception('Good not found')
    found_good = found_goods[0]
    return LabeledPrice(
        label=found_good['name'],
        amount=found_good['price'] * order_item['quantity']
    )
