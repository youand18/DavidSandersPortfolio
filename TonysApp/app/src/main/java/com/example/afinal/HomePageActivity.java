package com.example.afinal;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class HomePageActivity extends AppCompatActivity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_page);

        copyCSVFileFromRaw();
        Button guessingGameButton = findViewById(R.id.guessingGameButton);
        Button flashcardsButton = findViewById(R.id.flashcardsButton);
        //Button inputButton = findViewById(R.id.inputButton);
        Button viewButton = findViewById(R.id.viewButton);
        guessingGameButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(HomePageActivity.this, MainActivity.class);
                startActivity(intent);
            }
        });
        flashcardsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(HomePageActivity.this, FlashcardsActivity.class);
                startActivity(intent);
            }
        });
         /*inputButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(HomePageActivity.this, FlashcardInputActivity.class);
                startActivity(intent);
            }
        });*/
        viewButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(HomePageActivity.this, CsvViewActivity.class);
                startActivity(intent);
            }
        });
    }
    private void copyCSVFileFromRaw() {
        File file = new File(getFilesDir(), "tonys.csv"); // Replace 'tonys.csv' with your desired file name

        if (!file.exists()) {
            try {
                InputStream inputStream = getResources().openRawResource(R.raw.tonys); // Replace 'tonys' with your actual CSV file name
                FileOutputStream outputStream = new FileOutputStream(file);
                byte[] buffer = new byte[1024];
                int length;
                while ((length = inputStream.read(buffer)) > 0) {
                    outputStream.write(buffer, 0, length);
                }
                outputStream.close();
                inputStream.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

}
