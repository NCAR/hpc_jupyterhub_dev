# Basic JupyterHub Configuration File


c = get_config()

c.ConfigurableHTTPProxy.debug = False
c.JupyterHub.tornado_settings = {
    'slow_spawn_timeout': 0
}

admin_user_s = (
    'user_a',
    'user_b',
)

c.Authenticator.admin_users = admin_user_s

c.PAMAuthenticator.service = 'jupyterhub'
c.PAMAuthenticator.open_sessions = False

c.JupyterHub.log_level = 'DEBUG'

c.Spawner.http_timeout = 600
c.Spawner.start_timeout = 600
c.Spawner.poll_interval = 15

c.JupyterHub.ip = '192.168.99.1'
c.JupyterHub.port = 8800

api_addr = '192.168.99.1'
api_port = 8801
c.ConfigurableHTTPProxy.api_url = f'http://{api_addr}:{api_port}'


base_url = u'/'

c.JupyterHub.default_url = f'{base_url}/user/' + '{username}/lab'
c.JupyterHub.notebook_dir = u'/home/{username}'

c.JupyterHub.spawner_class = 'sudospawner.SudoSpawner'

