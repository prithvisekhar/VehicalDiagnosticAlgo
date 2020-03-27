def AverageDistance(Distance, Fuel, Kmpl):
    ExpectedDistance = []
    TotalDistance = Distance.iloc[-1]
    TotalDistance = float(TotalDistance)
    print("The total Distance covered:", TotalDistance)
    RemainingFuel = Fuel.iloc[-1]
    UsedFuel = Fuel.iloc[-1] - Fuel.iloc[1]
    print("UsedFuel:", UsedFuel)
    Mileage = TotalDistance/UsedFuel
    TimeIndex = input('Enter the Time : ')
    for i in Distance.index:
        ExpectedDistance.append([Fuel[i]*Mileage], i)
    if TimeIndex < range(len(Kmpl)):
        TempExpectedDistance = Fuel[TimeIndex]*Mileage
    else:
        TempExpectedDistance = RemainingFuel*Mileage
    print('Expected Distance', TempExpectedDistance)
    DistanceToZero = pd.DataFrame(data=ExpectedDistance, columns=['DistanceToZero', 'Index'])
    return DistanceToZero
