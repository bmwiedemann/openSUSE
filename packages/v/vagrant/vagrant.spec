#
# spec file for package vagrant
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Laurent Bigonville <bigon@debian.org>, License GPL-2.0+
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

# disable tests if you want to just run a quick build
%{bcond_without tests}

%global mod_name vagrant
%global mod_full_name %{mod_name}-%{version}
%global vim_data_dir %{_datadir}/vim/site/plugin/


Name:           vagrant
Version:        2.3.4
Release:        0
Summary:        Tool for building and distributing virtualized development environments
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/hashicorp/vagrant
Source0:        %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
Source11:       vagrant.1
Source93:       vagrant_transfiletriggerin.rb
Source94:       vagrant_transfiletriggerun.rb
Source95:       vagrant_post.rb
Source96:       binstub
Source97:       macros.vagrant
Source98:       README.SUSE
Provides:       rubygem-vagrant = %{version}
Obsoletes:      rubygem-vagrant < %{version}
Recommends:     vagrant-libvirt
#
# Patches are maintained in the opensuse_package branch in the
# https://github.com/dcermak/vagrant.git repository.
# On every new release of vagrant, rebase them on top of the latest tag.
#
Patch1:         0001-bin-vagrant-silence-warning-about-installer.patch
Patch2:         0002-Use-a-private-temporary-dir.patch
Patch3:         0003-plugins-don-t-abuse-require_relative.patch.patch
Patch4:         0004-fix-vbox-package-boo-1044087-added-by-robert.muntean.patch
Patch5:         0005-do-not-depend-on-wdm.patch
Patch6:         0006-do-not-abuse-relative-paths-in-docker-plugin-to-make.patch
Patch7:         0007-Don-t-abuse-relative-paths-in-plugins.patch
Patch8:         0008-Skip-failing-tests.patch
Patch9:         0009-Disable-Subprocess-unit-test.patch
Patch10:        0010-Remove-dependency-on-grpc-tools.patch

# force only one ruby version
# CAUTION: if you change this, then you *must* also change the sed calls which
#          fix these values in macros.vagrant
%global rb_build_versions %rb_default_ruby
%global rb_build_abi %rb_default_ruby_abi
%global rb_ruby_suffix %rb_default_ruby_suffix

# we use the rpm macros in this spec
# need to load them *after* defining the rb_* macros
%{load:%{SOURCE97}}

%global vagrant_plugin_name vagrant


#===============================================================================
# Build dependencies
#===============================================================================

#  s.required_ruby_version     = ">= 2.7", "< 3.2"
%if 0%{?suse_version} > 1500
BuildRequires:  %{ruby} < 3.2
%else
BuildRequires:  %{ruby} >= 2.7
%endif
#
#
#
BuildRequires:  %{rubygem bundler}
#  s.add_dependency "bcrypt_pbkdf", "~> 1.1"
BuildRequires:  %{rubygem bcrypt_pbkdf:1 >= 1.1 }
#  s.add_dependency "childprocess", "~> 4.1.0"
BuildRequires:  %{rubygem childprocess:4.1 }
#  s.add_dependency "ed25519", "~> 1.3.0"
BuildRequires:  %{rubygem ed25519:1.3 >= 1.3.0 }
#  s.add_dependency "erubi"
BuildRequires:  %{rubygem erubi }
#  s.add_dependency 'googleapis-common-protos-types', '~> 1.3'
BuildRequires:  %{rubygem googleapis-common-protos-types:1 >= 1.3}
#  s.add_dependency "grpc"
BuildRequires:  %{rubygem grpc}
#  s.add_dependency "i18n", "~> 1.8"
BuildRequires:  %{rubygem i18n:1 >= 1.8 }
#  s.add_dependency "listen", "~> 3.6"
BuildRequires:  %{rubygem listen:3 >= 3.6 }
#  s.add_dependency "hashicorp-checkpoint", "~> 0.1.5"
BuildRequires:  %{rubygem hashicorp-checkpoint:0.1 >= 0.1.5 }
#  s.add_dependency "log4r", "~> 1.1.9", "< 1.1.11"
BuildRequires:  %{rubygem log4r:1.1 >= 1.1.9 }
BuildConflicts:  %{rubygem log4r:1.1 >= 1.1.11 }
#  s.add_dependency "mime-types", "~> 3.3"
BuildRequires:  %{rubygem mime-types:3 >= 3.3 }
#  s.add_dependency "net-ftp", "~> 0.1"
BuildRequires:  %{rubygem net-ftp:0 >= 0.1 }
#  s.add_dependency "net-ssh", "~> 7.0"
BuildRequires:  %{rubygem net-ssh:7 }
#  s.add_dependency "net-sftp", "~> 4.0"
BuildRequires:  %{rubygem net-sftp:4 }
#  s.add_dependency "net-scp", "~> 4.0"
BuildRequires:  %{rubygem net-scp:4 }
#  s.add_dependency "rb-kqueue", "~> 0.2.0"
BuildRequires:  %{rubygem rb-kqueue:0.2 }
#  s.add_dependency "rexml", "~> 3.2"
BuildRequires:  %{rubygem rexml:3 >= 3.2 }
#  s.add_dependency "rgl", "~> 0.5.7"
BuildRequires:  %{rubygem rgl:0.5 >= 0.5.7}
#  s.add_dependency "rubyzip", "~> 2.0"
BuildRequires:  %{rubygem rubyzip:2}
# Intentionally removed, wdm only works on Windows
# BuildRequires:  %%{rubygem wdm }
#  s.add_dependency "winrm", ">= 2.3.4", "< 3.0"
BuildRequires:  %{rubygem winrm:2 >= 2.3.4 }
#  s.add_dependency "winrm-fs", ">= 1.3.4", "< 2.0"
BuildRequires:  %{rubygem winrm-fs:1 >= 1.3.4 }
#  s.add_dependency "winrm-elevated", ">= 1.2.1", "< 2.0"
BuildRequires:  %{rubygem winrm-elevated:1 >= 1.2.1 }
#  s.add_dependency "vagrant_cloud", "~> 3.0.5"
BuildRequires:  %{rubygem vagrant_cloud:3.0 >= 3.0.5 }

