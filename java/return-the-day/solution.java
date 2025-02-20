public class DayOfWeek {

public static String getDay(int n) {
        final String[] week = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

        try {
            return week[n - 1];
        } catch (ArrayIndexOutOfBoundsException e) {
            return "Wrong, please enter a number between 1 and 7";
        }
    }
  
}