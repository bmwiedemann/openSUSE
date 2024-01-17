#!/usr/bin/ruby.%{rb_ruby_suffix}

begin
  $LOAD_PATH.unshift "%{vagrant_dir}/lib"
  begin
    require "vagrant/plugin/manager"
  rescue LoadError => e
    raise
  end

  $stdin.each_line do |gemspec_file|
    next if gemspec_file =~ /\/%{name}-%{version}.gemspec$/

    spec = Gem::Specification.load(gemspec_file.strip)
    Vagrant::Plugin::StateFile.new(Pathname.new(File.expand_path "%{vagrant_plugin_conf}")).remove_plugin spec.name
  end
rescue => e
  puts "Vagrant plugin un-register error: #{e}"
end
