#
# spec file for package qt4-assistant-adp
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


Name:           qt4-assistant-adp
BuildRequires:  fdupes
BuildRequires:  libqt4-devel
BuildRequires:  update-desktop-files
Url:            http://www.qtsoftware.com
Summary:        C++ Program Library, Core Components
License:        SUSE-LGPL-2.1-with-nokia-exception-1.1 or GPL-3.0
Group:          System/Libraries
Version:        4.6.3
Release:        0
Source:         qt-assistant-qassistantclient-library-compat-src-%version.tar.bz2
Source2:        baselibs.conf
Patch0:         fix_build_system.diff
Patch1:         hardcode-lib-version.diff
Patch2:         add-camelcase-headers.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libQtAssistantClient4 = %version
Provides:       libqt4-devel-doc:/usr/bin/assistant_adp

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.



Authors:
--------
    Qt Software

%prep
%define plugindir %_libdir/qt4/plugins
%setup -q -n  qt-assistant-qassistantclient-library-compat-version-%version
%patch0 -p1
%patch1
%patch2

%package devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       %name = %version

%description devel
You need this package, if you want to compile programs with Qt. It
contains the "Qt Crossplatform Development Kit". It does contain
include files and development applications like GUI designers,
translator tools and code generators.



%package -n libQtAssistantClient4
Summary:        Qt Development Kit
Group:          Development/Libraries/X11

%description -n libQtAssistantClient4
You need this package, if you want to compile programs with Qt. It
contains the "Qt Crossplatform Development Kit". It does contain
include files and development applications like GUI designers,
translator tools and code generators.




%build
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS"
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
qmake
make %{?jobs:-j %jobs}

pushd lib
    qmake
    make %{?jobs:-j %jobs}
popd

pushd translations
    lrelease assistant_adp_*.ts
popd

%install
make INSTALL_ROOT=$RPM_BUILD_ROOT install
pushd lib
    make INSTALL_ROOT=$RPM_BUILD_ROOT install
popd

mkdir -p %{buildroot}/usr/share/qt4/translations/
install -p -m 644 translations/assistant_adp_*.qm %{buildroot}/usr/share/qt4/translations/

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libQtAssistantClient4 -p /sbin/ldconfig

%postun -n libQtAssistantClient4 -p /sbin/ldconfig

%files
%defattr(-,root,root,755)
/usr/bin/assistant_adp
/usr/share/qt4/translations/assistant_adp_*.qm

%files -n libQtAssistantClient4
%defattr(-,root,root,755)
%_libdir/libQtAssistantClient.so.4*

%files devel
%defattr(644,root,root,755)
/usr/include/QtAssistant
%_libdir/libQtAssistantClient.so

%changelog
