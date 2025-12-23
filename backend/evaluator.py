def evaluate_answer(user_answer, ideal_answer):
    if not user_answer.strip():
        return 0, "No answer provided."

    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([user_answer, ideal_answer])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    score = round(similarity * 100, 2)

    if score >= 80:
        feedback = "Excellent answer with strong conceptual clarity."
    elif score >= 55:
        feedback = "Good attempt, but some key points are missing."
    elif score >= 30:
        feedback = "Basic understanding shown. Needs improvement."
    else:
        feedback = "Answer is too weak or irrelevant."

    return score, feedback
