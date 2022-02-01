#
# spec file for package vagrant-libvirt
#
# Copyright (c) 2022 SUSE LLC
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


%global rb_build_versions %rb_default_ruby
%global rb_build_abi %rb_default_ruby_abi
%global rb_ruby_suffix %rb_default_ruby_suffix

Name:           vagrant-libvirt
Version:        0.7.0
Release:        0
%define mod_name vagrant-libvirt
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       libvirt
%ifarch %ix86 x86_64
Requires:       qemu-x86
%endif
# switch to %%elifarch once every platform that we care about has rpm >= 4.15
%ifarch %arm %arm64
Requires:       qemu-arm
%endif
Requires:       vagrant
# for virt-sysprep
Recommends:     guestfs-tools
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

# s.add_development_dependency "rspec-core", ">= 3.5"
BuildRequires:  %{rubygem rspec-core >= 3.5}
# s.add_development_dependency "rspec-expectations", ">= 3.5"
BuildRequires:  %{rubygem rspec-expectations >= 3.5}
# s.add_development_dependency "rspec-mocks", ">= 3.5"
BuildRequires:  %{rubygem rspec-mocks >= 3.5}
# s.add_development_dependency 'rake'
BuildRequires:  %{rubygem rake}

# s.add_runtime_dependency 'fog-libvirt', '>= 0.6.0'
Requires:       %{rubygem fog-libvirt >= 0.6.}
# s.add_runtime_dependency 'fog-core', '~> 2.1'
Requires:       %{rubygem fog-core:2 >= 2.1}
# s.add_runtime_dependency 'nokogiri', '~> 1.6'
Requires:       %{rubygem nokogiri:1 >= 1.6 }

# required when using a non-default ruby version
BuildRequires:  %{rubygem gem2rpm}

# Prevent: have choice for rubygem(ruby:2.7.0:childprocess) >= 0
BuildRequires:  %{rubygem childprocess > 3}

BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  kmod

URL:            https://github.com/vagrant-libvirt/vagrant-libvirt
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Patch0:         0001-Remove-simplecov-from-tests.patch
Patch1:         0002-Double-the-UDPSocket-in-cases-where-there-s-no-netwo.patch
Patch2:         0003-Allow-the-connection.client.libversion-call-1416.patch

Summary:        Vagrant provider for libvirt
License:        MIT

%description
This is a Vagrant plugin that adds a Libvirt provider to Vagrant, allowing
Vagrant to control and provision machines via the Libvirt toolkit.

%package        -n %{name}-doc
Summary:        Documentation for vagrant-libvirt

%description    -n %{name}-doc
This package contains the documentation for the Libvirt provider to Vagrant.


%global vagrant_plugin_name %{name}

%prep
%gem_unpack
# remove dropped or unneeded dependencies
sed -i '/simplecov/d' %{mod_full_name}.gemspec

# this is essentially https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1330
# FIXME: drop this on the next upstream release
sed -i 's/\["~> 3.5.0"\]/\[">= 3.5"\]/' %{mod_full_name}.gemspec
%autopatch -p1

%build
%gem_build

%install
%vagrant_plugin_install
%fdupes %{buildroot}%{vagrant_plugin_instdir}

%check
# Use the actual gemspec for tests
cp %{mod_full_name}/%{mod_full_name}.gemspec \
   %{buildroot}%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec
pushd %{buildroot}%{vagrant_plugin_instdir}

# Create dummy Gemfile and load dependencies via the gemspec
echo "gem 'vagrant'" > Gemfile
echo "gem 'rdoc'" >> Gemfile
echo "gem 'vagrant-spec'" >> Gemfile
echo "gemspec" >> Gemfile

# Relax developement rspec dependency
sed -i '/rspec/ s/~>/>=/' %{vagrant_plugin_name}.gemspec

export GEM_PATH=%{vagrant_plugin_dir}:`ruby.%{vagrant_rb_ruby_suffix} -e "print Gem.path.join(':')"`
bundle exec rspec spec

rm %{vagrant_plugin_name}.gemspec
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
