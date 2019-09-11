#
# spec file for package gpgmepp5
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.5.0
Name:           gpgmepp5
Version:        16.08.3
Release:        0
Summary:        C++ bindings/wrapper for gpgme
License:        LGPL-2.1+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source:         gpgmepp-%{version}.tar.xz
Source1:        baselibs.conf
# FIXME /home/abuild/rpmbuild/BUILD/gpgmepp-4.79.0git/src/verificationresult.h:32:32: fatal error: boost/shared_ptr.hpp: No such file or directory, but no cmake check for boost
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  kf5-filesystem
BuildRequires:  libgpgme-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GpgME++ is a C++ wrapper (or C++ bindings) for the GnuPG project's
gpgme (GnuPG Made Easy) library, version 0.4.4 and later.

%package devel
Summary:        C++ bindings/wrapper for gpgme: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
# FIXME /home/abuild/rpmbuild/BUILD/gpgmepp-4.79.0git/src/verificationresult.h:32:32: fatal error: boost/shared_ptr.hpp: No such file or directory, but no cmake check for boost
# that is a public header
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif
Requires:       libKF5QGpgme5 = %{version}
Requires:       libgpgme-devel
Requires:       pkgconfig
Requires:       pkgconfig(Qt5Core) >= 5.2.0

%description devel
GpgME++ is a C++ wrapper (or C++ bindings) for the GnuPG project's
gpgme (GnuPG Made Easy) library, version 0.4.4 and later.
Development files.

%package -n libKF5QGpgme5
Summary:        C++ bindings/wrapper for gpgme: Build Environment
Group:          Development/Libraries/KDE

%description  -n libKF5QGpgme5
GpgME++ is a C++ wrapper (or C++ bindings) for the GnuPG project's
gpgme (GnuPG Made Easy) library, version 0.4.4 and later.

%prep
%setup -q -n gpgmepp-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON
  %make_jobs

%install
  %kf5_makeinstall -C build

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libKF5QGpgme5 -p /sbin/ldconfig
%postun -n libKF5QGpgme5 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING.LIB README*
%{_kf5_libdir}/libKF5Gpgmepp.so.*
%{_kf5_libdir}/libKF5Gpgmepp-pthread.so.*

%files devel
%defattr(-,root,root)
%doc COPYING.LIB
%{_kf5_libdir}/cmake/KF5Gpgmepp/
%{_kf5_libdir}/libKF5Gpgmepp.so
%{_kf5_libdir}/libKF5Gpgmepp-pthread.so
%{_kf5_includedir}/gpgme++/
%{_kf5_includedir}/gpgmepp_version.h
%{_kf5_libdir}/libKF5QGpgme.so
%{_kf5_includedir}/
%{_kf5_mkspecsdir}/qt_QGpgme.pri

%files -n libKF5QGpgme5
%defattr(-,root,root)
%doc COPYING.LIB
%{_kf5_libdir}/libKF5QGpgme.so.*

%changelog
