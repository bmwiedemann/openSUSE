#
# spec file for package suseconnect-ng
#
# Copyright (c) 2021 SUSE LLC
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

%global provider_prefix github.com/SUSE/connect-ng
%global import_path     %{provider_prefix}

Name:           suseconnect-ng
Version:        0.0.1~git0.a5f168a
Release:        0
URL:            https://github.com/SUSE/connect-ng
License:        LGPL-2.1-or-later
Summary:        Utility to register a system with the SUSE Customer Center
Group:          System/Management
Source:         connect-ng-%{version}.tar.xz
Source1:        %name-rpmlintrc
BuildRequires:  golang-packaging
BuildRequires:  go >= 1.16
Conflicts:      SUSEConnect

%description
This package provides a command line tool for connecting a
client system to the SUSE Customer Center. It will connect the system to your
product subscriptions and enable the product repositories/services locally.
suseconnect-ng reduces the size of its runtime dependencies compared to the
replaced SUSEConnect.


%{go_nostrip}
%{go_provides}

%prep
%setup -q -n connect-ng-%{version}

%build
find %_builddir/..
%goprep %{import_path}
find %_builddir/..
go list all
%gobuild suseconnect
# only to test that it compiles, nothing from it is installed for now
make -C %_builddir/go/src/github.com/SUSE/connect-ng build-so-example
find %_builddir/..

%install
%goinstall
ln -s suseconnect %buildroot/%_bindir/SUSEConnect
mkdir %buildroot/%_sbindir
ln -s ../bin/suseconnect %buildroot/%_sbindir/SUSEConnect
#TODO package ruby module
#cp /home/abuild/rpmbuild/BUILD/go/src/github.com/SUSE/connect-ng/ext/libsuseconnect.so %_libdir/libsuseconnect.so
#TODO man pages not yet available in source, these are the names frome the ruby version
#/usr/share/man/man5/SUSEConnect.5.gz
#/usr/share/man/man8/SUSEConnect.8.gz

find %_builddir/..
# we currently do not ship the source for any go module
rm -rf %buildroot/usr/share/go

%check
%gotest github.com/SUSE/connect-ng/connect

%files
%license LICENSE LICENSE.LGPL
%doc README.md
%_bindir/suseconnect
%_bindir/SUSEConnect
%_sbindir/SUSEConnect

