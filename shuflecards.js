var game = {
    deck: {
        cards: [],
        init: function() {
            for (var suit in ["Spades", "Clubs", "Diamonds", "Hearts"]){
                for (var rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]) {
                    this.cards.push({suit: suit, rank: rank})