# Use the Kramdown markdown parser
set :markdown_engine, :kramdown

# Enable syntax highlighting
activate :syntax

# Enable live reload
#activate :livereload

set :haml, { ugly: true }

set :css_dir,    'assets/css'
set :js_dir,     'assets/js'
set :images_dir, 'assets/img'

#set :layouts_dir,  '../layouts'
#set :partials_dir, '../partials'

# Build-specific configuration
configure :build do
  # Change the Compass output style for deployment
  # activate :minify_css

  # Minify Javascript on build
  # activate :minify_javascript

  # Enable cache buster
  # activate :cache_buster

  # Use relative URLs
  # activate :relative_assets

  # Compress PNGs after build
  # First: gem install middleman-smusher
  # require "middleman-smusher"
  # activate :smusher

  # Or use a different image path
  # set :http_path, "/Content/images/"
end
