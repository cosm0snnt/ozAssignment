from flask import request, jsonify, render_template
from flask_smorest import Blueprint, abort


# Blueprint
def createPostsBlp(mysql):
    postsBlp = Blueprint("posts", __name__, description = "posts api", url_prefix = "/posts")

    @postsBlp.route("/")
    def posts():
        return render_template('posts.html')

    # 데코레이터, HTTP 메소드
    # .route는 URL 경로를 연결하는 메소드
    # 누군가 /posts/로 들어가 GET or POST 요청을 보내면
    # posts() 함수를 실행해라
    @postsBlp.route("/", methods = ["GET", "POST"])
    def posts():
        cursor = mysql.connection.cursor()

        # 게시글 조회: 만약 GET 요청을 받았다면~
        if request.method == "GET":
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
            posts = cursor.fetchall()
            cursor.close()

            # DB 대신
            postList = []

            # posts 안의 post를 가져오기
            for post in posts:
                postList.append({"id": post[0], "title": post[1], "content": post[2]})
            return postList
        

        # 게시글 작성(생성)
        elif request.method == "POST":
            title = request.json.get("title")
            content = request.json.get("content")

            # 예외 컨트롤
            if not title or not content:
                abort(400, msg = "title or content is missing")
                # abort(상태-코드, 옵션)
                # 상태 코드가 제일 중요해서 앞에 씀(에러만 처리하는 함수)
            
            sql = "INSERT INTO posts(title, content) VALUES(%s, %s)"
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            return jsonify({"message": "success"}, 201)
            # jsonify(데이터, 상태-코드)
            # 데이터가 제일 중요해서 앞에 씀(데이터를 json으로 변환하는 게 목적임)


    @postsBlp.route("/<int:id>", methods = ["GET", "PUT", "DELETE"])
    def post(id,):
        cursor = mysql.connection.cursor()

        # 글 조회하기
        if request.method == "GET":
            sql = f"SELECT * FROM posts WHERE id = {id}"
            cursor.execute(sql)
            post = cursor.fetchone()
            
            if not post:
                abort(404, msg = "Can't find this content")
                return {"id": post[0], "title": post[1], "content": post[2]}
        
        # 글 수정하기
        elif request.method == "PUT":
            title = request.json.get("title")
            content = request.json.get("content")
            
            if not title or not content:
                abort(400, msg = "Can't find title or content")

            # 1번째 쿼리문
            sql = "SELECT * FROM posts WHERE id = %s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(404, msg = "Can't find this content")
            
            # 2번째 쿼리문
            sql = "UPDATE posts SET title = %s, content = %s, WHERE id = %s"
            cursor.execute(sql, (title, content, id))
            mysql.connection.commit()

            return jsonify({"message": "Successfully updated title and content"})
            # 이 부분에 post.html이 들어가야 하지 않나?
        
        # 글 삭제하기
        elif request.method == "DELETE":
            # 1번째 쿼리문
            sql = "SELECT * FROM posts WHERE id = %s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(404, "Can't find this content")

            # 2번째 쿼리문
            sql = "DELETE FROM posts WHERE id = %s"
            cursor.execute(sql, (id,))
            mysql.connection.commit()
            return jsonify({"message": "Successfully deleted"})
        
    return postsBlp