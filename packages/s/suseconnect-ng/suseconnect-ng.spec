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
Version:        0.0.4~git0.64b80e9
Release:        0
URL:            https://github.com/SUSE/connect-ng
License:        LGPL-2.1-or-later
Summary:        Utility to register a system with the SUSE Customer Center
Group:          System/Management
Source:         connect-ng-%{version}.tar.xz
Source1:        %name-rpmlintrc
BuildRequires:  go >= 1.16
BuildRequires:  golang-packaging
BuildRequires:  ruby-devel
BuildRequires:  zypper
Obsoletes:      SUSEConnect < 0.3.99
Provides:       SUSEConnect = 0.3.99
Obsoletes:      zypper-migration-plugin < 0.99
Provides:       zypper-migration-plugin = 0.99
Obsoletes:      zypper-search-packages-plugin < 0.99
Provides:       zypper-search-packages-plugin = 0.99
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos_version}
Requires:       ca-certificates
%else
Requires:       ca-certificates-mozilla
%endif
Requires:       coreutils
# ExclusiveArch from this package
%ifarch %ix86 ia64 x86_64 %arm aarch64
Requires:       dmidecode
%endif
# ExclusiveArch from this package
%ifarch s390x
Requires:       s390-tools
%endif
Requires:       systemd
Requires:       zypper
# lscpu is only used on those
%ifarch x86_64 aarch64
Requires:       util-linux
%endif

%description
This package provides a command line tool for connecting a
client system to the SUSE Customer Center. It will connect the system to your
product subscriptions and enable the product repositories/services locally.
suseconnect-ng reduces the size of its runtime dependencies compared to the
replaced SUSEConnect.


%{go_nostrip}
%{go_provides}

%package -n libsuseconnect
Summary:        C interface to suseconnect-ng.
Group:          System/Management
# the CLI is not used by libsuseconnect but it has the same dependencies and it's easier to keep one list above
Requires:       suseconnect-ng

%description -n libsuseconnect
This package contains library which provides C interface to selected
suseconnect-ng functions.

%package -n suseconnect-ruby-bindings
Summary:        Ruby bindings for libsuseconnect library.
Group:          System/Management
Requires:       libsuseconnect
Requires:       rubygem(ffi)

%description -n suseconnect-ruby-bindings
This package provides bindings needed to use libsuseconnect from Ruby scripts.

%prep
%setup -q -n connect-ng-%{version}

%build
find %_builddir/..
echo %{version} > internal/connect/version.txt
%goprep %{import_path}
find %_builddir/..
go list all
%gobuild suseconnect
mkdir -p %_builddir/go/lib
go build -v -buildmode=c-shared -o %_builddir/go/lib/libsuseconnect.so %import_path/libsuseconnect
find %_builddir/..

%install
%goinstall
ln -s suseconnect %buildroot/%_bindir/SUSEConnect
install -d -m0755 %buildroot/%_sbindir %buildroot/usr/lib/zypper/commands
ln -s %_bindir/suseconnect %buildroot/%_sbindir/SUSEConnect
ln -s %_bindir/suseconnect %buildroot/usr/lib/zypper/commands/zypper-migration
ln -s %_bindir/suseconnect %buildroot/usr/lib/zypper/commands/zypper-search-packages
install -D -m0755 %_builddir/go/lib/libsuseconnect.so %buildroot/%_libdir/libsuseconnect.so
install -d -m0755 %buildroot/%_libdir/ruby/vendor_ruby/%rb_ver
cp -r %_builddir/go/src/%import_path/yast/lib/* %buildroot/%_libdir/ruby/vendor_ruby/%rb_ver
#TODO man pages not yet available in source, these are the names frome the ruby version
#/usr/share/man/man5/SUSEConnect.5.gz
#/usr/share/man/man8/SUSEConnect.8.gz
#/usr/share/man/man8/zypper-migration.8.gz
#/usr/share/man/man8/zypper-search-packages.8.gz

find %_builddir/..
# we currently do not ship the source for any go module
rm -rf %buildroot/usr/share/go

%check
%gotest -v %import_path/internal/connect
%gotest -v %import_path/suseconnect
make -C %_builddir/go/src/%import_path gofmt

%files
%license LICENSE LICENSE.LGPL
%doc README.md
%_bindir/suseconnect
%_bindir/SUSEConnect
%_sbindir/SUSEConnect
/usr/lib/zypper/commands

%files -n libsuseconnect
%license LICENSE LICENSE.LGPL
%_libdir/libsuseconnect.so

%files -n suseconnect-ruby-bindings
%doc yast/README.md
%_libdir/ruby/vendor_ruby/%rb_ver/suse

%changelog
