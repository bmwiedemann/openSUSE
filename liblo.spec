#
# spec file for package liblo
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lname	liblo7
Name:           liblo
Version:        0.32
Release:        0
Summary:        Open Sound Control implementation
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://liblo.sourceforge.net
Source:         https://downloads.sourceforge.net/liblo/%{name}-%{version}.tar.gz
Source100:      baselibs.conf
BuildRequires:  doxygen
BuildRequires:  pkgconfig

%description
This is an implementation of the OSC protocol
(see http://www.cnmat.berkeley.edu/OpenSoundControl/ for details).

%package -n %{lname}
Summary:        Open Sound Control implementation
Group:          System/Libraries

%description -n %{lname}
This is an implementation of the OSC protocol
(see http://www.cnmat.berkeley.edu/OpenSoundControl/ for details).

%package devel
Summary:        Header files for the liblo OSC implementation
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of liblo.

%prep
%autosetup -p1

%build
echo 'HTML_TIMESTAMP=NO' >> doc/reference.doxygen.in
%configure \
  --disable-static \
  --disable-examples
make %{?_smp_mflags}

%install
%make_install
rm -f examples/Makefile examples/Makefile.in
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/liblo.so.*

%files devel
%license COPYING
%doc doc/html
%doc examples
%{_bindir}/oscdump
%{_bindir}/oscsend
%{_bindir}/oscsendfile
%{_libdir}/liblo.so
%{_includedir}/lo
%{_libdir}/pkgconfig/liblo.pc

%changelog
