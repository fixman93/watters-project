module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    // sass to css
    sass: {
        dist: {
            options: {
                style: 'compressed',
                lineNumbers: false,
                noCache: true
            },
            files: {
                'assets/css/styles.css': 'assets/scss/styles.scss'
            }
        }
    },
    // concating of css and js
    concat: {
        js : {
            src : [
                'assets/js/*.js'
            ],
            dest : 'assets/dist/all.js'
        }
    },
    // minification of main stylesheet
    cssmin : {
        css:{
            src: 'assets/css/styles.css',
            dest: 'assets/dist/styles.min.css'
        }
    },
    // minification of main javascript
     uglify : {
        js: {
            files: {
                'assets/dist/all.min.js' : ['assets/dist/all.js']
            }
        }
    },
    clean: [
        'assets/dist/all.js',
        'assets/dist/styles.css',
        'assets/css/styles.css',
        'assets/css/styles.css.map'],
    // inserting paths to css and js for components automatically
    wiredep: {
        target: {
            src: [
                'index.htm',
            ],
            options: {
                cwd: '',
                dependencies: true,
                devDependencies: true,
                exclude: [],
                fileTypes: {},
                ignorePath: '',
                overrides: {},
                fileTypes: {
                    html: {
                        replace: {
                          js: '<script src="/{{filePath}}"></script>',
                          css: '<link rel="stylesheet" href="/{{filePath}}" />'
                        }
                    }
                }
            }
        }
    },
    cachebreaker: {
        options: {
            match: ['/assets/dist/all.min.js', '/assets/dist/styles.min.css'],
        },
        files: {
            src: ['index.htm']
        }
    },
    // watching for changes in files
    watch: {
        files: ['assets/js/**/*.js', 'assets/scss/**/*.scss'],
        tasks: ['magic']
    }
  });

  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');

  //grunt.loadNpmTasks('grunt-bower-concat');
  grunt.loadNpmTasks('grunt-cache-breaker');
  grunt.loadNpmTasks('grunt-wiredep');

  grunt.registerTask('magic', 'Makes all. It\'s magic.', function() {
    grunt.task.run(['sass', 'concat', 'cssmin', 'uglify', 'clean',
                    'wiredep', 'cachebreaker']);
  });

  grunt.registerTask('default', ['magic']);
};