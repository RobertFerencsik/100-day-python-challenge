student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60,
    'Bob': 70,
}

def scores_to_grades(scores):
    """
    Converts student scores to grades.
    Args:
        scores (dict): A dictionary of student scores.
    Returns:
        dict: A dictionary of student grades.
    """
    for key in scores:
        if scores[key] < 71:
            scores[key] = "Fail"
        elif 70 < scores[key] < 81:
            scores[key] = "Acceptable"
        elif 80 < scores[key] < 91:
            scores[key] = "Exceeds Expectations"
        else:
            scores[key] = "Outstanding"
    return scores


student_grades = scores_to_grades(student_scores)

print(student_grades)