module.exports =

  # Copy files and folders
  # https://github.com/gruntjs/grunt-contrib-copy
 
  font_bower:
    expand: true
    flatten: true
    src: '<%= paths.vendors %>/*/fonts/*'
    dest: '<%= paths.css %>/fonts'
  # Copy files and folders
  # https://github.com/gruntjs/grunt-contrib-copy
 
  stylesheets:
    expand: true
    flatten: true
    src: '<%= paths.css %>/build/*.css'
    dest: '<%= paths.pelican_assets_css %>/build/'



  scripts:
    files: ['<%= paths.coffee %>/*.coffee']
    tasks: [
      'newer:coffeelint:scripts'
      'newer:coffee:scripts'
    ]
