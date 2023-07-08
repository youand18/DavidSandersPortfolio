package com.example.afinal;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.opencsv.bean.CsvToBeanBuilder;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class FlashcardDisplayActivity extends AppCompatActivity {
    private List<Flashcard> flashcards;
    private List<Flashcard> originalOrder = new ArrayList<>();
    private int currentIndex = 0;
    private boolean isShowingBack = false;
    private TextView flashcardTextView;
    List<TonyAwardWinner> winners;
    Set<String> categories = new HashSet<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_flashcard_display);



        String selectedCategory = getIntent().getStringExtra("selectedCategory");
        if (getSupportActionBar() != null) {
            getSupportActionBar().setTitle(selectedCategory);
        }
        flashcards = new ArrayList<>();
        try {
            winners = new CsvToBeanBuilder<TonyAwardWinner>(new FileReader(new File(getFilesDir(), "tonys.csv")))
                    .withType(TonyAwardWinner.class).build().parse();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        for (TonyAwardWinner winner : winners) {
            if (winner.getCategory().equals(selectedCategory)) {
                Flashcard flashcard = new Flashcard(winner.getYear(), winner.getShow(), winner.getWinner());
                flashcards.add(flashcard);
                originalOrder.add(flashcard);
            }
            categories.add(winner.getCategory());
        }
        Toolbar toolbar = findViewById(R.id.toolbar);

        setSupportActionBar(toolbar);
        if (getSupportActionBar() != null) {
            getSupportActionBar().setTitle(selectedCategory);
        }
        Button backToHomeButton = findViewById(R.id.backToHomeButton);
        backToHomeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flashcards = new ArrayList<>(originalOrder);
                currentIndex = 0;
                isShowingBack = false;
                Intent intent = new Intent(FlashcardDisplayActivity.this, HomePageActivity.class);
                startActivity(intent);
            }
        });
        flashcardTextView = findViewById(R.id.flashcardTextView);
        if (!selectedCategory.equals("Best Musical") && !selectedCategory.equals("Best Play") && !selectedCategory.equals("Best Revival of a Musical") && !selectedCategory.equals("Best Revival of a Play")){
            flashcardTextView.setText(flashcards.get(currentIndex).getFront());
        } else {
            flashcardTextView.setText(flashcards.get(currentIndex).getYear());
        }


        Button flipButton = findViewById(R.id.flipButton);
        flipButton.setOnClickListener(v -> {
           isShowingBack = !isShowingBack;
           if (!selectedCategory.equals("Best Musical") && !selectedCategory.equals("Best Play") && !selectedCategory.equals("Best Revival of a Musical") && !selectedCategory.equals("Best Revival of a Play")) {
               if(isShowingBack) {
                   flashcardTextView.setText(flashcards.get(currentIndex).getBack());
               } else {
                   flashcardTextView.setText(flashcards.get(currentIndex).getFront());
               }
           } else {
               if(isShowingBack) {
                   flashcardTextView.setText(flashcards.get(currentIndex).getWinner());
               } else {
                   flashcardTextView.setText(flashcards.get(currentIndex).getYear());
               }

           }
        });

        Button nextButton = findViewById(R.id.nextButton);
        nextButton.setOnClickListener(v -> {
           currentIndex = (currentIndex + 1) % flashcards.size();
           isShowingBack = false;
            if (!selectedCategory.equals("Best Musical") && !selectedCategory.equals("Best Play") && !selectedCategory.equals("Best Revival of a Musical") && !selectedCategory.equals("Best Revival of a Play")){
                flashcardTextView.setText(flashcards.get(currentIndex).getFront());
            } else {
                flashcardTextView.setText(flashcards.get(currentIndex).getYear());
            }
        });
        Button shuffleButton = findViewById(R.id.shuffleButton);
        shuffleButton.setOnClickListener(v -> {
                Collections.shuffle(flashcards);
                currentIndex = 0;
                isShowingBack = false;
            if (!selectedCategory.equals("Best Musical") && !selectedCategory.equals("Best Play") && !selectedCategory.equals("Best Revival of a Musical") && !selectedCategory.equals("Best Revival of a Play")){
                flashcardTextView.setText(flashcards.get(currentIndex).getFront());
            } else {
                flashcardTextView.setText(flashcards.get(currentIndex).getYear());
            }
        });
    }
}