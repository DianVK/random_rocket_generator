![README](https://user-images.githubusercontent.com/115580585/215584373-75e62f1c-2378-40e5-8166-a9c0bf7256c9.gif)


Console Application To Represent A Random Missile Generator with an Air Defence System
Create a console application to represent:
- It is generating 1 random missile every 3 seconds
- Missiles are 3 types: ThermoNuclear, FacetBomb and TNTBomb (each represented by a different class)
- Missiles have the following properties: SerialNumber (unique), MissileType
- An Air Defence System, that can identify the 3 types of missles and neutralizes each of them
- Different Anti-Air Guns - AntiThermoGun, AntiFacetGun, AntiTNTGun (each represented by a different class)
- The Air Defence System has a method InterceptMissile accepting a Missile as a parameter
- Each Gun has a method Neutralize that accepts an appropriate Missile as parameter and neutralizes only that one type of missiles. 
- The air defence system must decide which missile will be neutralized with which gun.
- Two options to Run the Program - Indefinitely or with a fixed number of Missiles, greater than 10.
