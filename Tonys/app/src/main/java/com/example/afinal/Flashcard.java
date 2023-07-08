package com.example.afinal;

public class Flashcard {
    private String year;
    private String show;
    private String winner;

    public Flashcard(String year, String show, String winner) {
        this.year = year;
        this.show = show;
        this.winner = winner;
    }
    public String getYear() {
        return year;
    }

    public String getShow() {
        return show;
    }

    public String getWinner() {
        return winner;
    }

    public String getFront() {
        return year + " - " + show;
    }

    public String getBack() {
        return winner;
    }
}
