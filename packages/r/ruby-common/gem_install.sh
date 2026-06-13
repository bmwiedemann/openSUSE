#!/bin/sh
# vim: set sw=2 sts=2 et tw=80 ft=ruby:
=begin &>/dev/null
# workaround for rubinius bug
# https://github.com/rubinius/rubinius/issues/2732
export LC_ALL="en_US.UTF-8"
export LANG="en_US.UTF-8"
shopt -s nullglob
for ruby in $(/usr/bin/ruby-find-versioned) ; do
  export GEM_HOME="$(${ruby} -r rubygems -e 'puts Gem.default_dir')"
  export RUBY="${ruby}"
  $ruby -x $0 "$@"
done
exit $?
=end
#!/usr/bin/ruby
require 'rbconfig'
require 'optparse'
require 'optparse/time'
require 'ostruct'
require 'fileutils'
require 'find'
require 'tempfile'
require 'logger'
require 'rubygems'
require 'rubygems/package'
require 'yaml'
begin
  require 'rubygems/format'
rescue LoadError => ex
end
begin
  require 'rbconfigpackagingsupport'
rescue LoadError => ex
end

options=OpenStruct.new
options.defaultgem=nil
options.gemfile=nil
options.otheropts=nil
options.docfiles=[]
options.gemname=nil
options.gemversion=nil
options.gemsuffix=nil
options.otheropts=[]
options.skipped_docs=['always']
options.ua_dir='/etc/alternatives'
options.docdir='/usr/share/doc/packages'
# once we start fixing packages set this to true
options.symlinkbinaries=false
options.verbose = false
options.rpmsourcedir = ENV['RPM_SOURCE_DIR'] || '/home/abuild/rpmbuild/SOURCES'
options.buildroot=options.rpmbuildroot = ENV['RPM_BUILD_ROOT'] || '/home/abuild/rpmbuild/BUILDROOT/just-testing'
options.parsed_config = nil
options.use_alts=false
options.libalternative_basedir="/usr/share/libalternatives/"

GILogger = Logger.new(STDERR)
GILogger.level=Logger::DEBUG
def bail_out(msg)
  GILogger.error(msg)
  exit 1
end

def patchfile(fname, needle, replace)
    tmpdir = File.dirname(fname)
    tmp = Tempfile.new('snapshot', tmpdir)
    begin
      stat = File.stat(fname)
      tmp.chmod(stat.mode)
      fc = File.read(fname)
      # fc.gsub!(/^(#!\s*.*?)(\s+-.*)?$/, "#!#{ruby} \2")
      fc.gsub!(needle, replace)
      tmp.write(fc)
      tmp.close
      File.rename(tmp.path, fname)
    rescue ArgumentError => ex
      GILogger.error "Exception while patching '#{fname}'. (#{ex}) Skipping ..."
    ensure
      tmp.close
    end
end

def map_executable(options, executable)
  if not(options.parsed_config.nil? or
         options.parsed_config[:binary_map].nil? or
         options.parsed_config[:binary_map][executable].nil?)
    executable=options.parsed_config[:binary_map][executable]
  end
  executable
end

def initialized_gem2rpm_config(options, name)
  options.config = name
  options.parsed_config = YAML.load_file(name)
end

