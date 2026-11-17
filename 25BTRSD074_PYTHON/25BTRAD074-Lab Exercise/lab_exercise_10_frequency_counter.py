# Lab Exercise 10: Frequency Counter Using Dictionaries
# Student: Niranjan P G | USN: 25BTRAD074
import string

def count_frequencies(text):
    clean = text.translate(str.maketrans('', '', string.punctuation)).lower()
    freq = {}
    for word in clean.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

def main():
    print("=== Frequency Counter Using Dictionaries ===")
    passage = "python is versatile and easy. python is widely used in data science."
    print(f'Input: "{passage}"\n')
    word_freq = count_frequencies(passage)
    
    print(f"{'Word':<14} {'Count':<8} {'Distribution':<15}")
    print("-" * 38)
    for word, cnt in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word:<14} {cnt:<8} {'#' * (cnt * 4)}")
        
    print("\nSurvey Feedback (Language Preferences):")
    votes = ["Python", "Java", "Python", "C++", "Python", "Java", "Python"]
    for lang in sorted(set(votes)):
        print(f"{lang:<8}: {votes.count(lang)} votes")

if __name__ == "__main__":
    main()
