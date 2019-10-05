#!/usr/bin/env bash

watch -n 1 'sudo cp -u Dockerfile ~/redash/  && \
            sudo cp -u docker-compose.yml ~/redash/  && \
            sudo cp -u libcacheodbc.so  ~/redash/  && \
            sudo cp -u odbcinst.ini ~/redash/  && \
            sudo cp -u intersysiris.png ~/redash/  && \
            sudo cp -u redash.gitignore ~/redash/.gitignore  && \
            sudo cp -u ../common_source/__init__.py ~/redash/redash/settings/  && \
            sudo cp -u ../common_source/intersysiris.py ~/redash/redash/query_runner/ && \
            sudo cp -u ../common_source/intersystem_test.py ~/redash/redash/query_runner/ '
