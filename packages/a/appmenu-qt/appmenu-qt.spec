#
# spec file for package appmenu-qt
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


%define rversion 0.2.7daily13.05.02

Name:           appmenu-qt
Version:        0.2.7~daily13.05.02
Release:        0
Summary:        Application Menu for Qt
License:        LGPL-3.0
Group:          System/GUI/KDE
Url:            https://launchpad.net/appmenu-qt/
Source0:        http://archive.ubuntu.com/ubuntu/pool/main/a/%{name}/%{name}_%{rversion}.orig.tar.gz
BuildRequires:  cmake >= 2.8.0
BuildRequires:  libdbusmenu-qt-devel >= 0.9.0
BuildRequires:  libqt4-devel >= 4.8.0
Requires:       dbus-1
Requires:       libqt4 >= 4.8.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Defined by libqt4-x11 > 4.8.2
%{!?_libqt4_pluginsdir: %global _libqt4_pluginsdir %{_libdir}/qt4/plugins}

%description
This projects adds support for application menu to Qt.

%prep
%setup -q -n %{name}-%{rversion}

%build
export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS
mkdir build && cd build && \
cmake -DCMAKE_SKIP_RPATH=ON \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DUSE_QT4=ON \
      -DUSE_QT5=OFF \
      -DCMAKE_BUILD_TYPE=release ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root,-)
%doc COPYING* LGPL_EXCEPTION.txt NEWS README
%dir %{_libqt4_pluginsdir}/menubar
%{_libqt4_pluginsdir}/menubar/libappmenu-qt.so

%changelog
