
import sys
import tornado.web
import tornado.ioloop



if __name__ == "__main__":
    application = sys.argv[0]
    print('application = ', application)
    print('waiting requesting ...')
    print('')


    print('\nservice is starting\n')

    application = tornado.web.Application([
        (r"/", EnteranceHandler),
        (r"/predict", PredictHandler),
        (r"/notify", NotifyHandler),
        (r"/scheduler", SchedulerHandler),
        (r"/collect", CollectRecordsHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(Version.PORT_PREDICT)
    tornado.ioloop.IOLoop.instance().start()