opt_parser = OptionParser.new do |opts|
  opts.banner = "Usage: gem_install.rb [options]"

  opts.separator ""
  opts.separator "Specific options:"

  opts.on('--config [FILENAME]', 'path to gem2rpm.yml') do |name|
    initialized_gem2rpm_config(options, name)
  end

  opts.on('--default-gem [FILENAME]', 'Which filename to use when we dont find another gem file.') do |fname|
    options.defaultgem=fname
  end
  opts.on('--extconf-opts [EXTOPTS]', 'which options to pass to extconf') do |extopts|
    options.extconfopts=extopts
  end
  opts.on('--gem-binary [PATH]', 'Path to gem. By default we loop over all gem binaries we find') do |fname|
    GILogger.warn("The --gem-binary option is deprecated.")
  end
  opts.on('--doc-files [FILES]', 'Whitespace separated list of documentation files we should link to /usr/share/doc/packages/<subpackage>') do |files|
    options.docfiles = files.split(/\s+/)
  end
  opts.on('--gem-name [NAME]', 'Name of them gem') do |name|
    options.gemname = name
  end
  opts.on('--gem-version [VERSION]', 'Version of them gem') do |version|
    options.gemversion = version
  end
  opts.on('--gem-suffix [SUFFIX]', 'Suffix we should append to the subpackage names') do |suffix|
    options.gemsuffix = suffix
  end
  opts.on('--build-root [BUILDROOT]', 'Path to rpm buildroot') do |buildroot|
    options.buildroot = buildroot
    options.rpmbuildroot = buildroot
  end
  # Boolean switches
  opts.on('--[no-]symlink-binaries', 'Create all the version symlinks for the binaries') do |v|
    options.symlinkbinaries = v
  end
  opts.on('-d', 'Forwarded to gem install') do |v|
    options.otheropts << '-d'
  end
  opts.on('-f', 'Forwarded to gem install') do |v|
    options.otheropts << '-f'
  end
  opts.on('-E', 'Forwarded to gem install') do |v|
    options.otheropts << '-E'
  end
  opts.on('--no-ri', 'Forwarded to gem install') do |v|
    options.skipped_docs << 'ri'
  end
  opts.on('-N', '--no-document', 'Forwarded to gem install') do |v|
    options.skipped_docs << 'ri'
    options.skipped_docs << 'rdoc'
  end
  opts.on('--no-rdoc', 'Forwarded to gem install') do |v|
    options.skipped_docs << 'rdoc'
  end
  opts.separator ""
  opts.separator "Common options:"
  opts.on("-v", "--[no-]verbose", "Run verbosely") do |v|
    options.verbose = v
  end
  opts.on_tail('-h', '--help', 'Show this message') do
    puts opts
    exit
  end
end

options.otheropts+=opt_parser.parse!(ARGV)
GILogger.info "unhandled options: #{options.otheropts.inspect}"
if options.gemfile.nil?
  # we are in /home/abuild/rpmbuild/BUILD/
  # search for rebuild gem files
  gemlist = Dir['*/*.gem', '*/*/.gem', "#{options.rpmsourcedir}/*.gem"]
  if gemlist.empty?
     bail_out("Can not find any gem file")
  end
  options.gemfile = gemlist.first
  GILogger.info "Found gem #{options.gemfile}"
end

if options.config.nil?
  name = File.join(options.rpmsourcedir, 'gem2rpm.yml')
  if File.exist?(name)
    initialized_gem2rpm_config(options, name)
  end
end

package   = Gem::Package.new(options.gemfile) rescue Gem::Format.from_file_by_path(options.gemfile)
spec      = package.spec
gemdir    = File.join(Gem.dir, 'gems', "#{options.gemname}-#{options.gemversion}")
# TODO: ruby = "#{File.join(RbConfig::CONFIG['bindir'],RbConfig::CONFIG['ruby_install_name'])}mo"
ruby      = Gem.ruby
gembinary = Gem.default_exec_format % "/usr/bin/gem"

rubysuffix = Gem.default_exec_format % ''
case rubysuffix
  when /\A\d+.\d+\z/
    options.rubysuffix = ".ruby#{rubysuffix}"
    options.rubyprefix = "ruby#{rubysuffix}"
  when /\A\.(.*)\z/
    options.rubysuffix = ".#{$1}"
    options.rubyprefix = $1
  when ''
    # TODO: case seems broken
    rb_ver = RbConfig::CONFIG['ruby_version'].gsub(/^(\d+\.\d+).*$/, "\1")
    options.rubysuffix = ".ruby#{rb_ver}"
    options.rubyprefix = "ruby#{rb_ver}"
  else
    bail_out "unknown binary naming scheme: #{rubysuffix}"
end
GILogger.info "Using prefix #{options.rubyprefix}"
GILogger.info "Using suffix #{options.rubysuffix}"

cmdline = [gembinary, 'install', '--verbose', '--local', '--build-root', options.buildroot]
cmdline += options.otheropts
unless options.skipped_docs.empty?
  cmdline << '--no-document'
end
cmdline << options.gemfile
unless options.extconfopts.nil?
  cmdline << '--'
  cmdline << options.extconfopts
end
GILogger.info "install cmdline: #{cmdline.inspect}"
if Process.respond_to? :spawn
  pid = Process.spawn(*cmdline)
  pid, status = Process.wait2(pid)
else
  system(*cmdline)
  status = $?
end
exit status.exitstatus unless 0 == status.exitstatus

rpmname="#{options.rubyprefix}-rubygem-#{options.gemname}#{options.gemsuffix}"
GILogger.info "RPM name: #{rpmname}"
pwd = Dir.pwd
bindir = File.join(options.buildroot, Gem.bindir)
GILogger.info "bindir: #{bindir}"

