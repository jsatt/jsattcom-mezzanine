supervisor:
    pkg:
        - installed
    service:
        - running
        - watch:
            - file: /etc/supervisor/conf.d/mazzanine.conf

/etc/supervisor/conf.d/mezzanine.conf:
    file.managed:
        - source: salt://etc/supervisor/conf.d/mezzanine.conf
        - mode: 644
        - require:
            - pkg: supervisor