# PATCHED -> removed
#  s.add_development_dependency "grpc-tools", "~> 1.41.1"
# BuildRequires:  %%{rubygem grpc-tools:1.41 >= 1.41.1}

# devel dependencies:
#  s.add_development_dependency "rake", "~> 13.0"
BuildRequires:  %{rubygem rake:13 }
#  s.add_development_dependency "rspec", "~> 3.11"
BuildRequires:  %{rubygem rspec:3 >= 3.11 }
#  s.add_development_dependency "rspec-its", "~> 1.3.0"
BuildRequires:  %{rubygem rspec-its:1.3 }
#  s.add_development_dependency "fake_ftp", "~> 0.3.0"
BuildRequires:  %{rubygem fake_ftp:0.3 >= 0.3.0 }
#  s.add_development_dependency "webrick", "~> 1.7.0"
BuildRequires:  %{rubygem webrick:1.7 }

# Prevent have choice for rubygem(ruby:2.6.0:mime-types) >= 2
BuildRequires:  %{rubygem mime-types:3 }
# Prevent have choice for rubygem(ruby:2.6.0:builder) >= 2.1.2
BuildRequires:  %{rubygem builder:3.2 }
# Prevent have choice for rubygem(ruby:2.6.0:ffi:1) >= 1
BuildRequires:  %{rubygem ffi >= 1.9 }
# Prevent have choice for rubygem(ruby:2.5.0:addressable) >= 2.3.6
BuildRequires:  %{rubygem addressable >= 2.7}

# gem2rpm *must* be included as a direct dependency when building with a
# non-default ruby version
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5

# for the test
%if %{with tests}
BuildRequires:  openssh
BuildRequires:  curl
BuildRequires:  bsdtar
BuildRequires:  %{rubygem vagrant-spec}
%endif

BuildRequires:  fdupes

#===============================================================================
# Runtime dependencies
#===============================================================================

