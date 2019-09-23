#
# spec file for package cmocka
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           php7-libphutil
%define lib_name libphutil
Version:        0.0~git.20190902T075857~f51f1b3
Release:        0
Summary:        Phabrcator PHP utility classes
License:        Apache-2.0
Group:          Development/Libraries/Other

Url:            https://github.com/phacility/libphutil/
Source0:        %{lib_name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  ca-certificates
BuildRequires:  php7-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       ca-certificates
Requires:       php7
Requires:       php7-curl
Requires:       php7-fileinfo
Requires:       php7-mbstring
Requires:       php7-xmlreader

%description
libphutil is a collection of utility classes and functions for PHP. It is used
by Phabricator and Arcanist.

Some of the major components of libphutil are:
* Core Utilities: a collection of useful functions like ipull() which simplify
  common data manipulation;
* Filesystem: classes like Filesystem which provide a strict API for filesystem
  access and throw exceptions on failure, making it easier to write robust code
  which interacts with files;
* Command Execution: libphutil provides a powerful system command primitive in
  ExecFuture which makes it far easier to write command-line scripts which
  execute system commands (see Command Execution);
* xsprintf(): allows you to define sprintf()-style functions which use custom
  conversions; and
* Library System: an introspectable, inventoried system for organizing PHP code
  and managing dependencies, supported by static analysis.


%prep
%setup -q -n %{lib_name}-%{version}

# remove tests
find src/ -name __tests__ -type d -print0 | xargs -0 rm -rf

%build

%install
install -d -m 0755 %{buildroot}%{_datadir}/phabricator/%{lib_name}
cp -a scripts/ src/ externals/ %{buildroot}%{_datadir}/phabricator/%{lib_name}/

find %{buildroot}%{_datadir}/phabricator/%{lib_name}/scripts/ -type f | \
    xargs sed -i '1 s|/usr/bin/env\ php|/usr/bin/php7|'

install -d -m 0755 %{buildroot}%{_datadir}/phabricator/%{lib_name}/resources/ssl
ln -s /var/lib/ca-certificates/ca-bundle.pem %{buildroot}%{_datadir}/phabricator/%{lib_name}/resources/ssl/default.pem

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README.md
%dir %{_datadir}/phabricator
%dir %{_datadir}/phabricator/%{lib_name}
%{_datadir}/phabricator/%{lib_name}/externals
%{_datadir}/phabricator/%{lib_name}/scripts
%{_datadir}/phabricator/%{lib_name}/src
%{_datadir}/phabricator/%{lib_name}/resources

%changelog
