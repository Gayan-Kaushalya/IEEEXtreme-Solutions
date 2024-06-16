import sys

def difference(first, second):
    second = set(second)
    return [item for item in first if item not in second]

def solve(topics_to_cover, books, topic_counts):
    if len(topics_to_cover) == 0:
        return 0
    
    min_time = None
    selected_topic = topics_to_cover[0]
    
    for book_id in topic_counts[selected_topic]:
        book_time, book_topics = books[book_id]
        new_topics = difference(topics_to_cover[1:], book_topics)

        if min_time is not None:
            if book_time > min_time:
                continue

        optimal_time = book_time + solve(new_topics, books, topic_counts)

        if min_time is None:
            min_time = optimal_time
        else:
            min_time = min(min_time, optimal_time)

    return min_time

books = {}
topics_to_cover = []
topic_counts = {}

count = 0

input_lines = sys.stdin.readlines()

for line in input_lines:
    book_info = line.split()
    time = int(book_info[0])
    topics = book_info[1:]
    
    for topic in topics:
        if topic not in topic_counts:
            topic_counts[topic] = [str(count)]
        else:
            topic_counts[topic].append(str(count))

    new_topics = [t for t in topics if t not in topics_to_cover]
    topics_to_cover += new_topics

    books[str(count)] = [time, topics]
    count += 1
    
print(solve(topics_to_cover, books, topic_counts))