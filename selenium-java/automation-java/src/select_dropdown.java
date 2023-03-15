import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class select_dropdown {
    public static void main(String args[]){
        try {
            WebDriver driver = new ChromeDriver();
            driver.manage().window().maximize();

            driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/");
            driver.navigate().refresh();
        
            Thread.sleep(10000);
            
            WebElement mElement = driver.findElement(By.name("dropdown"));
            Select dd = new Select(mElement);
            dd.selectByVisibleText("Automation Testing");
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            e.getMessage();
        }
    }
}
