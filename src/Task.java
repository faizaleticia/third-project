import java.util.LinkedList;

public class Task {
    public static void main(String[] args) {
        var reader = new SimpleReader("../files/clients.txt");
        var clients = new LinkedList<Client>();
        var line = reader.readLine();
        while(line != null) {
            var client = line.split(" ");
            clients.add(new Client(client[0], Float.parseFloat(client[1]), Float.parseFloat(client[2])));
            
            line = reader.readLine();
        }
        reader.close();

        reader = new SimpleReader("../files/providers.txt");
        var providers = new LinkedList<Provider>();
        line = reader.readLine();
        while(line != null) {
            var provider = line.split(" ");
            providers.add(new Provider(provider[0], Float.parseFloat(provider[1]), Float.parseFloat(provider[2])));
            
            line = reader.readLine();
        }
        reader.close();

        
    }
}