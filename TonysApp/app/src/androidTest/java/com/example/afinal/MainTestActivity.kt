package com.example.afinal
import androidx.test.core.app.ActivityScenario
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.action.ViewActions.click
import androidx.test.espresso.matcher.ViewMatchers.withId
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.withText
import androidx.test.filters.LargeTest
import junit.framework.TestCase.assertTrue
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith


//Can't get this to run!!!!

@RunWith(AndroidJUnit4::class)
@LargeTest
class MainTestActivity {

    @get:Rule
    val activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun testOption1Selection() {
        val scenario = ActivityScenario.launch(MainActivity::class.java)
        scenario.onActivity { activity ->
            val initialCorrectGuesses = activity.correctGuesses
            val initialIncorrectGuesses = activity.incorrectGuesses

            onView(withId(R.id.option1)).perform(click())

            val correctGuessesChanged = activity.correctGuesses != initialCorrectGuesses
            val incorrectGuessesChanged = activity.incorrectGuesses != initialIncorrectGuesses

            assertTrue(correctGuessesChanged xor incorrectGuessesChanged)

        }
    }

    @Test
    fun testOption2Selection() {
        val scenario = ActivityScenario.launch(MainActivity::class.java)
        scenario.onActivity { activity ->
            val initialCorrectGuesses = activity.correctGuesses
            val initialIncorrectGuesses = activity.incorrectGuesses

            onView(withId(R.id.option2)).perform(click())

            val correctGuessesChanged = activity.correctGuesses != initialCorrectGuesses
            val incorrectGuessesChanged = activity.incorrectGuesses != initialIncorrectGuesses

            assertTrue(correctGuessesChanged xor incorrectGuessesChanged)

        }
    }
    @Test
    fun testOption3Selection() {
        val scenario = ActivityScenario.launch(MainActivity::class.java)
        scenario.onActivity { activity ->
            val initialCorrectGuesses = activity.correctGuesses
            val initialIncorrectGuesses = activity.incorrectGuesses

            onView(withId(R.id.option3)).perform(click())

            val correctGuessesChanged = activity.correctGuesses != initialCorrectGuesses
            val incorrectGuessesChanged = activity.incorrectGuesses != initialIncorrectGuesses

            assertTrue(correctGuessesChanged xor incorrectGuessesChanged)

        }
    }
    @Test
    fun testOption4Selection() {
        val scenario = ActivityScenario.launch(MainActivity::class.java)
        scenario.onActivity { activity ->
            val initialCorrectGuesses = activity.correctGuesses
            val initialIncorrectGuesses = activity.incorrectGuesses

            onView(withId(R.id.option4)).perform(click())

            val correctGuessesChanged = activity.correctGuesses != initialCorrectGuesses
            val incorrectGuessesChanged = activity.incorrectGuesses != initialIncorrectGuesses

            assertTrue(correctGuessesChanged xor incorrectGuessesChanged)

        }
    }

}