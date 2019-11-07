import web
import json


class Index:
    def GET(self):
        response = {
            'message': 'Simple python service',
            'version': '0.0.1'
        }
        web.header('Content-Type', 'application/json')
        return json.dumps(dict(response))


class PersonalHelloController:
    def GET(self, name):
        response = {
            'message': message(name)
        }
        web.header('Content-Type', 'application/json')
        return json.dumps(dict(response))


class HelloController:
    def GET(self):
        response = {
            'message': message('world')
        }
        web.header('Content-Type', 'application/json')
        return json.dumps(dict(response))


def message(name):
    return 'Hello {}!'.format(name)


urls = (
    '/', Index,
    '\\/hello\\/?', HelloController,
    '\\/hello\\/([^\\/]+)\\/?', PersonalHelloController,
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
