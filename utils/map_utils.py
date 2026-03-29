import folium

def create_map(data):
    # Center map (Mumbai region)
    m = folium.Map(location=[19.07, 72.87], zoom_start=6)

    for _, row in data.iterrows():
        color = "red" if row['risk'] == 1 else "green"

        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"Risk: {'High' if row['risk'] else 'Safe'}",
            icon=folium.Icon(color=color)
        ).add_to(m)

    return m._repr_html_()