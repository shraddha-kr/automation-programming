import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.NoAlertPresentException;

public class noalert_ex {
    public static void main(String[] args){
        try{
            WebDriver driver = new ChromeDriver();
            driver.switchTo().alert().accept();
        }catch(NoAlertPresentException e){
            e.printStackTrace();
            e.getMessage();
            e.toString();
        }
    }
}
