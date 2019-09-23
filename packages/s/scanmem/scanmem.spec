#
# spec file for package scanmem
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


Name:           scanmem
Version:        0.17
Release:        0
Summary:        Interactive debugging utility
License:        GPL-3.0
Group:          Development/Tools/Debuggers
Url:            https://github.com/scanmem/scanmem
Source0:        https://github.com/scanmem/scanmem/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         fix-build-with-older-autotools.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  readline-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
scanmem is a debugging utility designed to isolate the address of an
arbitrary variable in an executing process. scanmem simply needs to be told
the PID of the process, and the value of the variable at several different
times. After several scans of the process, scanmem isolates the position of
the variable and allows you to modify its value.

%prep
%setup -q
%patch1 -p1

%build
autoreconf -fiv
intltoolize
%configure --libdir=%{_libdir}/scanmem
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print
find %{buildroot} -type l \( -name '*.so' \) -delete -print
rm -rf %{buildroot}%{_includedir}/scanmem

%files
%defattr(-, root, root)
%{_bindir}/scanmem
%dir %{_libdir}/scanmem
%{_libdir}/scanmem/libscanmem.so.*
%{_datadir}/doc/scanmem
%{_mandir}/man1/scanmem.1%{ext_man}

%changelog
