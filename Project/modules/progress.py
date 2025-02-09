import json

progress_file='Project/modules/progress.json'

def save_progress(progress):
    with open(progress_file, 'w') as file:
        json.dump(progress, file, indent=4)

def load_progress():
    try:
        with open(progress_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return{'completed_topics': [],
               'quiz_scores': {},
               'last_accessed': None}

def mark_topic_completed(topic, score):
    progress = load_progress()
    if topic not in progress['completed_topics']:
        progress['completed_topics'].append(topic)
    progress['quiz_scores'][topic] = score
    progress['last_accessed'] = topic
    save_progress(progress)

def view_progress():
    progress = load_progress()
    print('\n_____ Learning Progress _____')
    print('Completed Topics:', ', '.join(progress['completed_topics']) if progress['completed_topics'] else 'None')
    print('Quiz Scores:', progress['quiz_scores'] if progress['quiz_scores'] else 'No quizzes attempted')
    print('Last Accessed Topic:', progress['last_accessed'] if progress['last_accessed'] else 'None')
    print('____________________________\n')