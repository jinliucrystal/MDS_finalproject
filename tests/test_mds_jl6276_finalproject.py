from mds_jl6276_finalproject import mds_jl6276_finalproject
import folium
from folium.plugins import MarkerCluster
def test():
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
    expected = m
    actual = mds_jl6276_finalproject.get_map('spanish')
    assert type(actual) == type(expected), "Result should be an map object"
    return actual


    
