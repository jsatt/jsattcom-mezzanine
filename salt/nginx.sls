nginx:
    pkgrepo.managed:
        - ppa: nginx/stable 
        - required_in:
            - pkg: nginx
    pkg.installed:
        - require:
            - pkgrepo: nginx
    service:
        - running
        - watch:
            - file: /etc/nginx/sites-available/default
            - file: /etc/nginx/nginx.conf
     
/etc/nginx/nginx.conf:
    file.managed:
        - source: salt://etc/nginx/nginx.conf
        - template: jinja
        - require:
            - pkg: nginx
    
/etc/nginx/sites-available/default:
    file.managed:
        - source: salt://etc/nginx/sites-available/default
        - template: jinja
        - require:
            - pkg: nginx

# vim:set ft=yaml:
