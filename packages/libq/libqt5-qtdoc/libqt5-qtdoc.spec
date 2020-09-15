#
# spec file for package libqt5-qtdoc
#
# Copyright (c) 2020 SUSE LLC
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
# nodebuginfo


%define real_version 5.15.1
%define tar_version qt-everywhere-src-5.15.1
Name:           libqt5-qtdoc
Version:        5.15.1
Release:        0
Summary:        Qt 5 API Documentation
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Documentation/Other
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/single/%{tar_version}.tar.xz
# Breaks make_jobs
#!BuildIgnore:  cmake
BuildRequires:  alsa-devel
BuildRequires:  bison
BuildRequires:  clang
BuildRequires:  cups-devel
BuildRequires:  double-conversion-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libpng-devel
BuildRequires:  libproxy-devel
BuildRequires:  libpulse-devel
BuildRequires:  libqt5-qtbase-devel >= %{version}
BuildRequires:  libqt5-qttools >= %{version}
BuildRequires:  libqt5-qttools-devel >= %{version}
BuildRequires:  libqt5-qttools-doc >= %{version}
BuildRequires:  libqt5-qtbase-common-devel >= %{version}
BuildRequires:  libtiff-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
BuildRequires:  tslib-devel
BuildRequires:  unixODBC-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xorg-x11-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.1
BuildRequires:  pkgconfig(xkbcommon-x11) >= 0.4.1
BuildRequires:  fdupes
BuildArch:      noarch
Requires:       %{name}-html = %{version}
Requires:       %{name}-qch  = %{version}
# Replaced in Qt 5.9.1-rc
Provides:       libqt5-qtcharts-docs = %{version}
Obsoletes:      libqt5-qtcharts-docs < %{version}
Provides:       libqt5-qtdatavis3d-docs = %{version}
Obsoletes:      libqt5-qtdatavis3d-docs < %{version}

%description
Qt is a set of libraries for developing applications.

This package pulls in the API documentation in HTML and QCH format.

%package html
Summary:        Qt 5 API Documentation in HTML format
Group:          Documentation/HTML

%description html
This package contains the Qt API documentation in html format.

%package qch
Summary:        Qt 5 API Documentation in QCH format
Group:          Documentation/Other

%description qch
This package contains the Qt API Documentation in QCH format, which can be used by tools like KDevelop, Qt Assistant, Qt Creator, etc.

%package devel
Summary:        QDoc index files and doxygen tag files for Qt 5 API Documentation
Group:          Development/Tools/Doc Generators
Requires:       libqt5-qttools => %{version}
Requires:       doxygen

%description devel
This package contains the QDoc index files and the doxygen tag files to create cross links between the QCH documentation files. This package is normally not
required.

%prep
%setup -q -n %{tar_version}
%autopatch -p1

%build
# We need to link to some of the programs used as that the source assumes they were just build.
ln -s %{_bindir}/rcc-qt5 qtbase/bin/rcc
ln -s %{_bindir}/uic-qt5 qtbase/bin/uic
ln -s %{_bindir}/moc-qt5 qtbase/bin/moc
ln -s %{_libqt5_bindir} qttools/bin

# Create the Makefiles which are required.
# To-Do: Clean up of the options and with this also the BuildRequires.

# FIXME: you should use the %%configure macro
./configure \
	-verbose \
    -prefix %{_prefix} \
    -bindir %{_libqt5_bindir} \
	-docdir %{_libqt5_docdir} \
	-accessibility \
	-no-strip \
	-opensource \
    -confirm-license \
    -release \
    -nomake tests \
    -nomake examples

%make_jobs docs

%install
make INSTALL_ROOT=%{buildroot} install_docs
%fdupes %{buildroot}%{_libqt5_docdir}

%files
%license LICENSE.*

%files html
%license LICENSE.*
%{_libqt5_docdir}/*/
%exclude %{_libqt5_docdir}/*/*.index
%exclude %{_libqt5_docdir}/*/*.tags

%files qch
%license LICENSE.*
%{_libqt5_docdir}/*.qch

%files devel
%license LICENSE.*
%{_libqt5_docdir}/*/*.index
%{_libqt5_docdir}/*/*.tags

%changelog
