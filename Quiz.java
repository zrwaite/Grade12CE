import java.util.Scanner;
import java.util.Random;

public class Quiz {
    
    //Method to take input, returns int
    public static int intInput(){
        //Creates scanner and take user input
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        return a;
    }
    
    //Method to take input, returns String
    public static String strInput(){
        //Creates scanner and take user input
        Scanner input = new Scanner(System.in);
        String a = input.nextLine();
        return a;
    }

    //Methods to print strings, saving typing time
    public static void pl(String input){
        //Prints
       System.out.println(input);
    }
    public static void p(String input){
        //Prints
       System.out.print(input);
    }
    
    //Method to leave a blank space, just saves me a few seconds of typing
    public static void space(){
        pl("");
    }
    
    public static void main(String[] args) {
        Random rand = new Random();
        //Variable delclaration
        int q = 0; //Question number
        int o = 0; //Option Number
        int userInput = 0; //User Input
        int score = 0; //User Score
        final int numQs = 10; //Number of Questions
        final int numOs = 4; //Number of options per question
        boolean valid = false; //Used for validity loops with try/catch
        //Questions
        String qs [] = new String [numQs];
        //Options
        String os [][] = new String [numQs][numOs];
        //Answers
        Integer as [] = {3, 0, 3, 3, 0, 1, 2, 0, 2, 0}; //JOE30330 and the Year 12020 H.E.
        //Array that helps generate a random order to go through other arrays
        Integer qRem [] = new Integer [numQs];
        for (int i = 0; i<numQs; i++){
            qRem[i] = i;
        }
        
        //Question and Answer declaration
        qs[0] = "Who was the last democrat to drop out of the race for the nomination?";
        os[0][0] = "Joe Biden";
        os[0][1] = "Elizabeth Warren";
        os[0][2] = "Amy Klobuchar";
        os[0][3] = "Bernie Sanders"; //
        qs[1] = "Which democratic candidate was from Hawaii?";
        os[1][0] = "Tulsi Gabbard"; //
        os[1][1] = "Andrew Yang";
        os[1][2] = "Joe Biden";
        os[1][3] = "Bernie Sanders";
        qs[2] = "How many republicans ran against Trump for the nomination"; 
        os[2][0] = "1";
        os[2][1] = "2";
        os[2][2] = "3";
        os[2][3] = "4";//
        qs[3] = "Which republican candidate did the best against Donald Trump"; 
        os[3][0] = "Rocky De La Fuente";
        os[3][1] = "Joe Walsh"; 
        os[3][2] = "Mark Sanford";
        os[3][3] = "Bill Weld";//
        qs[4] = "Which democratic candidate ran on the issue of automation?";
        os[4][0] = "Andrew Yang"; //
        os[4][1] = "Tulsi Gabbard";
        os[4][2] = "Beto O'Rourke";
        os[4][3] = "Corry Booker";
        qs[5] = "Which democratic candidate won the Iowa Primary?";
        os[5][0] = "Micheal Bloomberg";
        os[5][1] = "Pete Buttigieg";//
        os[5][2] = "Bernie Sanders";
        os[5][3] = "Joe Biden";
        qs[6] = "Which democratic candidate won the New Hampshire Primary?";
        os[6][0] = "Micheal Bloomberg";
        os[6][1] = "Pete Buttigieg";
        os[6][2] = "Bernie Sanders";//
        os[6][3] = "Joe Biden";
        qs[7] = "Which female candidate did the best in the primary?";
        os[7][0] = "Elizabeth Warren";//
        os[7][1] = "Kamala Harris";
        os[7][2] = "Amy Klobuchar";
        os[7][3] = "Tulsi Gabbard";
        qs[8] = "What was the most people on a single debate stage?";
        os[8][0] = "6";
        os[8][1] = "9";
        os[8][2] = "12";//
        os[8][3] = "15";
        qs[9] = "Who won the 2020 Election?";
        os[9][0] = "Joe Biden"; //
        os[9][1] = "Kanye West";
        os[9][2] = "Jo Jorgenson";
        os[9][3] = "Howie Hawkins";

        //Title
        pl("---THE 2020 PRESIDENTIAL ELECTION AND PRIMARIES---");
        space();
        //Length is used for random number generation
        int length = qRem.length;
        while (length>0){
            int num = rand.nextInt(length);//Makes random number up to length 
            q = qRem[num];//Grabs a question from the questions remaining array with that value
            //Prints the question 
            pl(qs[q]);
            space();
            //Prints the potential answers
            while(o<numOs){
                System.out.print((o+1) + ": ");
                pl(os[q][o]);
                o+=1;
            }
            o=0; //Resets options index
            //Gets user input
            while (!valid) {
                p("Answer: ");
                try{
                    //Try getting a string input from the user
                    userInput = intInput();
                    space();
                    valid = true;
                }
                catch (Exception e){
                    //If unsuccesful, tell the user
                    pl("That was not valid input. Please try again.");
                    space();
                }
            }
            valid = false; //Resets validity
            //Print success or failure
            if (userInput == as[q]+1){
                pl("Correct!");
                score++;
                space();
            }
            else{
                pl("WRONG!");
                space();
            }
            //Creates a temporary array to remove a used value from another array.
            Integer TEMPqRem [] = new Integer [qRem.length];
            int i2 = 0;
            //Creates temporary array without the used question index
            for (int i=0; i<length; i++){
                if (i == num){
                    continue;
                }
                else{
                    TEMPqRem[i2] = qRem[i];
                }
                i2++;
            }
            //Sets the array to the temporary one
            qRem = TEMPqRem;
            //Decrements Length
            length--;
        }
        //Prints Score
        space();
        pl("Score: " + score + "/" + numQs);
    }
}


