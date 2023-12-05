def read_input():
    with open('input.txt', 'r') as input_file:
        input_maps = input_file.read().strip().split('\n\n')
    return input_maps


def get_map(map_name, map_index):
    file = read_input()
    locations = []
    almanac_map = file[map_index].split('\n')
    for map in almanac_map:
        if not map == map_name:
            arrays = map.split(' ')
            arrays = [int(x) for x in arrays]
            locations.append(arrays)
    return locations

def get_mapping(map_name, numbers):
    mapped_values = []
    for number in numbers:
        for data in map_name:
            destination = data[0]
            source = data[1]
            range = data[2]

            if source <= number <= source + range - 1:
                reference = number - source + destination
                break
            else:
                reference = number
        mapped_values.append(reference)
    return mapped_values

file = read_input()

seeds = [int(x) for x in file[0].split(' ') if x != 'seeds:']

seed_to_soil_map = get_map('seed-to-soil map:', 1)
seed_to_soil = get_mapping(seed_to_soil_map, seeds)

soil_to_fertilizer_map = get_map('soil-to-fertilizer map:', 2)
soil_to_fertilizer = get_mapping(soil_to_fertilizer_map, seed_to_soil)

fertilizer_to_water_map = get_map('fertilizer-to-water map:', 3)
fertilizer_to_water = get_mapping(fertilizer_to_water_map, soil_to_fertilizer)

water_to_light_map = get_map('water-to-light map:', 4)
water_to_light = get_mapping(water_to_light_map, fertilizer_to_water)

light_to_temp_map = get_map('light-to-temperature map:', 5)
light_to_temp = get_mapping(light_to_temp_map, water_to_light)

temp_to_humidity_map = get_map('temperature-to-humidity map:', 6)
temp_to_hum = get_mapping(temp_to_humidity_map, light_to_temp)

humidity_to_location_map = get_map('humidity-to-location map:', 7)
hum_to_loc = get_mapping(humidity_to_location_map, temp_to_hum)

print(min(hum_to_loc))
