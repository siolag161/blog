module.exports =

  # Run tasks whenever watched files change
  # https://github.com/gruntjs/grunt-contrib-watch

  options:
    spawn: false

  config:
    options:
      reload: true
    files: [
      'Gruntfile.coffee'
      'grunt/*.{coffee,yaml}'
    ]

  livereload:
    options:
      livereload: '<%= connect.livereload %>'
    files: [
      '<%= paths.pelican_content %>/**/*.md'
      '<%= paths.pelican_conf %>/*.py'
      '<%= paths.pelican_assets_css %>/build/*.css'
      '<%= paths.coffee %>/*.coffee'
    ]

  pelican:
    files: [
      '<%= paths.pelican_content %>/**/*.rst',
      '<%= paths.pelican_content %>/**/*.md'
      '<%= paths.pelican_conf %>/*.py'
      ]
    tasks: [
      'build_pelican_dev'
    ] 

  stylesheets:
    files: ['<%= paths.scss %>/*.scss']
    tasks: [
      #'newer:scsslint'
      'newer:sass'
      'newer:autoprefixer'
      'replace:stylesheets'
      'copy:stylesheets'
    ]

  scripts:
    files: ['<%= paths.coffee %>/*.coffee']
    tasks: [
      'newer:coffeelint:scripts'
      'newer:coffee:scripts'
    ]

  images:
    files: ['<%= paths.img %>/**/*.{png,jpg,gif,svg}']
    tasks: ['newer:imagemin']
