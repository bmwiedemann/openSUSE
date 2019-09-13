#
# spec file for package tipcutils
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


Name:           tipcutils
Version:        2.1.1
Release:        0
Summary:        Transparent Inter Process Communication Protocol
License:        BSD-3-Clause
Group:          Development/Tools/Other
Url:            https://sourceforge.net/projects/tipc/files/tipc-utils
Source0:        https://sourceforge.net/projects/tipc/files/tipc-utils/%{name}-%{version}.tar
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libdaemon-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
TIPC utilities (tipcutils) is a set of userspace programs used to
configure and manage TIPC (http://tipc.sourceforge.net/).

The Transparent Inter Process Communication protocol allows
applications in a clustered computer environment to communicate quickly
and reliably with other applications, regardless of their location
within the cluster.

%prep
%setup -q

%build
./bootstrap
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%{_sbindir}/tipc-config
%{_bindir}/tipc-pipe
%{_sbindir}/tipclog
%{_mandir}/man1/tipc-config.1%{ext_man}
%{_mandir}/man1/tipc-pipe.1%{ext_man}

%changelog