def segment_to_int(version_segments, index, default)
  begin v=Integer(version_segments[index]) rescue v=default end
  return v
end

def compute_segments(v1,v2,v3)
  return v1*10000+v2*100+v3
end

spec_version_segments=spec.version.segments
version_weight=compute_segments(
  segment_to_int(spec_version_segments, 0, 1),
  segment_to_int(spec_version_segments, 1, 0),
  segment_to_int(spec_version_segments, 2, 0)
)

ruby_version_segments=Gem::Version.new(RUBY_VERSION).segments
ruby_weight=compute_segments(
  segment_to_int(ruby_version_segments, 0, 1),
  segment_to_int(ruby_version_segments, 1, 0),
  segment_to_int(ruby_version_segments, 2, 0)
)

weight=version_weight+ruby_weight

def write_alts_file(alts_dir, full_versioned, target_subdir, weight)
  config_dir=File.join(alts_dir, target_subdir)
  config_filename=File.join(config_dir, "#{weight}.conf")
  config_content= <<EOF
binary=#{Gem.bindir}/#{full_versioned}
group=#{target_subdir}
EOF
  if FileUtils.mkdir_p(config_dir)
    unless File.write(config_filename, config_content)
      GILogger.error "Creating #{config_file} failed"
    end
  else
    GILogger.error "Creating #{config_dir} failed"
  end
end

if options.symlinkbinaries && File.exist?(bindir)
  if options.use_alts
    br_alts_dir=File.join(options.buildroot, options.libalternative_basedir)
    GILogger.info "Creating libalternatives dir: #{br_alts_dir}"
    FileUtils.mkdir_p(br_alts_dir)
  else
    br_ua_dir = File.join(options.buildroot, options.ua_dir)
    GILogger.info "Creating upate-alternatives dir: #{br_ua_dir}"
    FileUtils.mkdir_p(br_ua_dir)
  end
  begin
    Dir.chdir(bindir)
    GILogger.info "executables: #{spec.executables.inspect}"
    spec.executables.each do |unversioned|
      default_path   = Gem.default_exec_format % unversioned
      full_versioned = "#{unversioned}#{options.rubysuffix}-#{spec.version}"
      ruby_versioned = "#{unversioned}#{options.rubysuffix}"
      gem_versioned  = "#{unversioned}-#{spec.version}"
      unversioned = map_executable(options, unversioned)
      File.rename(default_path, full_versioned)
      patchfile(full_versioned,  />= 0(\.a)?/, "= #{options.gemversion}")
      # unversioned
      [unversioned, ruby_versioned, gem_versioned].each do |linkname|
        if options.use_alts
          link_path = File.join(options.buildroot, Gem.bindir, linkname)
          write_alts_file(br_alts_dir, full_versioned, linkname, weight)
          GILogger.info "Symlinking 'alts' -> '#{link_path}'"
          File.symlink('/usr/bin/alts', link_path) unless File.symlink? link_path
        else
          ua_path   = File.join(options.ua_dir, linkname)
          GILogger.info "Symlinking '#{linkname}' -> '#{ua_path}'"
          File.symlink(ua_path, linkname) unless File.symlink? linkname
        end
      end
    end
  ensure
    Dir.chdir(pwd)
  end
else
  GILogger.error "Skipping symlinking binaries #{options.symlinkbinaries} #{File.exist?(bindir)} #{bindir}"
end

# shebang line fix
Find.find(File.join(options.buildroot, gemdir)) do |fname|
  if File.file?(fname) && File.executable?(fname)
    next if fname =~ /\.so$/
    GILogger.info "Looking at #{fname}"
    patchfile(fname, /^(#!\s*.*(?:rub|rbx).*?)(\s+-.*)?$/, "#!#{ruby} \\2")
  else
    next
  end
end

unless options.docfiles.empty?
  GILogger.info "Linking documentation"
  docdir = File.join(options.buildroot, options.docdir, rpmname)
  FileUtils.mkdir_p(docdir)

  options.docfiles.each do |fname|
    fullpath = File.join(gemdir, fname)
    GILogger.info "- #{fullpath}"
    File.symlink(fullpath, File.join(docdir,fname))
  end
end

system("chmod -R u+w,go+rX,go-w #{options.buildroot}")
#system("find #{options.buildroot} -ls")
