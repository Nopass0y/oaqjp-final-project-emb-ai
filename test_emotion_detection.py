import unittest
from EmotionDetection.emotion_detection import sentiment_analyzer

class TestEmotionDetection(unittest.TestCase): 
    def test1(self):
        self.assertEqual(sentiment_analyzer("I am glad this happened")['dominant_emotion'], "joy") 
        self.assertEqual(sentiment_analyzer("I am really mad about this")['dominant_emotion'], "anger") 
        self.assertEqual(sentiment_analyzer("I feel disgusted just hearing about this")['dominant_emotion'], "disgust") 
        self.assertEqual(sentiment_analyzer("I am so sad about this")['dominant_emotion'], "sadness") 
        self.assertEqual(sentiment_analyzer("I am really afraid that this will happen")['dominant_emotion'], "fear") 
        
unittest.main()