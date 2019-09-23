#
# spec file for package mono-debugger
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mono-debugger
Summary:        Mono Debugger
License:        GPL-2.0+ and LGPL-2.0+ and MIT
Group:          Development/Languages/Mono
Url:            http://www.mono-project.com/Debugger
Version:        2.10
Release:        0
Source:         http://download.mono-project.com/sources/mono-debugger/%{name}-%{version}.tar.bz2
Source99:       mono-debugger-rpmlintrc
Patch1:         mono-debugger-glib.patch
Patch2:         mono-v4-install.patch
# PATCH-FIX-OPENSUSE fix build error with mono 5.10 and up
Patch3:         mono-510-build-fix.patch
ExclusiveArch:  %ix86 x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       mono-core >= 2.7
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  libmono-2_0-devel
BuildRequires:  libtool
BuildRequires:  mono-devel
BuildRequires:  mono-nunit
BuildRequires:  ncurses-devel

%description
A debugger is an important tool for development. The Mono Debugger
(MDB) can debug both managed and unmanaged applications.  It provides a
reusable library that can be used to add debugger functionality to
different front-ends. The debugger package includes a console debugger
named "mdb", and MonoDevelop (http://www.monodevelop.com) provides a
GUI interface to the debugger.

%define mcsver %({ mcs --version | awk '{print $5}' | cut -f1 -d"." ; mcs --version | awk '{print $5}' | cut -f2 -d"." ; } | xargs printf "%03d")

%if 0%{?mcsver} >= 4000
%define target_dir 4.5
%else
%define target_dir 2.0
%endif

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README NEWS
%{_bindir}/mdb*
%{_libdir}/*.so*
%{_prefix}/lib/mono/%{target_dir}/mdb*.exe
%{_prefix}/lib/mono/gac/Mono.Debugger*
%{_prefix}/lib/mono/mono-debugger
%{_libdir}/pkgconfig/mono-debugger*.pc

%prep
%setup -q
%patch1 -p1
%if 0%{?mcsver} >= 4000
%patch2 -p1
%endif
%patch3 -p1

%build
%if 0%{?mcsver} >= 4000
export MCS="/usr/bin/mcs"
%endif

autoreconf -fiv
%configure
make

%install
make install DESTDIR=%{buildroot}
# Unset executable bit on .exe files
# This prevents the dbuginfo macros from scanning them
find %{buildroot} -name '*.exe' -exec chmod a-x '{}' ';'
find %{buildroot} -name '*.dll' -exec chmod a-x '{}' ';'
# Remove unnecessary devel files
rm -f %{buildroot}%_libdir/*.la
rm -f %{buildroot}%_libdir/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
