def is_palindrome(s):
    s = ''.join([ch for ch in s if ch.isalpha()])
    s = s.lower()
    return s == s[::-1]

for s in ['racecar', 'mike', 'hello', 'helleh', "A Toyota’s a Toyota.",
          "Are we not drawn onward, we few, drawn onward to new era?", 
          '''Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era.''']:
    print("{:4} {}".format('yes' if is_palindrome(s) else 'no', s))


