import java.util.Scanner;

public class MadLibs {
    
    //Method to take input, returns int
    public static int intInput(){
        //Creates scanner and take user input
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        return a;
    }
    
    //Method to take input, returns double
    public static double doubleInput(){
        //Creates scanner and take user input
        Scanner input = new Scanner(System.in);
        double a = input.nextDouble();
        return a;
    }
    
    
    //Method to take input, returns String
    public static String strInput(){
        //Creates scanner and take user input
        Scanner input = new Scanner(System.in);
        String a = input.nextLine();
        return a;
    }

    //Method to print, saving typing time
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
        //Variable delclaration
        int i = 0;
        int numNouns = 4;
        int numVerbs = 3;
        int numAdjec = 3;
        int numAdver = 3;
        int numNums = 2;
        String nouns [] = new String [numNouns];
        String verbs [] = new String [numVerbs];
        String adjec [] = new String [numAdjec];
        String adver [] = new String [numAdver];
        Integer nums [] = new Integer [numNums];

        
        //Title
        pl("---MAD LIBS---");
        space();
        
        //Until the nouns have been filled
        while (i<numNouns) {
            //Instructions
            p("Input a noun: ");
            try{
                //Try getting a string input from the user
                nouns[i] = strInput();
                space();
                //If successful, add 1
                i+=1;
            }
            catch (Exception e){
                //If unsuccesful, tell the user
                pl("That was not valid input.");
                space();
            }
        }
        
        space();
        //Resets i
        i = 0;
        
        //Until the adjectives have been filled
        while (i<numAdjec) {
            //Instructions
            p("Input an adjective: ");
            try{
                //Try getting a string input from the user
                adjec[i] = strInput();
                space();
                //If successful, add 1
                i+=1;
            }
            catch (Exception e){
                //If unsuccesful, tell the user
                pl("That was not valid input.");
                space();
                i+=1;
            }
        }

        space();
        //Resets i
        i = 0;

        //Until the verbs have been filled
        while (i<numVerbs) {
            //Instructions
            p("Input a past-tense verb: ");
            try{
                //Try getting a string input from the user
                verbs[i] = strInput();
                space();
                //If successful, add 1
                i+=1;
            }
            catch (Exception e){
                //If unsuccesful, tell the user
                pl("That was not valid input.");
                space();
            }
        }

        space();
        //Resets i
        i = 0;

        //Until the adverbs have been filled
        while (i<numAdver) {
            //Instructions
            p("Input an adverb: ");
            try{
                //Try getting a string input from the user
                adver[i] = strInput();
                space();
                //If successful, add 1
                i+=1;
            }
            catch (Exception e){
                //If unsuccesful, tell the user
                pl("That was not valid input.");
                space();
            }
        }

        space();
        //Resets i
        i = 0;

        //Until the numbers have been filled
        while (i<numNums) {
            //Instructions
            p("Input a number: ");
            try{
                //Try getting a string input from the user
                nums[i] = intInput();
                space();
                if (nums[i] <= 0){
                    throw new Exception();
                }
                //If successful, add 1
                i+=1;
            }
            catch (Exception e){
                //If unsuccesful, tell the user
                pl("That was not valid input.");
                space();
            }
        }
       
        pl("The " + adjec[0] + " " + nouns[0] + " " + adver[0] + " " + verbs[0] + " towards the " + nums[0] + " people.");
        pl("Then the " + nums[1] + " birds " + adver[1] + " " + verbs[1] + " the " + adjec[1] + " " + nouns[1]);
        pl("At the end of the day, the best " + nouns[2] + "s are the " + adjec[0] + " ones who love to " + adver[2] + " eat " + nouns[3] + ", or have even " + verbs[2] + " " + nouns[3] + "s .");
    }
}


