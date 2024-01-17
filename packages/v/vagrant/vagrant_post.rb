#!/usr/bin/ruby.%{rb_ruby_suffix}

begin
  $LOAD_PATH.unshift "%{vagrant_dir}/lib"
  begin
    require "vagrant/plugin/manager"
  rescue LoadError => e
    raise
  end;

  unless File.exist?("%{vagrant_plugin_conf}")
    Vagrant::Plugin::StateFile.new(Pathname.new(File.expand_path "%{vagrant_plugin_conf}")).save!
#    File.symlink "%{vagrant_plugin_conf}", "%{vagrant_plugin_conf_link}"
  end
rescue => e
  puts "Vagrant plugin.json is not properly initialized: #{e}"
end
