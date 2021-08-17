## Distance Calculation Blueprint
Flask Blueprint to find the distance from the Moscow Ring Road to the specified address.

# How to use.
Start flask server by going to the folder where the application is located and typing "flask run" at the command prompt.

```
$ flask run
```

Go to http://127.0.0.1:5000/ and enter the address that distance you want to calculate. Then click calculate distance.

![image](https://user-images.githubusercontent.com/48105864/129762642-52d0c126-37fc-4416-99bf-43ed6b1fd303.png)

You will see the information about adress.
- Adress
- Distance from Moscow Ring Road
- Whether the adress is inside or outside the MKAD.

![image](https://user-images.githubusercontent.com/48105864/129762667-5c784762-642f-48fe-9a1f-86aa951927cb.png)

If you want to calculate the distance of another adress. Click to calculate another location.

All the information about adress will be logged in distance_logs.log file.


# How to pull docker container and run as a container.


```
docker run --publish 5000:5000 python-docker
```


