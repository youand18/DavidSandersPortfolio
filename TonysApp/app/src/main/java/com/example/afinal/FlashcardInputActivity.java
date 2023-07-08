package com.example.afinal;

import android.content.Context;
import android.content.Intent;
import android.content.res.Resources;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.afinal.TonyAwardWinner;
import com.opencsv.CSVWriter;
import com.opencsv.bean.CsvToBeanBuilder;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FlashcardInputActivity extends AppCompatActivity {

    private EditText editTextYearWon;
    private Spinner spinnerCategoryWon;
    private EditText editTextWhoWon;
    private EditText editTextWhatShowWon;

    private List<TonyAwardWinner> winners;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_flashcard_input);

        editTextYearWon = findViewById(R.id.editTextYearWon);
        spinnerCategoryWon = findViewById(R.id.spinnerCategoryWon);
        editTextWhoWon = findViewById(R.id.editTextWhoWon);
        editTextWhatShowWon = findViewById(R.id.editTextWhatShowWon);
        Button backToHomeButton = findViewById(R.id.backToHomeButton);
        backToHomeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(FlashcardInputActivity.this, HomePageActivity.class);
                startActivity(intent);
            }
        });
        // Load the winners list from the CSV file
        try {
            winners = new CsvToBeanBuilder<TonyAwardWinner>(new FileReader(new File(getFilesDir(), "tonys.csv")))
                    .withType(TonyAwardWinner.class).build().parse();
        } catch (Exception e) {
            e.printStackTrace();
            Toast.makeText(FlashcardInputActivity.this, "Failed to load the CSV file.", Toast.LENGTH_SHORT).show();
        }

        // Get the categories from the winners list
        List<String> categories = getCategories();

        // Set up the spinner with categories
        ArrayAdapter<String> spinnerAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, categories) {
            @Override
            public View getDropDownView(int position, View convertView, ViewGroup parent) {
                View view = super.getDropDownView(position, convertView, parent);
                TextView textView = (TextView) view;
                textView.setTextSize(12); // Adjust the text size as per your requirement
                return view;
            }
        };
        spinnerAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinnerCategoryWon.setAdapter(spinnerAdapter);

        Button buttonSubmit = findViewById(R.id.buttonSubmit);
        buttonSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String yearWon = editTextYearWon.getText().toString();
                String categoryWon = spinnerCategoryWon.getSelectedItem().toString();
                String whoWon = editTextWhoWon.getText().toString();
                String whatShowWon = editTextWhatShowWon.getText().toString();

                // Generate the data line to be appended
                String dataLine = yearWon + "," + categoryWon + "," + whoWon + "," + whatShowWon;

                // Append the data to the CSV file
                appendDataToCSV(dataLine);
            }
        });
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

    private void appendDataToCSV(String dataLine) {
        try {
            File file = new File(getFilesDir(), "tonys.csv");
            FileWriter writer = new FileWriter(file, true);
            PrintWriter printWriter = new PrintWriter(writer);

            // Append the new data line with a line separator
            printWriter.print(System.lineSeparator());
            printWriter.print(dataLine);

            // Close the writer
            printWriter.close();

            // Show success message
            Toast.makeText(this, "Data appended successfully to the CSV file.", Toast.LENGTH_SHORT).show();
        } catch (IOException e) {
            e.printStackTrace();
            // Show failure message
            Toast.makeText(this, "Failed to append data to the CSV file.", Toast.LENGTH_SHORT).show();
        }
    }
}
