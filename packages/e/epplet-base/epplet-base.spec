#
# spec file for package epplet-base
#
# Copyright (c) 2019 SUSE LLC
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


Name:           epplet-base
Version:        0.10
Release:        0
Summary:        Applets for the Enlightenment DR16 Window Manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://www.enlightenment.org/
Source:         epplets-%{version}.tar.bz2
Patch0:         epplets-unsuficient_include.patch
Patch1:         epplet-base-linking.patch
BuildRequires:  Mesa-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  imlib2-devel >= 1.2.0
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(xext)

%description
Epplets are programs designed to work with the Enlightenment Window
Manager Version 0.16.  Generally they are quite small and
provide a quick way for a user to perform simple tasks or view
information.

%prep
%setup -q -n epplets-%{version}
%patch0
%patch1 -p1

%build
autoreconf --force --install
CFLAGS="$CFLAGS %{optflags} -fno-strict-aliasing" \
%configure --disable-static --with-pic --enable-fsstd
make %{?_smp_mflags}

%check
export MALLOC_CHECK_=2
make %{?_smp_mflags} check
unset MALLOC_CHECK_

%install
make DESTDIR=%{buildroot} libdir=%{_libdir} install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 755)
%{_bindir}/E*epplet
%{_includedir}/epplet.h
%{_libdir}/libepplet*
%dir %{_datadir}/e16
%{_datadir}/e16/epplet_icons
%{_datadir}/e16/epplet_data

%changelog
