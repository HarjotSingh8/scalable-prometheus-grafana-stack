import cherrypy
import os
import requests
# try to pull workers from worker_management here

class WorkerManagement:
    def init():
        # worker_management url
        worker_management_url = "http://"+os.getenv("WORKER_MANAGEMENT_HOST")+":"+os.getenv("WORKER_MANAGEMENT_PORT")+"/"+os.getenv("WORKER_MANAGEMENT_ENDPOINT")
        self.local_ip_address = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').text # host information from ec2, will change depending on here this is deployed
        self.public_ip_address = requests.get('http://169.254.169.254/latest/meta-data/public-ipv4').text
        self.prometheus_port = os.getenv("PROMETHEUS_PORT") 
        self.grafana_port = os.getenv("GRAFANA_PORT")
        




# update prometheus json config file

# accept push requests for adding new workers/removing old workers to the cluster




class Root:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def update_worker(self):
        result = {"operation": "request", "result": "success"}
        input_json = cherrypy.request.json
        task = input_json["operation"] // "insert" or "delete"



        return result



if __name__ == '__main__':
    # global thread
    start_http_server(9000)

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': int(os.environ['PORT'])})
    cherrypy.quickstart(ListenerService(), '/', conf)