#  s.add_dependency "bcrypt_pbkdf", "~> 1.1"
Requires:       %{rubygem bcrypt_pbkdf:1 >= 1.1 }
#    s.add_dependency "childprocess", "~> 4.1.0"
Requires:       %{rubygem childprocess:4.1}
#   s.add_dependency "ed25519", "~> 1.3.0"
Requires:       %{rubygem ed25519:1.3 >= 1.3.0}
#  s.add_dependency "erubi"
Requires:       %{rubygem erubi}
#  s.add_dependency 'googleapis-common-protos-types', '~> 1.3'
Requires:       %{rubygem googleapis-common-protos-types:1 >= 1.3}
#  s.add_dependency "grpc"
Requires:       %{rubygem grpc}
#  s.add_dependency "i18n", "~> 1.8"
Requires:       %{rubygem i18n:1 >= 1.8}
#  s.add_dependency "listen", "~> 3.6"
Requires:       %{rubygem listen:3 >= 3.6}
#  s.add_dependency "hashicorp-checkpoint", "~> 0.1.5"
Requires:       %{rubygem hashicorp-checkpoint:0.1 >= 0.1.5}
#  s.add_dependency "log4r", "~> 1.1.9", "< 1.1.11"
Requires:       %{rubygem log4r:1.1 >= 1.1.9 }
Requires:       %{rubygem log4r:1.1 < 1.1.11 }
#  s.add_dependency "mime-types", "~> 3.3"
Requires:       %{rubygem mime-types:3 >= 3.3}
#  s.add_dependency "net-ftp", "~> 0.1"
BuildRequires:  %{rubygem net-ftp:0 >= 0.1 }
#  s.add_dependency "net-ssh", "~> 7.0"
Requires:       %{rubygem net-ssh:7 }
#  s.add_dependency "net-sftp", "~> 4.0"
Requires:       %{rubygem net-sftp:4 }
#  s.add_dependency "net-scp", "~> 4.0"
Requires:       %{rubygem net-scp:4 }
#  s.add_dependency "rb-kqueue", "~> 0.2.0"
Requires:       %{rubygem rb-kqueue:0.2}
#  s.add_dependency "rexml", "~> 3.2"
Requires:       %{rubygem rexml:3 >= 3.2 }
#  s.add_dependency "rgl", "~> 0.5.7"
Requires:       %{rubygem rgl:0.5 >= 0.5.7}
#  s.add_dependency "rubyzip", "~> 2.0"
Requires:       %{rubygem rubyzip:2}
#   s.add_dependency "wdm", "~> 0.1.0"
# skip wdm, Windows only
#  s.add_dependency "winrm", ">= 2.3.4", "< 3.0"
Requires:       %{rubygem winrm:2 >= 2.3.4}
#  s.add_dependency "winrm-fs", ">= 1.3.4", "< 2.0"
Requires:       %{rubygem winrm-fs:1 >= 1.3.4}
#  s.add_dependency "winrm-elevated", ">= 1.2.1", "< 2.0"
Requires:       %{rubygem winrm-elevated:1 >= 1.2.1}
#  s.add_dependency "vagrant_cloud", "~> 3.0.5"
Requires:       %{rubygem vagrant_cloud:3.0 >= 3.0.5}


Requires:       bsdtar
Requires:       curl
Requires:       openssh

%description
Vagrant is a tool for building and distributing virtualized development
environments.

%package        doc
Summary:        Documentation for Vagrant
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
This package contains the documentation for vagrant.

%package        vim
Summary:        Vagrantfile syntax files for the vim editor
Group:          Development/Languages/Ruby
Supplements:    (vagrant and vim)
BuildRequires:  vim
Requires:       vagrant = %{version}
Requires:       vim
BuildArch:      noarch

%description    vim
Optional dependency offering vim syntax files for Vagrantfile

%package        emacs
Summary:        Vagrantfile syntax files for the emacs editor
Group:          Development/Languages/Ruby
Supplements:    (vagrant and emacs_program)
BuildRequires:  emacs-nox
Requires:       emacs_program
Requires:       vagrant = %{version}
BuildArch:      noarch

%description    emacs
Optional dependency offering emacs syntax files for Vagrantfile

%package bash-completion
Summary:        Vagrant bash autocompletion
Group:          Development/Languages/Ruby
Supplements:    (vagrant and bash)
BuildRequires:  bash
BuildRequires:  bash-completion
Requires:       bash
Requires:       bash-completion
Requires:       vagrant = %{version}
BuildArch:      noarch

%description  bash-completion
Optional dependency offering bash completion for vagrant

%prep
%autosetup -p1 -n %{mod_full_name}

cp %{SOURCE98} .

%build
mv %{mod_name}.gemspec %{mod_full_name}.gemspec
%gem_build
mv %{mod_full_name}.gem %{_sourcedir}

%install

# cannot use %%vagrant_plugin_install here, as we provide a different --bindir
CONFIGURE_ARGS="--with-cflags='%{optflags}' $CONFIGURE_ARGS"
%gem_binary install -V -f --local --no-user-install \
    --ignore-dependencies --no-document --backtrace \
    --document=rdoc,ri \
    --install-dir %{buildroot}%{vagrant_plugin_dir} \
    --bindir %{buildroot}%{vagrant_plugin_dir}/bin %{_sourcedir}/%{mod_full_name}.gem

