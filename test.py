package RestAPI111.RESSS;

import org.testng.Assert;
import org.testng.annotations.Test;

import io.restassured.RestAssured;
import io.restassured.http.Method;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;

public class RestAPITest {
@Test
void getDexcom()
{
//Specifying the Base URI
RestAssured.baseURI = "https://sandbox-api.dexcom.com";

//Creation of get request object
RequestSpecification httpRequest = RestAssured.given();

//Response Object Creation
Response response = httpRequest.request(Method.GET,"/info");

//Printing the respose in Console
String responseBody = response.getBody().asString();

//case 1 : Status code validation
int statuscode = response.getStatusCode();
System.out.println("Status code is :"+ statuscode);
Assert.assertEquals(statuscode, 200);

//Case 2 : Capturing details of Header
String header = response.header("Content-Type");
System.out.println("The Hearder content-type is :" +header);
Assert.assertEquals(header, "application/json");

//Case 3 : From the response validating the Product Name, UDI / Device Identifier,Version, Part Number (PN)

Assert.assertEquals(responseBody.contains("Dexcom API"), true); //Checking the product name
Assert.assertEquals(responseBody.contains("00386270000668"), true); // Checking the UDI / Device Identifier
Assert.assertEquals(responseBody.contains("3.1.1.0"), true); // Checking the Version
Assert.assertEquals(responseBody.contains("350-0019"), true);// Checking the Part Number (PN)

String [] Sub_Components_Name = new String[2];
		Sub_Components_Name[0] = "api-gateway";
		Sub_Components_Name[1]= "insulin-service";
		for(int i =0; i< Sub_Components_Name.length; i++){
			System.out.println(Sub_Components_Name[i]);
		}
	
Assert.assertEquals(responseBody.contains("Sub_Components_Name[0]"),"api-gateway");//Getting the names of api-gateway
Assert.assertEquals(responseBody.contains("Sub_Components_Name[1]"),"insulin-service");//Getting the names of insulin-service

//Case 4:Verify that the content-type header is returned as a valid xml media type

String header = response.header("Content-Type");
System.out.println("The Hearder content-type is :" +header);
Assert.assertEquals(header, "application/json");

}

}    