#
# spec file for package qgpgme
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 15
%if 0%{?suse_version} >= 1600
%bcond_without qt6
%else
%bcond_with qt6
%endif
Name:           qgpgme
Version:        2.0.0
Release:        0
Summary:        Qt API bindings/wrapper for GPGME
License:        GPL-2.0-or-later
URL:            https://www.gnupg.org/software/gpgme/index.html
Source:         https://www.gnupg.org/ftp/gcrypt/qgpgme/%{name}-%{version}.tar.xz
Source1:        https://www.gnupg.org/ftp/gcrypt/qgpgme/%{name}-%{version}.tar.xz.sig
# https://www.gnupg.org/signature_key.html
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(Gpgmepp) >= 2.0.0
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  pkgconfig(gpg-error) >= 1.47
BuildRequires:  pkgconfig(gpgme) >= 2.0.0
%if %{with qt6}
BuildRequires:  cmake(Qt6Core) >= 6.5.0
BuildRequires:  cmake(Qt6CoreTools) >= 6.9.1
BuildRequires:  cmake(Qt6Test)
%endif
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%endif

%description
QGpgme provides a very high level Qt API around GpgMEpp.

%package -n libqgpgme%{sover}
Summary:        Qt5 API bindings/wrapper for GPGME

%description -n libqgpgme%{sover}
QGpgme provides a very high level Qt API around GpgMEpp.

This package contains the shared library built for Qt5.

%if %{with qt6}
%package -n libqgpgmeqt6-%{sover}
Summary:        Qt6 API bindings/wrapper for GPGME

%description -n libqgpgmeqt6-%{sover}
QGpgme provides a very high level Qt API around GpgMEpp.

This package contains the shared library built for Qt6.
%endif

%package -n libqgpgme-devel
Summary:        Development files for %{name} (Qt5)
Requires:       libqgpgme%{sover} = %{version}
Requires:       cmake(Gpgmepp) >= 2.0.0

%description -n libqgpgme-devel
QGpgme provides a very high level Qt API around GpgMEpp.

This package contains the files needed to build using %{name} and Qt5.

%if %{with qt6}
%package -n libqgpgmeqt6-devel
Summary:        Development files for %{name} (Qt6)
Requires:       libqgpgmeqt6-%{sover} = %{version}
Requires:       cmake(Gpgmepp) >= 2.0.0

%description -n libqgpgmeqt6-devel
QGpgme provides a very high level Qt API around GpgMEpp.

This package contains the files needed to build using %{name} and Qt6.
%endif

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif
%cmake \
	-DBUILD_WITH_QT5:BOOL=ON \
%if %{with qt6}
	-DBUILD_WITH_QT6:BOOL=ON \
%endif
	-DBUILD_TESTING:BOOL=ON \
	%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n libqgpgme%{sover}
%if %{with qt6}
%ldconfig_scriptlets -n libqgpgmeqt6-%{sover}
%endif

%files -n libqgpgme%{sover}
%license COPYING
%{_libdir}/libqgpgme.so.%{sover}{,.*}

%if %{with qt6}
%files -n libqgpgmeqt6-%{sover}
%license COPYING
%{_libdir}/libqgpgmeqt6.so.%{sover}{,.*}
%endif

%files -n libqgpgme-devel
%license COPYING
%doc ChangeLog NEWS README VERSION
%{_libdir}/libqgpgme.so
%{_includedir}/qgpgme-qt5
%{_libdir}/cmake/QGpgme

%if %{with qt6}
%files -n libqgpgmeqt6-devel
%license COPYING
%doc ChangeLog NEWS README VERSION
%{_libdir}/libqgpgmeqt6.so
%{_includedir}/qgpgme-qt6
%{_libdir}/cmake/QGpgmeQt6
%endif

%changelog
