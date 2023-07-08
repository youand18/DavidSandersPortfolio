package com.example.afinal;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import androidx.appcompat.widget.Toolbar;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.content.Intent;
import android.widget.Toast;

import com.opencsv.bean.CsvToBeanBuilder;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

public class MainActivity extends AppCompatActivity {

    public List<TonyAwardWinner> winners;
    private boolean isAnswered = false;

    private Set<Integer> askedQuestions = new HashSet<>();
    TonyAwardWinner currentWinner;
    private Random rand;
    public int correctGuesses = 0;
    public int incorrectGuesses = 0;
    public TextView questionTextView;
    public Button[] options = new Button[4];
    private Button submitButton;
    public TextView resultTextView;
    private TextView correctTextView;
    private TextView incorrectTextView;
    private Spinner categorySpinner;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        askedQuestions = new HashSet<>();
        rand = new Random();
        try {
            winners = new CsvToBeanBuilder<TonyAwardWinner>(new FileReader(new File(getFilesDir(), "tonys.csv")))
                    .withType(TonyAwardWinner.class).build().parse();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

        questionTextView = findViewById(R.id.questionText);
        resultTextView = findViewById(R.id.resultText);
        correctTextView = findViewById(R.id.correctText);
        correctTextView.setText("Correct Guesses: " + correctGuesses);
        incorrectTextView = findViewById(R.id.incorrectText);
        incorrectTextView.setText("Incorrect Guesses: " + incorrectGuesses);
        Button backToHomeButton = findViewById(R.id.backToHomeButton);
        backToHomeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, HomePageActivity.class);
                startActivity(intent);
            }
        });
        categorySpinner = findViewById(R.id.categorySpinner);

        // Get the available categories from the winners list
        List<String> categories = getCategories();

        // Set up the spinner adapter
        ArrayAdapter<String> spinnerAdapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, categories);
        spinnerAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        categorySpinner.setAdapter(spinnerAdapter);

        options[0] = findViewById(R.id.option1);
        options[1] = findViewById(R.id.option2);
        options[2] = findViewById(R.id.option3);
        options[3] = findViewById(R.id.option4);

        for (Button option : options) {
            option.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    if (!isAnswered) {
                        checkAnswer(((Button) v).getText().toString());
                        isAnswered = true; // Set the flag to true
                    }
                }
            });
        }
        generateQuestion();
    }

    public void generateQuestion() {
        isAnswered = false;

        int winnerIndex = rand.nextInt(winners.size());
        currentWinner = winners.get(winnerIndex);

        // Get the selected category from the Spinner
        String selectedCategory = categorySpinner.getSelectedItem().toString();

        askedQuestions = new HashSet<>();

        if (askedQuestions.size() == winners.size()) {
            // All questions for the selected category have been asked
            askedQuestions.clear();
        }

        // Find a new question that hasn't been asked
        do {
            winnerIndex = rand.nextInt(winners.size());
        } while (askedQuestions.contains(winnerIndex) || !winners.get(winnerIndex).getCategory().equals(selectedCategory));

        currentWinner = winners.get(winnerIndex);

        // Add the current question index to the askedQuestions set
        askedQuestions.add(winnerIndex);

        // Check if the current question's category matches the selected category
        while (!currentWinner.getCategory().equals(selectedCategory)) {
            winnerIndex = rand.nextInt(winners.size());
            currentWinner = winners.get(winnerIndex);
        }
        questionTextView.setText(String.format("Who won the Tony for '%s' in %s?", currentWinner.getCategory(), currentWinner.getYear()));

        int correctOption = rand.nextInt(4);
        Set<String> incorrectOptions = new HashSet<>();
        while (incorrectOptions.size() < 3) {
            int incorrectIndex = rand.nextInt(winners.size());
            TonyAwardWinner incorrectWinner = winners.get(incorrectIndex);
            if (!incorrectWinner.getWinner().equals(currentWinner.getWinner()) && incorrectWinner.getCategory().equals(currentWinner.getCategory())){
                incorrectOptions.add(incorrectWinner.getWinner());
            }
        }

        List<String> allOptions = new ArrayList<>(incorrectOptions);
        allOptions.add(correctOption, currentWinner.getWinner());

        for (int i = 0; i < 4; i++){
            options[i].setText(allOptions.get(i));
            options[i].setBackgroundColor(Color.MAGENTA); // Set background color to blue
        }
    }
    private List<String> getCategories() {
        List<String> categories = new ArrayList<>();

        for (TonyAwardWinner winner : winners) {
            String category = winner.getCategory();
            if (!categories.contains(category)) {
                categories.add(category);
            }
        }

        return categories;
    }

    public void checkAnswer(String answer) {
        // Disable the options buttons to prevent further user interaction
    /*for (Button option : options) {
        option.setEnabled(false);
    }*/

        if (answer.equals(currentWinner.getWinner())) {
            resultTextView.setText("Correct!");
            correctGuesses++;
            correctTextView.setText("Correct Guesses: " + correctGuesses);
        } else {
            incorrectGuesses++;
            resultTextView.setText("Sorry, that's incorrect!");
            incorrectTextView.setText("Incorrect Guesses: " + incorrectGuesses);
            int selectedOptionIndex = -1;
            int i;
            for (i = 0; i < options.length; i++) {
                if (options[i].getText().toString().equals(answer)) {
                    selectedOptionIndex = i;
                    break;
                }
            }
            options[i].setBackgroundColor(Color.RED);
        }

        // Find the index of the correct answer option
        int correctOptionIndex = -1;
        for (int i = 0; i < options.length; i++) {
            if (options[i].getText().toString().equals(currentWinner.getWinner())) {
                correctOptionIndex = i;
                break;
            }
        }

        // Change the background color of the correct answer button to green
        options[correctOptionIndex].setBackgroundColor(Color.GREEN);

        int finalCorrectOptionIndex = correctOptionIndex;
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                // Reset the background color of the correct answer button
                options[finalCorrectOptionIndex].setBackgroundColor(Color.BLUE);

                // Enable the options buttons
            /*for (Button option : options) {
                option.setEnabled(true);
            }*/

                generateQuestion();
            }
        }, 3000); // Delay for two seconds before generating the next question
    }


   /* private void flashCorrectOption() {
        // Find the index of the correct answer option
        int correctOptionIndex = -1;
        for (int i = 0; i < options.length; i++) {
            if (options[i].getText().toString().equals(currentWinner.getWinner())) {
                correctOptionIndex = i;
                break;
            }
        }

        // Flash the correct answer option by changing its background color multiple times
        int numFlashes = 9; // Number of times to flash the correct option
        int flashDuration = 100; // Duration of each flash in milliseconds

        for (int i = 0; i < numFlashes; i++) {
            final int finalI = i;
            int finalCorrectOptionIndex = correctOptionIndex;
            new Handler().postDelayed(new Runnable() {
                @Override
                public void run() {
                    if (finalI % 2 == 0) {
                        // Set the background color to green during even flashes
                        options[finalCorrectOptionIndex].setBackgroundResource(android.R.color.holo_green_light);
                    } else {
                        // Set the background color to the default color during odd flashes
                        options[finalCorrectOptionIndex].setBackgroundResource(android.R.color.transparent);
                    }
                }
            }, i * flashDuration);
        }
    }
*/
}