def random_waypoints(aircraft_name, area, num_points, lat=37.6213, long=-122.379, alt=10.668, rewind=True):
    if rewind:
        root.Rewind()
        
    temp_lat, temp_long = lat, long 
    
    root.ExecuteCommand(f'AddWaypoint */Aircraft/{aircraft_name} DetTimeAccFromVel {temp_lat} {temp_long} {alt} 1.0')
    
    # 1 degree is 111 km
    x = (math.sqrt(area / math.pi)) / 111
    y = math.sqrt(area / math.pi) / 111
    
    if num_points > 2:
        for i in range(num_points - 2):
            coin_flip = random.randint(0,1)
            if coin_flip == 0:
                lat = random.uniform(lat, lat + x)
                long = random.uniform(long, long + y)
                root.ExecuteCommand(f'AddWaypoint */Aircraft/{aircraft_name} DetTimeAccFromVel {lat} {long} {alt} 1.0')
            else:
                lat = random.uniform(lat, lat - x)
                long = random.uniform(long, long - y)
                root.ExecuteCommand(f'AddWaypoint */Aircraft/{aircraft_name} DetTimeAccFromVel {lat} {long} {alt} 1.0')
                
    root.ExecuteCommand(f'AddWaypoint */Aircraft/{aircraft_name} DetTimeAccFromVel {temp_lat} {temp_long} {alt} 1.0')



