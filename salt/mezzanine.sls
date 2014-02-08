mezzanine_db:
    postgres_database.present:
        - name: jsatt_blog
        - owner: django
