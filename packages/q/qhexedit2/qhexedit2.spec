#
# spec file for package qhexedit2
#
# Copyright (c) 2025 SUSE LLC
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


%define _libver 4
Name:           qhexedit2
Version:        0.8.10
Release:        0
Summary:        Qt-based hex editor
License:        LGPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/Simsys/qhexedit2
Source0:        https://github.com/Simsys/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        qhexedit.desktop
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt6Widgets)

%description
QHexEdit is a hex editor widget written in C++ for the Qt framework.
It is a simple editor for binary data, just like QPlainTextEdit is for text
data.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libqhexedit%{_libver} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation and examples for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation and examples for %{name}.

%package -n libqhexedit%{_libver}
Summary:        Qt5 %{name} library
Group:          System/Libraries

%description -n libqhexedit%{_libver}
Qt5 library for %{name}.

%prep
%autosetup -p1

%build
mkdir build-lib
pushd build-lib
qmake6 QMAKE_CXXFLAGS="%{optflags}" ../src/qhexedit.pro
make %{?_smp_mflags}
popd

# Build application
mkdir build-example
pushd build-example
qmake6 QMAKE_CXXFLAGS="%{optflags}" ../example/qhexedit.pro
make %{?_smp_mflags}
popd

%install
# Library and headers
install -d %{buildroot}%{_includedir}/%{name}
cp -a src/*.h %{buildroot}%{_includedir}/%{name}
install -d %{buildroot}%{_libdir}
chmod 0755 build-lib/*.so.*.*
cp -a build-lib/*.so* %{buildroot}%{_libdir}

# pkg-config files
install -d %{buildroot}%{_libdir}/pkgconfig/

cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc <<EOF
libdir=%{_libdir}
includedir=%{_includedir}/%{name}

Name:           %{name}
Version:        %{version}
Description: %{summary}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqhexedit
EOF

# Application
install -Dpm 0755 build-example/qhexedit %{buildroot}%{_bindir}/qhexedit
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/qhexedit.desktop

# Fix docs
%fdupes -s doc/html

# Install icon
install -d %{buildroot}%{_datadir}/pixmaps
convert -strip doc/html/qhexedit.png -resize 128x128! %{buildroot}%{_datadir}/pixmaps/qhexedit.png

%post
%desktop_database_post

%postun
%desktop_database_postun

%post -n libqhexedit%{_libver} -p /sbin/ldconfig

%postun -n libqhexedit%{_libver} -p /sbin/ldconfig

%files
%license src/license.txt
%doc readme.md
%{_bindir}/qhexedit
%{_datadir}/applications/qhexedit.desktop
%{_datadir}/pixmaps/qhexedit.png

%files doc
%license src/license.txt
%doc doc/html readme.md

%files -n libqhexedit%{_libver}
%license src/license.txt
%doc doc/release.txt
%{_libdir}/libqhexedit.so.%{_libver}*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libqhexedit.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
