"""Unit tests for the emotion_detector function."""
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases verifying the dominant emotion for known inputs."""

    def test_joy(self):
        """Joyful text should be classified as joy."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """Angry text should be classified as anger."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Disgusted text should be classified as disgust."""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Sad text should be classified as sadness."""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Fearful text should be classified as fear."""
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
