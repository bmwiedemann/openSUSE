#
# spec file for package docparser
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2022 Hillwood Yang <hillwood@opensuse.org>
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


%define libver  1

Name:           docparser
Version:        1.0.1
Release:        0
Summary:        A document parser library
License:        GPL-3.0+
Group:          Productivity/Publishing/HTML/Tools
Url:            https://github.com/linuxdeepin/docparser
Source0:        https://github.com/linuxdeepin/docparser/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  dtkcommon
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  libqt5-qtbase-common-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
docparser is a document parser library.It is ported from document2html.

%package -n lib%{name}%{libver}
Summary:        A document parser library
Group:          System/Libraries

%description -n lib%{name}%{libver}
docparser is a document parser library.It is ported from document2html.

%package devel
Summary:        Development tools for docparser
Group:          Development/Libraries/Other
Requires:       lib%{name}%{libver} = %{version}

%description devel
The docparser-devel package contains the header files and developer docs for
docparser.

%prep
%autosetup -p1

%build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}

%install
%qmake5_install

%post -n lib%{name}%{libver} -p /sbin/ldconfig
%postun -n lib%{name}%{libver} -p /sbin/ldconfig

%files -n lib%{name}%{libver}
%{_libdir}/lib%{name}.so.*

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog

