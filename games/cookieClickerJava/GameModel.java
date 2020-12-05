public class GameModel{

	CookieInfo cookie;

	public GameModel(){

		cookie = new CookieInfo();
		reset();
	}

	public void reset(){
		cookie = new CookieInfo();
	}

	public CookieInfo getCookie(){

		return cookie;
	}

	public double getNumberOfCookies(){

		return cookie.getNumberOfCookies();
	}

	public double getCookiesPerSec(){

		return cookie.getCookiesPerSec();
	}

	public double getCookiesPerClick(){

		return cookie.getCookiesPerClick();
	}




	public void increaseNumberOfCookies(double increment){

		cookie.increaseNumberOfCookies(increment);
	}

	public void increaseCookiesPerSec(double increment){

		cookie.increaseCookiesPerSec(increment);
	}

	public void increaseCookiesPerClick(double increment){

		cookie.increaseCookiesPerClick(increment);
	}



	public String toString(){
        StringBuffer b = new StringBuffer();
        b.append("You are making cookies!");
        return b.toString();
    }
}