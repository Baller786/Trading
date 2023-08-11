from flask import Flask, render_template

app = Flask(__name__)

stocks_data = [
    {
        'name': "AAPL",
        'price': 192.12,
        'shares': 120, 
        'options': [
            {
                'type': 'call',
                'profit': 50,
            },
            {
                'type': 'put',
                'profit': 80
            },
            {
                'type': 'call',
                'profit': 20
            }
        ]
    },
    {
        'name': "TSLA",
        'price': 162.12,
        'shares': 20, 
        'options': [
            {
                'type': 'call',
                'profit': 150
            },
            {
                'type': 'put',
                'profit': 180
            },
            {
                'type': 'call',
                'profit': -70
            }
        ]
    },
    {
        'name': "HOOD",
        'price': 122.12,
        'shares': 220, 
        'options': [
            {
                'type': 'put',
                'profit': 150
            },
            {
                'type': 'put',
                'profit': 180
            },
            {
                'type': 'call',
                'profit': -70
            }
        ]
    }
]

@app.route('/')
def stock_info():
    stock_info_list = []
    for stock in stocks_data:
        name = stock['name']
        price = stock['price']
        amount = stock['shares']
        profit = price * amount

        options = stock['options']
        options_profit = sum(int(option['profit']) for option in options)
        total_profit = profit + options_profit

        stock_info_list.append({
            'name': name,
            'shares': amount,
            'share_profit': profit,
            'option_profit': options_profit,
            'total_profit': total_profit
        })

    return render_template('stock_info.html', stocks=stock_info_list)


if __name__ == '__main__':
    app.run(debug=True)