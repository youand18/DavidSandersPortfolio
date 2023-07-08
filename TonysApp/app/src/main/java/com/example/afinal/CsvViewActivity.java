package com.example.afinal;

import android.content.Intent;
import android.content.SharedPreferences;
import android.content.res.Resources;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Spannable;
import android.text.SpannableString;
import android.text.TextUtils;
import android.text.style.ForegroundColorSpan;
import android.view.KeyEvent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.EditorInfo;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.opencsv.bean.CsvToBeanBuilder;
import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CsvViewActivity extends AppCompatActivity {
    private List<TonyAwardWinner> winners;
    private CsvAdapter adapter;
    private SharedPreferences sharedPreferences;
    private Spinner spinnerYear;
    private ArrayAdapter<String> yearAdapter;
    private List<String> yearsList;
    private EditText searchEditText;
    private EditText showSearchEditText;
    private TextView searchResultsTextView;
    private String searchQuery;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_csv_view);

        Button backToHomeButton = findViewById(R.id.backToHomeButton);
        backToHomeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(CsvViewActivity.this, HomePageActivity.class);
                startActivity(intent);
            }
        });

        RecyclerView recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        sharedPreferences = getSharedPreferences("CsvViewActivity", MODE_PRIVATE);
        searchEditText = findViewById(R.id.searchEditText);
        searchEditText.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                if (actionId == EditorInfo.IME_ACTION_SEARCH) {
                    searchQuery = searchEditText.getText().toString();
                    filterBySearchQuery();
                    return true;
                }
                return false;
            }
        });
        showSearchEditText = findViewById(R.id.showSearchEditText);
        showSearchEditText.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                if (actionId == EditorInfo.IME_ACTION_SEARCH) {
                    searchQuery = showSearchEditText.getText().toString();
                    filterByShowSearchQuery();
                    return true;
                }
                return false;
            }
        });
        searchResultsTextView = findViewById(R.id.searchResultsTextView);

        // Load the CSV data
        try {
            winners = new CsvToBeanBuilder<TonyAwardWinner>(new FileReader(new File(getFilesDir(), "tonys.csv")))
                    .withType(TonyAwardWinner.class).build().parse();
            adapter = new CsvAdapter(winners);
            recyclerView.setAdapter(adapter);

            yearsList = getYearsFromWinners();
            // Get the years from the winners list
            List<String> years = getYearsFromWinners();
            // Set up the spinner
            this.spinnerYear = findViewById(R.id.spinnerYear);
            ArrayAdapter<String> spinnerAdapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, years);
            spinnerAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
            spinnerYear.setAdapter(spinnerAdapter);
            spinnerYear.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
                @Override
                public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                    String selectedYear = yearsList.get(position);
                    adapter.filterByYear(selectedYear);
                }

                @Override
                public void onNothingSelected(AdapterView<?> parent) {
                    adapter.filterByYear(null);  // Show all winners when nothing is selected
                }
            });

        } catch (Exception e) {
            e.printStackTrace();
            Toast.makeText(CsvViewActivity.this, "Failed to load the CSV file.", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
    }

    private class CsvAdapter extends RecyclerView.Adapter<CsvAdapter.ViewHolder> {
        private List<TonyAwardWinner> allWinners;  // Original list of all winners
        private List<TonyAwardWinner> filteredWinners;  // Filtered list based on selected year

        public CsvAdapter(List<TonyAwardWinner> winners) {
            this.allWinners = winners;
            this.filteredWinners = new ArrayList<>(winners);  // Initialize with all winners initially
        }

        @NonNull
        @Override
        public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
            View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_csv_row, parent, false);
            return new ViewHolder(view);
        }

        @Override
        public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
            TonyAwardWinner winner = filteredWinners.get(position);
            holder.bind(winner);
        }

        @Override
        public int getItemCount() {
            return filteredWinners.size();
        }
        public void setFilteredWinners(List<TonyAwardWinner> filteredWinners) {
            this.filteredWinners.clear();
            this.filteredWinners.addAll(filteredWinners);
            notifyDataSetChanged();
        }

        public class ViewHolder extends RecyclerView.ViewHolder {
            private TextView textViewYearWon;
            private TextView textViewCategoryWon;
            private TextView textViewWhoWon;
            private TextView textViewWhatShowWon;
            private Button deleteButton;

            public ViewHolder(@NonNull View itemView) {
                super(itemView);

                textViewYearWon = itemView.findViewById(R.id.textViewYearWon);
                textViewCategoryWon = itemView.findViewById(R.id.textViewCategoryWon);
                textViewWhoWon = itemView.findViewById(R.id.textViewWhoWon);
                textViewWhatShowWon = itemView.findViewById(R.id.textViewWhatShowWon);
                /*deleteButton = itemView.findViewById(R.id.deleteButton);

                deleteButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        int position = getAdapterPosition();
                        if (position != RecyclerView.NO_POSITION) {
                            // Remove the item from both lists
                            TonyAwardWinner deletedWinner = filteredWinners.get(position);
                            winners.remove(deletedWinner);
                            filteredWinners.remove(position);

                            // Update the CSV file
                            updateCsvFile();

                            // Notify the adapter about the removed item
                            notifyItemRemoved(position);
                            notifyItemRangeChanged(position, filteredWinners.size());

                            // Show deletion success message
                            Toast.makeText(CsvViewActivity.this, "Row deleted successfully.", Toast.LENGTH_SHORT).show();
                        }
                    }
                });*/
            }

            public void bind(TonyAwardWinner winner) {
                textViewYearWon.setText(winner.getYear());
                textViewCategoryWon.setText(winner.getCategory());
                textViewWhoWon.setText(winner.getWinner());
                textViewWhatShowWon.setText(winner.getShow());

                highlightSearchQuery(textViewWhoWon, winner.getWinner());
                highlightSearchQuery(textViewWhatShowWon, winner.getShow());
            }

            private void highlightSearchQuery(TextView textView, String text) {
                if (searchQuery != null && !searchQuery.isEmpty() && text != null) {
                    SpannableString spannableString = new SpannableString(text);
                    int startIndex = text.toLowerCase().indexOf(searchQuery.toLowerCase());
                    int endIndex = startIndex + searchQuery.length();
                    if (startIndex >= 0) {
                        spannableString.setSpan(new ForegroundColorSpan(Color.RED), startIndex, endIndex, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE);
                        textView.setText(spannableString);
                    } else {
                        textView.setText(text); // Reset the text to original if search query is not found
                    }
                }
            }


        }

        public void filterByYear(String year) {
            filteredWinners.clear();  // Clear the previous filtered list

            if (TextUtils.isEmpty(year)) {
                filteredWinners.addAll(allWinners);  // If no year is selected, show all winners
            } else {
                // Filter the winners based on the selected year
                for (TonyAwardWinner winner : allWinners) {
                    if (TextUtils.equals(winner.getYear(), year)) {
                        filteredWinners.add(winner);
                    }
                }
            }

            notifyDataSetChanged();  // Notify the RecyclerView about the updated data
        }


        private void updateCsvFile() {
            try {
                File file = new File(getFilesDir(), "tonys.csv");

                FileWriter writer = new FileWriter(file, false); // Overwrite the existing file
                StatefulBeanToCsv<TonyAwardWinner> beanToCsv = new StatefulBeanToCsvBuilder<TonyAwardWinner>(writer)
                        .build();

                // Write only non-empty rows to the CSV file
                List<TonyAwardWinner> nonEmptyWinners = new ArrayList<>();
                for (TonyAwardWinner winner : winners) {
                    if (isRowEmpty(winner)) {
                        continue;  // Skip empty rows
                    }
                    nonEmptyWinners.add(winner);
                }

                beanToCsv.write(nonEmptyWinners);
                writer.close();
            } catch (Exception e) {
                e.printStackTrace();
                // Show failure message
                Toast.makeText(CsvViewActivity.this, "Failed to update the CSV file.", Toast.LENGTH_SHORT).show();
            }
        }

        private boolean isRowEmpty(TonyAwardWinner winner) {
            return winner.getYear() == null || winner.getCategory() == null ||
                    winner.getWinner() == null || winner.getShow() == null;
        }
    }

    private List<String> getYearsFromWinners() {
        List<String> years = new ArrayList<>();

        for (TonyAwardWinner winner : winners) {
            String year = winner.getYear();
            if (!TextUtils.isEmpty(year) && !years.contains(year)) {
                years.add(year);
            }
        }

        // Sort the years in ascending order
        Collections.sort(years);

        return years;
    }
    private void filterBySearchQuery() {
        String searchQuery = searchEditText.getText().toString().toLowerCase().trim();

        List<TonyAwardWinner> searchResults = new ArrayList<>();

        for (TonyAwardWinner winner : winners) {
            String whoWon = winner.getWinner();
            String show = winner.getShow();

            if (whoWon != null && whoWon.toLowerCase().contains(searchQuery)) {
                searchResults.add(winner);
            } else if (show != null && show.toLowerCase().contains(searchQuery)) {
                searchResults.add(winner);
            }
        }

        adapter.setFilteredWinners(searchResults);

        int numResults = searchResults.size();
        String resultText = numResults + " matching result" + (numResults != 1 ? "s" : "");
        searchResultsTextView.setText(resultText);
    }

    private void filterByShowSearchQuery() {
        String searchQuery = showSearchEditText.getText().toString().toLowerCase().trim();

        List<TonyAwardWinner> searchResults = new ArrayList<>();

        for (TonyAwardWinner winner : winners) {
            String show = winner.getShow();

            if (show != null && show.toLowerCase().contains(searchQuery)) {
                searchResults.add(winner);
            }
        }

        adapter.setFilteredWinners(searchResults);

        int numResults = searchResults.size();
        String resultText = numResults + " matching result" + (numResults != 1 ? "s" : "");
        searchResultsTextView.setText(resultText);
    }
}
