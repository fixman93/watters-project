Frontend developemnt based at the following Node.js applications

* Bower package manager http://bower.io/
* Grunt task runner http://gruntjs.com/

Preparing local environment for development
===========================================

Change current path in the terminal to frontend directory

	$ cd path-to-source-code/frontend

Install Node.js and npm from https://nodejs.org/download/

Install Bower globally

	$ npm install -g bower

Install Grunt globally

	$ npm install -g grunt-cli

Load required Grunt modules

	$ npm install

Check

	$ grunt


Overview
========

*Bower configuration* keeps all requirements in the frontend/bower.json file, devDependencies section. All requirements are part of repository and stores in frontend/bower_components. New requirement can be installed or existing requirement can be updated via command:

	$ bower install

That command should be runned once, when you add new requirement or change version of existing.


*Grunt configuration* keeps all required modules for task in frontend/package.json file, devDependencies section. All modules aren't part of repository and stores in frontend/node_modules only locally. New module can be installed or existing module can be updated via command:

	$ npm install

That command should be runned when you add new module, change version of existing or another developer added new module in the previous commit.

*Grunt automation* tasks described in frontend/Gruntfile.js. After any changes in frontend/assert directory please run command:

	$ grunt


That calls default task magic. Magic task will:

* Process all scss files into css. Don't need to run compass command separatelly
* Combine all css and js files into one per type
* Minification of css file
* Uglyfication of js file
* Update links to used bower requirements in index.htm
* Append hashstring to resources from index.htm to avoid problems with cache

This command should be runned before each commit into repository to prepare all source files for the serving under web-server.