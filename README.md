# Distance Calculation Blueprint
Flask Blueprint to find the distance from the Moscow Ring Road to the specified address.

# How to Use
Start flask server by going to the folder where the application is located and typing "flask run" at the command prompt.

```
$ flask run
```

Go to http://127.0.0.1:5000/ and enter the address that distance you want to calculate. Then click check distance.

![image](https://user-images.githubusercontent.com/48105864/129760333-05d4b526-cd9e-42b1-9c03-7a50e9dbc0be.png)

You will see the information about adress.
- Adress
- Distance from Moscow Ring Road
- Whether the adress is inside or outside the MKAD.

![image](https://user-images.githubusercontent.com/48105864/129761017-33458013-e431-4b5c-8300-014695e176a5.png)

If you want to calculate the distance of another adress. Click to calculate another location.

All the information about adress will be logged in distance_logs.log file.

