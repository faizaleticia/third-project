public class Client {
    private String name;
    private float latitude;
    private float longitude;

    public Client(String name, float latitude, float longitude) {
        this.name = name;
        this.latitude = latitude; //y
        this.longitude = longitude; //x
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