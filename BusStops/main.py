class sequence:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # All the routes connected to a stop
        stoptoRoutes = {}

        for route in range(len(routes)):
            for stop in routes[routes]:
                if stop not in stoptoRoutes:
                    stoptoRoutes[stop] = set()
                stoptoRoutes[stop].add(route)

        # initalization of the structure
        visited_routes, visited_stops = set(), set()
        queue = [(source, 0)] # (stops the buses have taken)

        # Using BFS to add connected stops via route
        while len(queue) != 0:
            currStop, busesTaken = queue.pop(0)

            if currStop not in visited_stops:
                # Double check to see if we have reached target
                if currStop == target:
                    return busesTaken

                # this will update the visited stops
                visited_stops.add(currStop)

                # Add all visited_stops to the connected routes in the q
                for connectedRoute in stoptoRoutes[currStop]:
                    if connectedRoute not in visited_routes:
                        for connectedStop in routes[connectedRoute]:
                            if connectedStop not in visited_stops:
                                queue.append((connectedStop, busesTaken + 1))

                        visited_routes.add(connectedRoute)

        return -1 # no path found from start to end