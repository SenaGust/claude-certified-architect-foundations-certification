import math
from main import calculate_pi_to_5th_digit


def test_calculate_pi_to_5th_digit():
    """Test that our pi calculation is accurate to the 5th digit"""
    
    # Get our calculated value
    calculated_pi = calculate_pi_to_5th_digit()
    
    # Get the expected value from math library
    expected_pi = math.pi
    
    print("Testing calculate_pi_to_5th_digit():")
    print(f"Calculated PI:  {calculated_pi:.15f}")
    print(f"Expected PI:    {expected_pi:.15f}")
    print(f"Difference:     {abs(calculated_pi - expected_pi):.2e}")
    
    # Check if it matches to at least 5 decimal places
    calculated_5th = round(calculated_pi, 5)
    expected_5th = round(expected_pi, 5)
    
    print(f"\nCalculated (5 decimals): {calculated_5th}")
    print(f"Expected (5 decimals):   {expected_5th}")
    
    # Assertion
    assert calculated_5th == expected_5th, f"Pi to 5th digit mismatch! Got {calculated_5th}, expected {expected_5th}"
    print("\n✓ Test PASSED! Pi calculated correctly to 5th digit: 3.14159")


if __name__ == "__main__":
    test_calculate_pi_to_5th_digit()
