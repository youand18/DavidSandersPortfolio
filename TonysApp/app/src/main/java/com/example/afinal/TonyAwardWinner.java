package com.example.afinal;

import com.opencsv.bean.CsvBindByName;

public class TonyAwardWinner {
    @CsvBindByName(column = "Year Won")
    private String year;

    @CsvBindByName(column = "Category Won")
    private String category;

    @CsvBindByName(column = "Who Won?")
    private String winner;

    @CsvBindByName(column = "What Show Was It? (Might Be Same as Last)")
    private String show;

    public String getYear() {
        return year;
    }
    public void setYear(String year) {
        this.year = year;
    }
    public String getCategory() {
        return category;
    }
    public void setCategory(String category) {
        this.category = category;
    }
    public String getWinner() {
        return winner;
    }
    public void setWinner(String winner) {
        this.winner = winner;
    }
    public String getShow() {
        return show;
    }
    public void setShow(String show) {
        this.show = show;
    }
}