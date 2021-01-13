#
# spec file for package tiptop
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


Name:           tiptop
Version:        2.3.1
Release:        0
Summary:        Performance monitoring tool using hardware counters
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://tiptop.gforge.inria.fr/
Source:         http://tiptop.gforge.inria.fr/releases/tiptop-%{version}.tar.gz
# PATCH-FIX-UPSTREAM reproducible.patch by bmwiedemann - override build date and build host (boo#1047218, boo#1084909) - sent upstream via email
Patch0:         reproducible.patch
BuildRequires:  autoconf >= 2.68
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncurses)

%description
Tiptop is a performance monitoring tool for Linux. It provides a dynamic
real-time view of the tasks running in the system. Tiptop is very similar
to the top utility, but most of the information displayed comes from
hardware counters.

%prep
%setup -q
%patch0 -p1

%build
export HOSTNAME=reproducible-openSUSE
sed -i "s/curses/ncurses/g" configure.ac
autoconf -f -i
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/tiptop
%{_bindir}/ptiptop
%{_mandir}/man1/tiptop.1%{?ext_man}
%{_mandir}/man1/ptiptop.1%{?ext_man}

%changelog
