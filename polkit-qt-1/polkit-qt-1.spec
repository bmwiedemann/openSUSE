#
# spec file for package polkit-qt-1
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define debug_package_requires libpolkit-qt-1-0 = %{version}-%{release}

Name:           polkit-qt-1
Version:        0.112.0
Release:        0
Summary:        PolicyKit Library Qt Bindings
License:        LGPL-2.1+
Group:          Development/Libraries/KDE
Url:            http://api.kde.org/kdesupport-api/kdesupport-apidocs/polkit-qt/html/
Source0:        http://download.kde.org/stable/apps/KDE4.x/admin//%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM do-not-use-global-static-systembus-instance.patch
Patch0:         do-not-use-global-static-systembus-instance.patch
BuildRequires:  automoc4
BuildRequires:  cmake
BuildRequires:  kde4-filesystem
BuildRequires:  libqt4-devel
BuildRequires:  polkit-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Polkit-qt-1 aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%package -n libpolkit-qt-1-1
Summary:        PolicyKit Library Qt Bindings
Group:          Development/Libraries/KDE
Provides:       libpolkit-qt0 = 0.9.3
Obsoletes:      libpolkit-qt0 < 0.9.3

%description -n libpolkit-qt-1-1
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%package -n libpolkit-qt-1-devel
Summary:        PolicyKit Library Qt Bindings
Group:          Development/Libraries/KDE
Requires:       libpolkit-qt-1-1 = %{version}
Requires:       polkit-devel
Provides:       libpolkit-qt-devel = 0.9.3
Obsoletes:      libpolkit-qt-devel < 0.9.3

%description -n libpolkit-qt-1-devel
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and
QAbstractButton that lets you integrate those two components easily
with PolicyKit.

%prep
%setup -q
%patch0 -p1

%build
  %cmake_kde4 -d build
  %make_jobs

%install
  cd build
  %make_install

%post -n libpolkit-qt-1-1 -p /sbin/ldconfig

%postun -n libpolkit-qt-1-1 -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n libpolkit-qt-1-devel
%defattr(-,root,root)
%doc AUTHORS README
%{_kde4_includedir}/polkit-qt-1/
%{_kde4_libdir}/pkgconfig/polkit-qt*
%{_kde4_libdir}/libpolkit-qt-gui-1.so
%{_kde4_libdir}/libpolkit-qt-core-1.so
%{_kde4_libdir}/libpolkit-qt-agent-1.so
%{_kde4_libdir}/cmake/PolkitQt-1/

%files -n libpolkit-qt-1-1
%defattr(-,root,root)
%{_kde4_libdir}/libpolkit-qt-gui-1.so.*
%{_kde4_libdir}/libpolkit-qt-core-1.so.*
%{_kde4_libdir}/libpolkit-qt-agent-1.so.*

%changelog