# the actual vagrant binary generated from the binstub
install -D -m 755 %{SOURCE96} %{buildroot}%{_bindir}/vagrant
gem_path=$(ruby.%{rb_ruby_suffix} -e "print Gem.path.reject{|path| path.include? 'home'}.join(':')")
sed -i -e "s|@vagrant_embedded_dir@|%{vagrant_embedded_dir}|" \
       -e "s|@ruby_vagrant_gem_path@|$gem_path:%{vagrant_plugin_dir}|" \
       -e "s|@vagrant_rb_ruby_suffix@|%{vagrant_rb_ruby_suffix}|" \
    %{buildroot}%{_bindir}/%{name}

# install the rpm macros & expand the name, name-version and vagrant_rb_* macros
%global macros_vagrant %{_rpmconfigdir}/macros.d/macros.%{name}
install -D -m 0644 %{SOURCE97} %{buildroot}%{macros_vagrant}
sed -i -e "s|%%{name}|%{name}|" \
       -e "s|%{name}-%%{version}|%{name}-%{version}|" \
       -e "s|%%{rb_build_versions}|%{rb_build_versions}|" \
       -e "s|%%{rb_build_abi}|%{rb_build_abi}|" \
       -e "s|%%{rb_ruby_suffix}|%{rb_ruby_suffix}|" \
    %{buildroot}%{macros_vagrant}

# install post, transfiletrigerin & transfiletriggerun scriptlets
%global post_rb %{vagrant_embedded_dir}/bin/vagrant_post.rb
%global transfiletriggerin_rb %{vagrant_embedded_dir}/bin/vagrant_transfiletriggerin.rb
%global transfiletriggerun_rb %{vagrant_embedded_dir}/bin/vagrant_transfiletriggerun.rb
install -D -m 0755 %{SOURCE93} %{buildroot}%{transfiletriggerin_rb}
install -D -m 0755 %{SOURCE94} %{buildroot}%{transfiletriggerun_rb}
install -D -m 0755 %{SOURCE95} %{buildroot}%{post_rb}

# expand macros in scriptlets
for file in %{post_rb} %{transfiletriggerin_rb} %{transfiletriggerun_rb}; do
    sed -i "s|%%{vagrant_dir}|%{vagrant_dir}|" %{buildroot}$file
    sed -i "s|%%{vagrant_plugin_conf}|%{vagrant_plugin_conf}|" %{buildroot}$file
    sed -i "s|%%{name}|%{name}|" %{buildroot}$file
    sed -i "s|%%{version}|%{version}|" %{buildroot}$file
    sed -i "s|%%{rb_ruby_suffix}|%{rb_ruby_suffix}|" %{buildroot}$file
done

# man page
install -D -m 644 %{SOURCE11} %{buildroot}%{_mandir}/man1/vagrant.1

# Bash completion: install it without the .sh ending, otherwise completion is broken
# and remove the shebang line in it
install -D -m 0644 %{buildroot}%{vagrant_dir}/contrib/bash/completion.sh \
    %{buildroot}%{_datadir}/bash-completion/completions/%{mod_name}
sed -i '1d' %{buildroot}%{_datadir}/bash-completion/completions/%{mod_name}

# Vim & Emacs syntax highlighting
install -D -m 0644 %{buildroot}%{vagrant_dir}/contrib/vim/vagrantfile.vim \
    %{buildroot}%{vim_data_dir}/%{mod_name}.vim
install -D -m 0644 %{buildroot}%{vagrant_dir}/contrib/emacs/vagrant.el \
    %{buildroot}%{_datadir}/emacs/site-lisp/%{mod_name}.el

chmod -x %{buildroot}%{vagrant_dir}/templates/locales/en.yml

# directories for vagrant plugins
mkdir -p %{buildroot}%{dirname:%{vagrant_plugin_cache}}
mkdir -p %{buildroot}%{dirname:%{vagrant_plugin_spec}}
mkdir -p %{buildroot}%{dirname:%{vagrant_plugin_docdir}}


# fix shebang in %%{vagrant_dir}/bin/%%{name}
sed -i 's|^\#\!/usr/bin/env.*|\#\!/usr/bin/ruby\.%{rb_ruby_suffix}|' \
    %{buildroot}%{vagrant_dir}/bin/%{name}

# remove versioned name from %%{vagrant_plugin_dir}/bin/%%{name}
# (aka /usr/share/vagrant/gems/bin/vagrant)
mv %{buildroot}%{vagrant_plugin_dir}/bin/%{name}.%{rb_ruby_suffix} \
    %{buildroot}%{vagrant_plugin_dir}/bin/%{name}


