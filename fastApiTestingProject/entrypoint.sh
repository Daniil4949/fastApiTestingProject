#!/bin/bash

uvicorn main:init_app --host "$NOTES_APP_HOST" --port "$NOTES_APP_PORT"
