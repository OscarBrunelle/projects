public class CookieInfo{

	double numberOfCookies;
	double cookiesPerSec;
	double cookiesPerClick;

	public CookieInfo(){
		numberOfCookies=0;
		cookiesPerSec=0;
		cookiesPerClick=1;
	}

	public double getNumberOfCookies(){

		return numberOfCookies;
	}

	public double getCookiesPerSec(){

		return cookiesPerSec;
	}

	public double getCookiesPerClick(){

		return cookiesPerClick;
	}



	public void increaseNumberOfCookies(double increment){

		numberOfCookies+=increment;
	}

	public void increaseCookiesPerSec(double increment){

		cookiesPerSec+=increment;
	}

	public void increaseCookiesPerClick(double increment){

		cookiesPerClick+=increment;
	}
}