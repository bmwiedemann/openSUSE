#
# spec file for package vagrant-libvirt
#
# Copyright (c) 2020 SUSE LLC
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


# FIXME: for now vagrant does not support Ruby 2.7
%if 0%{?suse_version} > 1500
%global rb_build_versions ruby26
%global rb_build_abi ruby:2.6.0
%global rb_ruby_suffix ruby2.6
%else
%global rb_build_versions %rb_default_ruby
%global rb_build_abi %rb_default_ruby_abi
%global rb_ruby_suffix %rb_default_ruby_suffix
%endif

Name:           vagrant-libvirt
Version:        0.0.45
Release:        0
%define mod_name vagrant-libvirt
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       libvirt
Requires:       vagrant
Recommends:     qemu-kvm
BuildRequires:  vagrant

BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5

# for tests:
BuildRequires:  %{rubygem bundler}
BuildRequires:  %{rubygem rspec}
BuildRequires:  %{rubygem vagrant-spec}
# BuildRequire the same gems as Required
BuildRequires:  %{rubygem fog-core:2 >= 2.1}
BuildRequires:  %{rubygem fog-libvirt >= 0.3.}

# s.add_development_dependency "rspec-core", "~> 3.5.0"
BuildRequires:  %{rubygem rspec-core:3.5}
# s.add_development_dependency "rspec-expectations", "~> 3.5.0"
BuildRequires:  %{rubygem rspec-expectations:3.5}
# s.add_development_dependency "rspec-mocks", "~> 3.5.0"
BuildRequires:  %{rubygem rspec-mocks:3.5}
# s.add_development_dependency 'rake'
BuildRequires:  %{rubygem rake}

# s.add_runtime_dependency 'fog-libvirt', '>= 0.3.0'
Requires:       %{rubygem fog-libvirt >= 0.3.}
# s.add_runtime_dependency 'fog-core', '~> 2.1'
Requires:       %{rubygem fog-core:2 >= 2.1}
# s.add_runtime_dependency 'nokogiri', '~> 1.6'
Requires:       %{rubygem nokogiri:1 >= 1.6 }

# s.add_runtime_dependency 'nokogiri', '~> 1.6'
# Prevent have choice for rubygem(ruby:2.6.0:nokogiri) >= 1.5.11
BuildRequires:  %{rubygem nokogiri:1.10 }
# Prevent have choice for rubygem(ruby:2.6.0:mime-types) >= 2
BuildRequires:  %{rubygem mime-types:3 }
# Prevent have choice for rubygem(ruby:2.6.0:builder) >= 2.1.2
BuildRequires:  %{rubygem builder:3.2 }
# Prevent have choice for rubygem(ruby:2.6.0:ffi) >= 0.5.0
BuildRequires:  %{rubygem ffi >= 1.9 }
# Prevent have choice for rubygem(ruby:2.5.0:thor:0) >= 0.18
BuildRequires:  %{rubygem thor:0.19}

# required when using a non-default ruby version
BuildRequires:  %{rubygem gem2rpm}

URL:            https://github.com/vagrant-libvirt/vagrant-libvirt
Source:         https://rubygems.org/gems/%{mod_full_name}.gem

# FIXME: drop this once 0.0.46 comes out
# these are cherry-picked fixes for vagrant-libvirt.gemspec
# PATCH-FIX-UPSTREAM: 0001-Revert-back-to-development-versiongemspec-file..patch
Patch0:         0001-Revert-back-to-development-versiongemspec-file..patch
# PATCH-FIX-UPSTREAM: 0002-Use-the-same-version-of-Nokogiri-as-Vagrant.patch
Patch1:         0002-Use-the-same-version-of-Nokogiri-as-Vagrant.patch
# PATCH-FIX-UPSTREAM: 0003-Update-fog-core-to-latest-version.patch
Patch2:         0003-Update-fog-core-to-latest-version.patch

Summary:        Vagrant provider for libvirt
License:        MIT
Group:          Development/Languages/Ruby

%description
This is a Vagrant plugin that adds a Libvirt provider to Vagrant, allowing
Vagrant to control and provision machines via the Libvirt toolkit.

%package        -n %{name}-doc
Summary:        Documentation for vagrant-libvirt
Group:          Documentation/HTML

%description    -n %{name}-doc
This package contains the documentation for the Libvirt provider to Vagrant.


%global vagrant_plugin_name %{name}

%prep
%gem_unpack

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Dirty hack: since the vagrant-libvirt-0.0.45.gemspec comes from the gem and is
# not patched to contain the updated dependency of fog-core, we fix this manually
# FIXME: remove this by 0.0.46
sed -i "s:~> 1.43.0:~> 2.1:" %{mod_full_name}.gemspec

# fix shebang & preserve timestamps
sed -i.orig "s:^#\!/usr/bin/env\s\+bash\s\?:#\!/bin/bash:" tools/create_box.sh
touch -r tools/create_box.sh.orig tools/create_box.sh
rm tools/create_box.sh.orig

%build
%gem_build

%install
%vagrant_plugin_install

%check
# Use the actual gemspec for tests
mv %{buildroot}%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec \
    %{buildroot}%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec.old

cp %{mod_full_name}/%{mod_full_name}.gemspec \
   %{buildroot}%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec
pushd %{buildroot}%{vagrant_plugin_instdir}

# Create dummy Gemfile and load dependencies via the gemspec
echo "gem 'vagrant'" > Gemfile
echo "gem 'rdoc'" >> Gemfile
echo "gem 'vagrant-spec'" >> Gemfile
echo "gemspec" >> Gemfile

# We don't care about code coverage.
sed -i '/[cC]overalls/ s/^/#/' spec/spec_helper.rb

# Relax developement rspec dependency
sed -i '/rspec/ s/~>/>=/' %{vagrant_plugin_name}.gemspec

export GEM_PATH=%{vagrant_plugin_dir}:`ruby.%{vagrant_rb_ruby_suffix} -e "print Gem.path.join(':')"`
bundle exec rspec spec

rm %{vagrant_plugin_name}.gemspec
mv %{vagrant_plugin_name}.gemspec.old %{vagrant_plugin_name}.gemspec
popd

%files
%{vagrant_plugin_instdir}
%{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%doc %{mod_full_name}/README.md
%license %{mod_full_name}/LICENSE

%exclude %{vagrant_plugin_instdir}/.*
%exclude %{vagrant_plugin_instdir}/Gemfile
%exclude %{vagrant_plugin_instdir}/Rakefile
%exclude %{vagrant_plugin_instdir}/README.md
%exclude %{vagrant_plugin_instdir}/LICENSE

%files -n %{name}-doc
%doc %{vagrant_plugin_docdir}

%changelog
