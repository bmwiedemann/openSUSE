#! /usr/bin/sh

# we need to set the default load path so we cannot use a simple symlink... :-(

# set the default load path
export NODE_PATH=/usr/lib/node_modules/playwright/node_modules

# run the CLI script
/usr/bin/env node /usr/lib/node_modules/playwright/cli.js "$@"

