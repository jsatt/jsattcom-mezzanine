include:
    - python

mezzanine_db:
    postgres_database.present:
        - name: {{pillar.postgres.blog_db}}
        - owner: {{pillar.postgres.blog_owner}}
        - runas: postgres
        - require:
            - postgres_user: pg_user-{{pillar.postgres.blog_owner}}

mezzanine:
    git.latest:
        - name: https://github.com/jsatt/jsattcom-mezzanine.git
        - target: /var/www/jsattcom-mezzanine/
    file.managed:
        - name: /var/www/jsattcom-mezzanine/local_settings.py
        - source: salt://mezzanine/local_settings.py
        - mode: 0644
        - template: jinja
        - require:
            - git: mezzanine

pip_requirements:
    cmd.wait:
        - name: pip install -r requirements.txt
        - cwd: /var/www/jsattcom-mezzanine/
        - watch:
            - git: mezzanine
        - require:
            - pkg: pillow_dependencies

collect_static:
    cmd.wait:
        - name: python manage.py collectstatic
        - cwd: /var/www/jsattcom-mezzanine/
        - runas: www-data
        - watch:
            - git: mezzanine

{% for username, user in pillar.postgres.users.items() %}
pg_user-{{username}}:
    postgres_user.present:
        - name: {{username}}
        - password: {{user.password}}
        - encrypted: True
        - superuser: {{user.get('superuser', False)}}
        - runas: postgres
{% endfor %}
