package com.example.afinal;

import org.junit.Assert;
import org.junit.Test;

public class FlashcardTest {
    @Test
    public void testGetFront(){
        Flashcard flashcard = new Flashcard("2022", "Test show", "Test winner");
        String expectedFront = "2022 - Test show";
        String actualFront = flashcard.getFront();
        Assert.assertEquals(expectedFront, actualFront);
    }
    @Test
    public void testGetBack(){
        Flashcard flashcard = new Flashcard("2022", "Test show", "Test winner");
        String expectedBack = "Test winner";
        String actualBack = flashcard.getBack();
        Assert.assertEquals(expectedBack, actualBack);
    }
}
