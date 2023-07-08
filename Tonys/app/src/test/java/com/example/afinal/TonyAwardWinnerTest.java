package com.example.afinal;
import org.junit.Assert;
import org.junit.Test;

public class TonyAwardWinnerTest {
    @Test
    public void testGetYear() {
        TonyAwardWinner winner = new TonyAwardWinner();
        winner.setYear("2021");
        String expectedYear = "2021";
        String actualYear = winner.getYear();
        Assert.assertEquals(expectedYear, actualYear);
    }

    @Test
    public void testGetCategory() {
        TonyAwardWinner winner = new TonyAwardWinner();
        winner.setCategory("Best Musical");
        String expectedCategory = "Best Musical";
        String actualCategory = winner.getCategory();
        Assert.assertEquals(expectedCategory, actualCategory);
    }

    @Test
    public void testGetWinner() {
        TonyAwardWinner winner = new TonyAwardWinner();
        winner.setWinner("Some Winner");
        String expectedWinner = "Some Winner";
        String actualWinner = winner.getWinner();
        Assert.assertEquals(expectedWinner, actualWinner);
    }

    @Test
    public void testGetShow() {
        TonyAwardWinner winner = new TonyAwardWinner();
        winner.setShow("Some Show");
        String expectedShow = "Some Show";
        String actualShow = winner.getShow();
        Assert.assertEquals(expectedShow, actualShow);
    }
}
