import tornado.web
import tornado.ioloop
import json
import os

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world ! Response from server")

class animalRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryParamtHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"Integer {num} is {r}")
        else:
            self.write(f"{num} is not a valid integer") 

class fruitsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        path = os.path.abspath("C:/SRDEV\Personal/python/Udemy/WebServer/fruits.txt")
        fh = open(path, "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        path = os.path.abspath("C:/SRDEV\Personal/python/Udemy/WebServer/fruits.txt")
        fh = open(path, "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message":"Fruit added successfully"}))


class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName} to course {courseId}")                  

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/animals", animalRequestHandler),
        (r"/isEven", queryParamtHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
        (r"/fruits",fruitsRequestHandler)
    ])

    port = 8080
    app.listen(port)
    print(f"App is listening on prt {port}")
    tornado.ioloop.IOLoop.current().start()