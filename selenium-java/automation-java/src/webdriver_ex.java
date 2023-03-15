import org.openqa.selenium.WebDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;

public class webdriver_ex {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        WebDriver driver = new InternetExplorerDriver();
        driver.get("https://www.google.com");
        driver.quit();   
    }
} 

