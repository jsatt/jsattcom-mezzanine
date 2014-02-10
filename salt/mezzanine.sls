include:
    - python

mezzanine_db:
    postgres_database.present:
        - name: {{pillar.postgres.blog_db}}
        - owner: {{pillar.postgres.blog_owner}}

mezzanine:
    git.latest:
        - name: https://github.com/jsatt/jsattcom-mezzanine.git
        - target: /var/www/jsatt-mezzanine
    file.managed:
        - name: /var/www/jsattcom-mezzanine/local_settings.py
        - source: salt://var/www/local_settings.py
        - template: jinja
        - require:
            - git: mezzanine
    cmd.wait:
        - name: pip install -r requirements.txt
        - cwd: /var/www/jsatt-mezzanine
        - watch:
            - git: mezzanine
        - require:
            - pkg: pillow_dependencies

{% for username, user in pillar.postgres.users.items() %}
{{username}}:
    postgres_user.present:
        - password: {{user.password}}
        {% if user.get('superuser', False) %}- superuser: True{% endif %}
{% endfor %}
