#!/bin/bash

run_as_me() {
    sudo -g me -u me "$@"
}
