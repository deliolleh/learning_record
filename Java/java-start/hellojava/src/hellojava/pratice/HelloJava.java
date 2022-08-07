package hellojava.pratice;

/**
 * 첫번째 자바 실습
 * 
 * @author jhhan
 * @update say함수 추가 (2022-08-02 by QQQ)
 *
 */

public class HelloJava {

	public static void main(String[] args) {

//		HelloJava에게 say라는 명령을 내림!
		HelloJava.say("Hi");

//		JVM이 스스로 화면에 출력
		System.out.println("Hello Java");
	}

	public static void say(String msg) {
		System.out.println(msg);
	}

}
