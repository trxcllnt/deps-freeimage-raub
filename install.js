'use strict';

const install = require('addon-tools-raub/install');


const prefix = 'https://github.com/raub/test-download/releases/download';
const tag    = process.env.npm_package_config_install;

install(`${prefix}/${tag}`);
// https://github.com/raub/test-download/releases/download/v1.0.0/windows.zip
