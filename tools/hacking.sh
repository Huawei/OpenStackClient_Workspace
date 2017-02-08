#!/bin/bash
flake8 workspaceclient | tee flake8.log
exit ${PIPESTATUS[0]}
