#
# spec file for package cacti-spine
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


Name:           cacti-spine
Version:        1.2.7
Release:        0
Url:            https://github.com/Cacti/spine
Source:         https://github.com/Cacti/spine/archive/release/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
Requires:       cacti = %{version}
Requires:       rrdtool
Summary:        Threaded poller for Cacti written in C
License:        LGPL-2.1-or-later
Group:          System/Monitoring

%description
Spine is a supplemental poller for Cacti that makes use of pthreads to achieve
excellent performance.

%prep
%setup -q -n spine-release-%{version}

%build
libtoolize --force
aclocal
autoheader
automake --force-missing --add-missing
autoconf

%configure
make %{?_smp_mflags}

%install
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG README.md
%config %{_sysconfdir}/spine.conf.dist
%{_bindir}/spine
%{_mandir}/man1/spine*

%changelog
