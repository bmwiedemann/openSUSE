#!/usr/bin/ruby
# based on my old shell function:
# irp () {
#   name="$1"
#   suffix="${3:+-$3}"
#   versioninfo="${2:+-v $2}"
#   r="rubygem-$name$suffix"
#   test -d $r && return 1
#   mkdir $r
#   pushd $r
#   cp ../gem2rpm.yml .
#   if [ -n "$suffix" ]
#   then
#     echo ":version_suffix: '$suffix'" >> gem2rpm.yml
#   fi
#   touch ${r}.spec
#   osc vc -m "initial package"
#   gem fetch --platform=ruby ${2:+-v $2} $name
#   gem2rpm --config gem2rpm.yml -o *spec *gem
#   osc add $PWD
#   ob-tw && osc ci -m "initial package"
#   popd
# }

require 'optparse'
require 'optparse/time'
require 'logger'
require 'fileutils'

class InitializeRubyPackage
  def initialize()
    @log = Logger.new(STDERR)
    @log.level = Logger::INFO
    @log.info("Welcome to IRP aka initialize ruby package")

    @gem_name, @version_info, @version_suffix = nil
    @build_repository = 'openSUSE_Tumbleweed'
    @build_results = '../rpms'

    parse_options
    check_for_existing
    smash_and_grab
  end

  def smash_and_grab
    initial_message="initial package"
    @log.info("Now starting real work")
    FileUtils.mkdir(@package_name)
    Dir.chdir(@package_name)
    gem2rpm_yml = "../gem2rpm.yml"
    if File.exist? gem2rpm_yml
      @log.info("Found gem2rpm.yml default file. Copying...")
      fc = File.read(gem2rpm_yml)
      unless @version_suffix.nil?
        @log.info("Appending version suffix setting.")
        fc += ":version_suffix: '-#{@version_suffix}'"
      end
      File.write("gem2rpm.yml", fc)
    end

    @log.debug("Creating empty spec file for g2r")
    FileUtils.touch("#{@package_name}.spec")
    @log.debug("Creating initial changes file entry")
    exec_with_fail(["osc", "vc", "-m", initial_message])
    gem_fetch_cmdline = ["gem", "fetch", "--platform=ruby"]
    unless @version_info.nil?
      gem_fetch_cmdline << '-v'
      gem_fetch_cmdline << @version_info
    end
    gem_fetch_cmdline << @gem_name
    exec_with_fail(gem_fetch_cmdline)
    exec_with_fail(["g2r"])
    exec_with_fail(["osc", "add", Dir.pwd])
    exec_with_fail(["osc", "ar"])
    exec_with_fail(["osc", "build", "-p", @build_results, '-k', @build_results, @build_repository])
    exec_with_fail(["osc", "ci", "-m", initial_message])
  end


  def exit_with_error(error_code, error_message)
    @log.error(error_message)
    exit(error_code)
  end

  def exec_with_fail(cmdline)
    unless(system(*cmdline))
      exit_with_error(4, "Executing '#{cmdline.join(' ')}' failed.")
    end
  end

  def check_for_existing
    @log.info("Checking for existing #{@package_name}")
    if File.directory?(@package_name)
      exit_with_error(3, "Package #{@package_name} already exists")
    end
  end

  def parse_options
    opt_parser = OptionParser.new do |opts|
      opts.banner = "Usage: irp [options] [gem name]"

      opts.separator ""
      opts.separator "Specific options:"

      opts.on('-v [version specifier]', 'see gem fetch -v for the parameters') do |version_info|
        @version_info = version_info
      end

      opts.on('-s [package suffix]', 'suffix for the package name') do |suffix|
        @version_suffix = suffix
      end

      opts.on('-b [build repository]', "repository to use for the test build - default #{@build_repository}") do |repo|
        @build_repository = repo
      end

      opts.on('-p [rpms directory]', "directory for built rpms and preferred rpms. default is #{@build_results}") do |args|
        @build_results = args
      end
    end
    rest = opt_parser.parse!(ARGV)
    if rest.size == 0
      exit_with_error(1, "Missing package name")
    end
    if rest.size > 1
      exit_with_error(2, "Too many parameters: #{rest}")
    end
    @gem_name = rest.first
    @package_name = "rubygem-#{@gem_name}"

    unless @version_suffix.nil?
      @package_name += "-#{@version_suffix}"
    end
  end
end

InitializeRubyPackage.new()
