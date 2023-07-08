package com.example.afinal;

import android.content.Intent;
import android.os.Bundle;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.Toast;

import com.opencsv.bean.CsvToBeanBuilder;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import com.example.afinal.TonyAwardWinner;
import java.util.List;
import java.util.Set;
import androidx.appcompat.app.AppCompatActivity;
import android.view.Gravity;
import androidx.appcompat.widget.Toolbar;
import android.util.TypedValue;
import androidx.core.content.ContextCompat;

public class FlashcardsActivity extends AppCompatActivity {
    List<TonyAwardWinner> winners;
    Set<String> categories = new HashSet<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Toolbar toolbar = new Toolbar(this);
        toolbar.setLayoutParams(new Toolbar.LayoutParams(Toolbar.LayoutParams.MATCH_PARENT, (int) TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, 40, getResources().getDisplayMetrics())));
        toolbar.setBackgroundColor(ContextCompat.getColor(this, R.color.purple_200));
        toolbar.setElevation(4);

        Button backToHomeButton = new Button(this);
        Toolbar.LayoutParams layoutParams = new Toolbar.LayoutParams(Toolbar.LayoutParams.WRAP_CONTENT, Toolbar.LayoutParams.WRAP_CONTENT);
        layoutParams.gravity = Gravity.END;
        backToHomeButton.setLayoutParams(layoutParams);
        backToHomeButton.setText("Back to Home");
        backToHomeButton.setOnClickListener(v -> {
            Intent intent = new Intent(FlashcardsActivity.this, HomePageActivity.class);
            startActivity(intent);
        });
        toolbar.addView(backToHomeButton);
        setSupportActionBar(toolbar);

        try {
            winners = new CsvToBeanBuilder<TonyAwardWinner>(new FileReader(new File(getFilesDir(), "tonys.csv")))
                    .withType(TonyAwardWinner.class).build().parse();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        for (TonyAwardWinner winner : winners) {
            categories.add(winner.getCategory());
        }

        ScrollView scrollView = new ScrollView(this);
        LinearLayout linearLayout = new LinearLayout(this);
        linearLayout.setOrientation(LinearLayout.VERTICAL);
        scrollView.addView(linearLayout);

        for (String category : categories) {
            Button button = new Button(this);
            button.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));
            button.setText(category);
            button.setOnClickListener(v -> {
                Intent intent = new Intent(FlashcardsActivity.this, FlashcardDisplayActivity.class);
                intent.putExtra("selectedCategory", category);
                startActivity(intent);
            });
            linearLayout.addView(button);
        }

        LinearLayout mainLayout = new LinearLayout(this);
        mainLayout.setOrientation(LinearLayout.VERTICAL);
        mainLayout.addView(toolbar);
        mainLayout.addView(scrollView);

        setContentView(mainLayout);
    }
}
