// https://www.softwaretestingmaterial.com/headless-browser-testing-using-htmlunitdriver/
// Download htmlunit - https://github.com/SeleniumHQ/htmlunit-driver/releases
// https://www.softwaretestingmaterial.com/headless-browser-testing-using-phantomjsdriver/
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;

public class htmlunit_driver{
    public static void main(String args[]) throws InterruptedException{
        try{
            WebDriver driver = new HtmlUnitDriver();
            driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
            Thread.sleep(1000);
            driver.get("https://www.google.com");
            WebElement el = driver.findElement(By.id("input"));
            el.sendKeys("softwaretestingmaterial.com");
            el.submit();  

            driver.findElement(By.linkText("Software Testing Material")).click();
            String title = driver.getTitle();
            System.out.println("I am at "+title); 
        }catch(Exception e){
            e.getMessage();
            e.printStackTrace();
            e.toString();
        }
    }
}