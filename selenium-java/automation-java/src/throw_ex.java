
import org.openqa.selenium.By;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.NoSuchElementException;



public class throw_ex {
    public static void main(String[] args) throws NoSuchElementException{
        WebDriver driver = new ChromeDriver();
        // WebDriverWait wait = new WebDriverWait(driver, 10);
        driver.get("https://www.google.com");
        try{
            driver.findElement(By.xpath("//*[@id='register']")).click();
        }catch (Exception e) {
            System.out.println("Register element is not found.");
            e.getMessage();
            e.printStackTrace();
            throw(e);
        }
            System.out.println("Hello");
        }
}

