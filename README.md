# ClickBot
Automate every task that requires periodical clicks with click bot.


## JSON File Format
```json
[
    {
        "macro-id":"test",
        "hotplaces":[
            [[x0,y0],time_delta0],
            [[x1,y1],time_delta1],
            [[x2,y2],time_delta2]
        ]
    }
]
```
The JSON Above means goto the point (x0,y0) and emulate a click every time_delta0 seconds when test data set is requested.