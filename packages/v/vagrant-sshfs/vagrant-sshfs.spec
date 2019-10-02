#
# spec file for package vagrant-sshfs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global vagrant_plugin_name vagrant-sshfs

%global rb_build_versions %rb_default_ruby
%global rb_build_abi %rb_default_build_abi

# don't substitute the name for %%vagrant_plugin_name, obs-service-format_spec
# otherwise messes up the spec's header
Name:           vagrant-sshfs
Version:        1.3.1
Release:        0
%define mod_name %{vagrant_plugin_name}
%define mod_full_name %{vagrant_plugin_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       vagrant
BuildRequires:  vagrant

BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5

# Prevent have choice for rubygem(ruby:2.6.0:mime-types) >= 2
BuildRequires:  %{rubygem mime-types:3 }
# Prevent have choice for rubygem(ruby:2.6.0:builder) >= 2.1.2
BuildRequires:  %{rubygem builder:3.2 }
# Prevent have choice for rubygem(ruby:2.6.0:ffi) >= 0.5.0
BuildRequires:  %{rubygem ffi:1.11 }

Summary:        SSHFS synced folder implementation for Vagrant
License:        GPL-2.0-only
Group:          Development/Languages/Ruby
URL:            https://github.com/dustymabe/%{name}
Source0:        %{URL}/releases/download/v%{version}/%{mod_full_name}.gem
# custom script to automate the test suite run
Source1:        testsuite.sh

# we don't need windows compatibility and don't ship that gem
# source:
# https://src.fedoraproject.org/rpms/vagrant-sshfs/raw/master/f/0001-remove-win32-dep.patch
# PATCH-FIX-OPENSUSE: 0001-remove-win32-dep.patch
Patch0:         0001-remove-win32-dep.patch
# Update the testing vagrant box version
Patch1:         0001-Bump-testing-Vagrant-box-version.patch

%description

This Vagrant plugin adds synced folder support for mounting folders from the
Vagrant host into the Vagrant guest via SSHFS. In the default mode it does this
by executing the SSHFS client software within the guest, which creates an SSH
connection from the Vagrant guest back to the Vagrant host.

%package        -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    -n %{name}-doc
This package contains the documentation for the SSHFS provider to Vagrant.

%package        -n %{name}-testsuite
Summary:        Testsuite for %{name}
Group:          Development/Languages/Ruby
BuildArch:      noarch

Requires:       vagrant-libvirt
Requires:       vagrant-sshfs = %{version}-%{release}

%description    -n %{name}-testsuite
This package contains the testsuite for the SSHFS provider for Vagrant. You most
likely do not want to install this package, unless you want to test
vagrant-sshfs.

%prep
%gem_unpack

%patch0
%patch1 -p1
sed -i "/^.*spec.add_dependency 'win32-process'/d" %{vagrant_plugin_name}.gemspec
chmod +x test/misc/dotests.sh

%build
%gem_build

%install
%vagrant_plugin_install
install -p -m 0755 %{S:1} %{buildroot}/%{vagrant_plugin_instdir}/test/misc/

%files
%{vagrant_plugin_instdir}
%{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%license %{mod_full_name}/LICENSE
%doc %{mod_full_name}/README.adoc

# files for development, we don't want these
%exclude %{vagrant_plugin_instdir}/.gitignore
%exclude %{vagrant_plugin_instdir}/Gemfile
%exclude %{vagrant_plugin_instdir}/Rakefile
%exclude %{vagrant_plugin_instdir}/RELEASE.txt
%exclude %{vagrant_plugin_instdir}/test

%exclude %{vagrant_plugin_instdir}/LICENSE
%exclude %{vagrant_plugin_instdir}/README.adoc

%files -n %{name}-doc
%license %{mod_full_name}/LICENSE
%doc %{vagrant_plugin_docdir}

%files -n %{name}-testsuite
%license %{mod_full_name}/LICENSE
%{vagrant_plugin_instdir}/test

%changelog
