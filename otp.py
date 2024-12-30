# OTP functions
def generate_otp(length=6):
    import random
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def validate_otp(input_otp, actual_otp):
    return input_otp == actual_otp

# Test cases
import unittest

class TestOTP(unittest.TestCase):
    def test_generate_otp_length(self):
        otp = generate_otp(6)
        self.assertEqual(len(otp), 6)

    def test_generate_otp_digits(self):
        otp = generate_otp(6)
        self.assertTrue(otp.isdigit())

    def test_validate_otp_correct(self):
        actual_otp = "123456"
        self.assertTrue(validate_otp("123456", actual_otp))

    def test_validate_otp_incorrect(self):
        actual_otp = "123456"
        self.assertFalse(validate_otp("654321", actual_otp))

if __name__ == "__main__":
    unittest.main()
