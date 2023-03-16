import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;
import java.util.concurrent.TimeUnit;

public class multiselect_dropdown {
    public static void main(String args[]) throws InterruptedException{
        
        WebDriver driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/");
		driver.navigate().refresh();
		//Once you got the select object initialised then you can access all the methods of select class. 
		//Identify the select HTML element:
		Thread.sleep(10000);
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		WebElement mySelectElement = driver.findElement(By.name("multipleselect[]"));

        Select dd = new Select(mySelectElement);
        dd.selectByValue("ddmanual"); 
        WebElement option = dd.getFirstSelectedOption();
        System.out.println(option.getText());
    }
}
