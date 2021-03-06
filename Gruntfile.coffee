module.exports = (grunt) ->

  # Initial variable configuration
  pkg = grunt.file.readJSON 'package.json'
  name = 'content'
  static_path = "./" + name
  output_path = "./output/blog"
  paths =
    css: static_path + '/static/css'
    scss: static_path + '/static/css/scss'
    js: static_path + '/static/js'
    coffee: static_path + '/static/js/coffee'
    img: static_path + '/static/img'
    vendors: './bower_components'
    fonts: static_path + '/static/fonts'

    pelican_conf: "./settings/"
    pelican_dev_conf: "./settings/dev_settings.py"
    pelican_prod_conf: "./settings/prod_settings.py"
    pelican_content: "./content"
    pelican_theme: "./theme"
    pelican_output: output_path

    pelican_assets: output_path + "static"
    pelican_assets_js: output_path + "static/js"
    pelican_assets_css: output_path + "static/css"

  # Loads grunt config automatically via broken up tasks
  # https://github.com/firstandthird/load-grunt-config
  require('load-grunt-config') grunt,
    data:
      name: name
      paths: paths
    loadGruntTasks:
      pattern: [
        'grunt-*'
      ]

  # Times how long tasks take
  # https://github.com/sindresorhus/time-grunt
  require('time-grunt') grunt
