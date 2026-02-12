#!/usr/bin/env python3
"""
Python Math Calculator - Terminal Edition

A simple yet powerful calculator that runs in the terminal.
Supports basic arithmetic operations and mathematical expressions.
"""

import sys
import re


def evaluate_expression(expression):
    """
    Safely evaluate a mathematical expression.
    
    Args:
        expression (str): The mathematical expression to evaluate
        
    Returns:
        float: The result of the evaluation
        
    Raises:
        ValueError: If the expression is invalid
        ZeroDivisionError: If division by zero is attempted
    """
    # Remove whitespace
    expression = expression.strip()
    
    # Basic validation - only allow numbers, operators, parentheses, and decimal points
    if not re.match(r'^[0-9+\-*/().\s]+$', expression):
        raise ValueError("Invalid characters in expression. Only numbers and operators (+, -, *, /, parentheses) are allowed.")
    
    # Check for empty expression
    if not expression:
        raise ValueError("Empty expression")
    
    try:
        # Use eval with a restricted namespace for safety
        # Only allow basic math operations
        result = eval(expression, {"__builtins__": {}}, {})
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")
    except SyntaxError:
        raise ValueError("Invalid mathematical expression")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {str(e)}")


def print_welcome():
    """Print welcome message and instructions."""
    print("=" * 50)
    print("Python Math Calculator".center(50))
    print("=" * 50)
    print("\nWelcome! Enter mathematical expressions to calculate.")
    print("\nSupported operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  () : Parentheses for grouping")
    print("\nExamples:")
    print("  2 + 2")
    print("  (5 + 3) * 2")
    print("  10 / 2 - 1")
    print("\nType 'quit' or 'exit' to close the calculator.")
    print("=" * 50)


def main():
    """Main calculator loop."""
    print_welcome()
    
    while True:
        try:
            # Get user input
            user_input = input("\n>>> ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using Python Math Calculator!")
                break
            
            # Skip empty input
            if not user_input:
                continue
            
            # Evaluate and display result
            result = evaluate_expression(user_input)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
