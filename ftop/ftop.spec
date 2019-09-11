#
# spec file for package ftop
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ftop
Version:        1.0
Release:        0
Summary:        Open File Monitoring
License:        GPL-3.0
Group:          System/Monitoring
Url:            http://code.google.com/p/ftop/
Source:         http://ftop.googlecode.com/files/ftop-%{version}.tar.bz2
Patch1:         ftop-ncurses.patch
Patch2:         ftop-fix_buffer_overflow.patch
Patch3:         ftop-fix_printf_format.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Ftop is to files what top is to processes. The progress of all open files and
file systems can be monitored. If run as a regular user, the set of open files
will be limited to those in that user's processes (which is generally all that
is of interest to the user). In any case, the selection of which files to
display is possible through a wide assortment of options. As with top, the
items are displayed in order from most to least active.

%prep
%setup -q
%patch1
%patch2
%patch3

%build
export CFLAGS="%{optflags} -Wall -DHAVE_LIBCURSES=1"
export CPPFLAGS="$CFLAGS"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/ftop
%doc %{_mandir}/man1/ftop.1%{ext_man}

%changelog
