supervisor:
    pkg:
        - installed
    service:
        - running
        - watch:
            - file: mezzanine

mezzanine:
    file.managed:
        - name: /etc/supervisor/conf.d/mezzanine.conf
        - source: salt://etc/supervisor/conf.d/mezzanine.conf
        - mode: 644
        - require:
            - pkg: supervisor
