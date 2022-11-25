#!/bin/sh
=begin &>/dev/null
# workaround for rubinius bug
# https://github.com/rubinius/rubinius/issues/2732
export LC_ALL="en_US.UTF-8"
export LANG="en_US.UTF-8"
ruby=""
for bundler in $(/usr/bin/ruby-find-versioned bundler) ; do
  if [ -x "$bundler" ] ; then
    ruby="${bundler//bundler/ruby}"
    break
  fi
done
exec $ruby -x $0 "$@"
=end
#!/usr/bin/ruby
# vim: set sw=2 sts=2 et tw=80 :
require 'bundler'
require 'yaml'

app_info_file=".appinfo.yml"
gemfile_lock = STDIN.read.chomp

appdir = File.dirname(gemfile_lock)
Dir.chdir(appdir)

unless File.exist? app_info_file then
  STDERR.puts "Warning: Skipping Gemfile.lock without appinfo.yaml file"
  exit 0
end

app_config =YAML.load_file(app_info_file) || {}
ruby_abi=app_config[:ruby_abi]

if ruby_abi.nil? then
  STDERR.puts "Error: Can not generate requires without a ruby abi. Skipping."
  exit 0
end

Bundler.definition.specs.each do |dep|
  puts "rubygem(#{ruby_abi}:#{dep.name}) = #{dep.version}"
end