# Garbage collection
rm -f %{buildroot}%{vagrant_dir}/test/vagrant-spec/boxes/.keep
rm -f %{buildroot}%{vagrant_dir}/bin/vagrant.orig
rm -f %{buildroot}%{_bindir}/vagrant.orig.%{rb_ruby_suffix}
rm -f %{buildroot}%{vagrant_plugin_dir}/bin/vagrant.orig.%{rb_ruby_suffix}
rm -f %{buildroot}%{vagrant_dir}/lib/vagrant/util.rb.orig

# remove build scripts & nix stuff & go stuff
rm -rf %{buildroot}%{vagrant_dir}/{.runner.sh,Dockerfile,Makefile,go.mod,go.sum,shell.nix,nix,gen.go,flake.lock,flake.nix,vagrant-config.hcl}
# we use our own binstub
rm -rf %{buildroot}%{vagrant_dir}/binstubs/

%fdupes %{buildroot}%{dirname:%vagrant_plugin_dir}

%check

%if %{with tests}
# remove the git reference to vagrant-spec
# -> don't have to cleanup, the Gemfile is excluded anyway
sed -i "s|gem 'vagrant-spec', git.*$|gem 'vagrant-spec'|" Gemfile

export GEM_PATH=%{buildroot}%{vagrant_plugin_dir}:$(ruby.%{rb_ruby_suffix} -e "print Gem.path.reject{|path| path.include? 'home'}.join(':')")
bundle exec rake test:unit
%endif
# with tests

%pre
getent group vagrant >/dev/null || groupadd -r vagrant

%post
%{post_rb}

%transfiletriggerin -- %{dirname:%{vagrant_plugin_spec}}/
%{transfiletriggerin_rb}

%transfiletriggerun -- %{dirname:%{vagrant_plugin_spec}}/
%{transfiletriggerun_rb}

%files
%doc %{vagrant_dir}/CHANGELOG.md
%doc %{vagrant_dir}/README.md
%doc %{vagrant_dir}/README.SUSE
%license %{vagrant_dir}/LICENSE

%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%{macros_vagrant}

# scriptlets
%dir %{dirname: %{post_rb}}
%{post_rb}
%{transfiletriggerin_rb}
%{transfiletriggerun_rb}

%dir %{vagrant_embedded_dir}
%ghost %{vagrant_plugin_conf}

# plugin directories
%dir %{vagrant_plugin_dir}
%dir %{vagrant_plugin_dir}/gems
%dir %{vagrant_plugin_dir}/bin
%dir %{dirname:%{vagrant_plugin_cache}}
%dir %{dirname:%{vagrant_plugin_spec}}
%dir %{dirname:%{vagrant_plugin_docdir}}

# vagrant's own files & directories
%{vagrant_plugin_cache}
%{vagrant_plugin_spec}
%{vagrant_plugin_dir}/bin/%{name}

%dir %{vagrant_dir}
%dir %{vagrant_dir}/bin
%dir %{vagrant_dir}/keys
%dir %{vagrant_dir}/lib
%dir %{vagrant_dir}/plugins
%dir %{vagrant_dir}/templates
%{vagrant_dir}/version.txt
%{vagrant_dir}/%{mod_full_name}.gemspec
%{vagrant_dir}/bin/%{name}
%{vagrant_dir}/keys/*
%{vagrant_dir}/lib/*
%{vagrant_dir}/plugins/*
%{vagrant_dir}/templates/*

# these are scripts for Hashicorp
%exclude %{vagrant_dir}/scripts/*
# either packaged in -vim -emacs subpackages or not relevant
%exclude %{vagrant_dir}/contrib
# various dotfiles we don't care about (.travis.yml et.al.)
%exclude %{vagrant_dir}/.*
# Development files
%exclude %{vagrant_dir}/Vagrantfile
%exclude %{vagrant_dir}/Rakefile
%exclude %{vagrant_dir}/Gemfile
%exclude %{vagrant_dir}/RELEASE.md
%exclude %{vagrant_dir}/tasks/*
# ruby configuration for acceptance tests
%exclude %{vagrant_dir}/vagrant-spec.config.example.rb

%files doc
%dir %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_docdir}/rdoc
%doc %{vagrant_plugin_docdir}/ri

%files vim
%{vim_data_dir}/%{mod_name}.vim

%files emacs
%{_datadir}/emacs/site-lisp/%{mod_name}.el

%files bash-completion
%{_datadir}/bash-completion/completions/%{mod_name}

%changelog
