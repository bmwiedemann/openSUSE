#
# spec file for package vagrant-sshfs
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


%global rb_build_versions %rb_default_ruby
%global rb_build_abi %rb_default_ruby_abi
%global rb_ruby_suffix %rb_default_ruby_suffix

%global vagrant_plugin_name vagrant-sshfs
%define mod_name %{vagrant_plugin_name}
%define mod_full_name %{vagrant_plugin_name}-%{version}
Name:           %{vagrant_plugin_name}
Version:        1.3.5
Release:        0
Summary:        SSHFS synced folder implementation for Vagrant
License:        GPL-2.0-only
Group:          Development/Languages/Ruby
URL:            https://github.com/dustymabe/%{name}
Source0:        %{URL}/releases/download/v%{version}/%{mod_full_name}.tar.gz
Source1:        %{URL}/releases/download/v%{version}/%{mod_full_name}.tar.gz.asc
# Dusty Mabe's key
Source2:        https://keybase.io/dustymabe/pgp_keys.asc#/%{name}.keyring
# custom script to automate the test suite run
Source3:        testsuite.sh
# FIX-OPENSUSE use the Tumbleweed.$(uname -m) vagrant box instead of fedora/*-cloud-base
Patch0:         0001-Use-opensuse-Tumbleweed.-uname-m-box-instead-of-Fedo.patch
# PATCH-FIX-OPENSUSE vagrant-sshfs-libexecdir.patch -- Use /usr/libexecdir/ssh to find sftp-server
Patch1:         vagrant-sshfs-libexecdir.patch
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  vagrant >= 1.9.1
Requires:       sshfs
Requires:       vagrant >= 1.9.1

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
Requires:       vagrant-libvirt
Requires:       vagrant-sshfs = %{version}-%{release}

%description    -n %{name}-testsuite
This package contains the testsuite for the SSHFS provider for Vagrant. You most
likely do not want to install this package, unless you want to test
vagrant-sshfs.

%prep
%autosetup -c -p1

# since we don't have the full git repo we can't use `git ls-files`
sed -i 's/git ls-files -z/find . -type f -print0/' %{vagrant_plugin_name}.gemspec

# remove dependencies on windows libraries (needed for windows, not linux)
sed -i '/win32-process/d' %{vagrant_plugin_name}.gemspec
chmod +x test/misc/dotests.sh

mv %{vagrant_plugin_name}.gemspec %{mod_full_name}.gemspec

%build
%{gem_build}

%install
%vagrant_plugin_install -n %{mod_full_name}.gem
install -p -m 0755 %{SOURCE3} %{buildroot}/%{vagrant_plugin_instdir}/test/misc/

%files
%{vagrant_plugin_instdir}
%{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%license LICENSE
%doc README.adoc

# files for development, we don't want these
%exclude %{vagrant_plugin_instdir}/.gitignore
%exclude %{vagrant_plugin_instdir}/Gemfile
%exclude %{vagrant_plugin_instdir}/Rakefile
%exclude %{vagrant_plugin_instdir}/RELEASE.txt
%exclude %{vagrant_plugin_instdir}/test

%exclude %{vagrant_plugin_instdir}/LICENSE
%exclude %{vagrant_plugin_instdir}/README.adoc

%files -n %{name}-doc
%license LICENSE
%doc %{vagrant_plugin_docdir}

%files -n %{name}-testsuite
%license LICENSE
%{vagrant_plugin_instdir}/test

%changelog
