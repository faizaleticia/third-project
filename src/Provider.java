public class Provider {
    private String name;
    private float latitude;
    private float longitude;

    public Provider(String name, float latitude, float longitude) {
        this.name = name;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public String getName() {
        return this.name;
    }

    public float getLatitude() {
        return this.latitude;
    }

    public float getLongitude() {
        return this.longitude;
    }

    @Override
    public String toString() {
        return this.name + " - Latitude: " + this.latitude + " Longitude: " + this.longitude + "\n";
    }
}