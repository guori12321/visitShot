import web
render = web.template.render('templates/')

print render

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, name):
        return render.index(name)
        #return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
