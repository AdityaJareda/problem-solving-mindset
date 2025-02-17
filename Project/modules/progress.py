import json
import os

topics={
        1: 'Variables',
        2: 'Data Types',
        3: 'Control Flow',
        4: 'Loops',
        5: 'Functions',
        6: 'List & Tuples',
        7: 'Dictionaries',
        8: 'File Handling',
        9: 'Exception Handling',
        10: 'Modules and Imports',
    }

progress_file='Project/modules/progress.json'

def save_progress(progress):
    try:
        with open(progress_file, 'w') as file:
            json.dump(progress, file, indent=4)
    except IOError:
        print('Enable to save progress.')

def load_progress():
    if not os.path.exists(progress_file):
        return {'completed_topics': [],
               'quiz_score': {},
               'last_accessed': None}
    try:
        with open(progress_file, 'r') as file:
            progress=json.load(file)
            if 'completed_topics' not in progress:
                progress['completed_topics']=[]
            if 'quiz_score' not in progress:
                progress['quiz_score']={[]}
            if 'last_accessed' not in progress:
                progress['last_accessed']=None
            return progress
    except (FileNotFoundError, json.JSONDecodeError):
        print('Unable to load progress. Resetting progress.')
        return{'completed_topics': [],
               'quiz_score': {},
               'last_accessed': None}

def mark_topic_completed(topic_number, score):
    progress = load_progress()
    topic_name=topics.get(topic_number)
    if topic_name:
        if topic_name not in progress['completed_topics']:
            progress['completed_topics'].append(topic_name)
        progress['quiz_score'][topic_name] = score
        progress['last_accessed'] = topic_name
    else:
        print(f'Invalid topic number! Unable to load progress.')
    save_progress(progress)

def view_progress():
    progress = load_progress()
    print('\n_____ Learning Progress _____\n')
    completed_topics = ', '.join(str(topic) for topic in progress['completed_topics']) if progress['completed_topics'] else 'None'
    print(f'Completed Topics: {completed_topics}')
    print(f'Quiz Score: {progress["quiz_score"] if progress["quiz_score"] else "No quiz attempted"}')
    print(f'Last Accessed Topic: {progress["last_accessed"] if progress["last_accessed"] else "None"}')
    print('____________________________\n')
