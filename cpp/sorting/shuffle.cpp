/*
 * Shuffle a deck of cards (modelled as ints from 0 to 51) with equal
 * probability of each of the 52! permutations (CtCI problem 18.2).
 *
 * Author: Jonathan Johnston
 * Date: 2016/2/8
 */
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <random>

std::random_device rd; // "truly" random system device

/*
 * Generate a random number from 0 to 1 as a double.
 */
double generate_random()
{
    return static_cast<double>(rd()) / rd.max();
}

/*
 * Card class which defines a card of some integer value.
 */
class Card
{
    int value;
public:
    Card() { value = 0; }
    Card(int val) { value = val; }
    
    int get_value() const { return value; }
};

/*
 * Shuffle a deck of cards with equal probability of any of the 52!
 * permutations.
 */
std::vector<Card> shuffle(const std::vector<Card>& deck) {
    size_t rand;
    size_t num_cards = deck.size();
    std::vector<Card> shuffled(num_cards, Card()); // new deck
    size_t indexes[num_cards]; // hold memory of which cards shuffled
    
    // fill index with range
    for (size_t i = 0; i < num_cards; ++i) {
        indexes[i] = i;
    }

    // choose random card to shuffle
    for (size_t i = 0; i < num_cards; ++i) {
        // for equal probablilities use floor with 0 to num_cards,
        // as a simple round would be unequal for end ranges.
        // (ex. 0 chosen for only 0 to 0.5, but 1 chosen from 0.5 to 1.5)
        do { 
            rand = floor(generate_random() * (num_cards - i));
        } while (rand == (num_cards - i)); // don't choose end of range

        shuffled[i] = deck[indexes[rand]]; // add chosen card to new deck

        // here we put the randomly chosen cards to the end of the index,
        // and don't consider them again (they're "dead")
        size_t tmp = indexes[rand];
        indexes[rand] = indexes[num_cards - 1 - i];
        indexes[num_cards - 1 - i] = tmp;
    }

    return shuffled;
}

int main()
{
    // create and fill the deck
    std::vector<Card> deck(52, Card(0));
    for (size_t i = 0; i < 52; ++i) {
        deck[i] = Card(static_cast<int>(i));
    }

    // shuffle it and show it
    std::vector<Card> shuffled = shuffle(deck);
    std::cout << "Shuffled order:\n";
    for (std::vector<Card>::const_iterator it = shuffled.begin();
            it != shuffled.end(); ++it)
    {
        std::cout << it->get_value() << ", ";
    }

    return 0;
}
