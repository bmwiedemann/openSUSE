#
# spec file for package epplet-base
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


Url:            http://www.enlightenment.org/

Name:           epplet-base
BuildRequires:  Mesa-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  imlib2-devel >= 1.2.0
BuildRequires:  libtool
BuildRequires:  pkg-config >= 0.9.0
Summary:        Applets for the Enlightenment DR16 Window Manager
License:        GPL-2.0+
Group:          System/GUI/Other
Version:        0.10
Release:        0
Source:         epplets-%{version}.tar.bz2
Patch:          epplets-unsuficient_include.patch
Patch1:         epplet-base-linking.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Epplets are programs designed to work with the Enlightenment Window
Manager Version 0.16.  Generally they are quite small and
provide a quick way for a user to perform simple tasks or view
information.

%prep
%setup -q -n epplets-%{version}
%patch 
%patch1 -p1

%build
autoreconf --force --install
CFLAGS="$CFLAGS $RPM_OPT_FLAGS -fno-strict-aliasing" \
%configure --disable-static --with-pic --enable-fsstd
make %{?_smp_mflags}

%check
export MALLOC_CHECK_=2
%{__make} check
unset MALLOC_CHECK_

%install
make DESTDIR=%{buildroot} libdir=%{_libdir} install
rm -f %{buildroot}%{_libdir}/*.la

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
