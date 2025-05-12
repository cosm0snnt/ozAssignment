# import
from pymongo import MongoClient

# RESET: START
# def insert_data(): START
def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용

    # 책 데이터 삽입
    books = \
    [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009}
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = \
    [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = \
    [
        {"user_id": 1, "action": "click", "timestamp": "2023-04-12T08:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-12T09:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T10:00:00Z"}
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")
    client.close()
# def insert_data(): END
# RESET: END

# 문제 1: 특정 장르의 책 찾기 START
def findBooksByGenre():
    booksCollection = db.books
    query = {"genre": "fantasy"} # 검색용 쿼리
    projection = {"_id": 0, "title": 1, "author": 1} # 정리용 필드(0: exclude/1: include)

    findBooks = booksCollection.find(query, projection)
    for book in findBooks:
        print(book)
# 문제 1: 특정 장르의 책 찾기 END

# 문제 2: 감독별 평균 영화 평점 계산 START
def calAverageRatingsByDirector():
    moviesCollection = db.movies
    # 파이프라인: 데이터를 여러 단계에 걸쳐 처리할 수 있게 만든 도구
    # pipeline = [{"$first": {...}}, {"$second": {...}}...]
    pipeline1 = \
    [
        {"$group" : {"_id": "$director", "averageRatings": {"$avg": "$rating"}}},
        {"$sort": {"averageRatings": -1}} # 내림차순
    ]

    calAverage = moviesCollection.aggregate(pipeline1)
    for rating in calAverage:
        print(rating)
# 문제 2: 감독별 평균 영화 평점 계산 END

# 문제 3: 특정 사용자의 최근 행동 조회 START
def findRecentActions(db, user_id, limit = 5):
    userActionsCollection = db.user_actions
    query = {"user_id": user_id}
    sort = [("timestamp", -1)]

    userActions = userActionsCollection.find(query, sort).limit(limit)
    for action in userActions:
        print(action)
# 문제 3: 특정 사용자의 최근 행동 조회 END

# 문제 4: 출판 연도별 책의 수 계산 START
def calBooksByYear():
    booksList = db.books
    pipeline2 = \
    [
        {"$group" : {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]

    calBooks = booksList.aggrgate(pipeline2)
    for book in calBooks:
        print(book)
# 문제 4: 출판 연도별 책의 수 계산 END

# 문제 5: 특정 사용자의 행동 유형 업데이트 START
def updateUserActions(db, user_id, oldAction, newAction, date):
    updateUser = db.users
    query = {"user_id": user_id, "action": oldAction, "timestamp": {"$lt": date}} # lt = less than
    update = {"$set": {"action": newAction}}

    updateResult = updateUser.update_many(query, update)
    print(f"Finished: Upload {updateResult}.")
# 문제 5: 특정 사용자의 행동 유형 업데이트 END

# main: START
if __name__ == "__main__":
    # insert_data() 이미 데이터는 다 삽입했으므로 주석 처리
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용
    findBooksByGenre() # 문제 1
    calAverageRatingsByDirector() # 문제 2
    findRecentActions() # 문제 3
    calBooksByYear() # 문제 4
    updateUserActions(db, 1, "view", "seen", "2023-04-10") # 문제 5
# main: END