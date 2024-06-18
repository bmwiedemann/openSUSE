#
# spec file for package editorconfig-core-c
#
# Copyright (c) 2023 SUSE LLC
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


Name:           editorconfig-core-c
Version:        0.12.9
Release:        0
Summary:        EditorConfig core library written in C
License:        BSD-2-Clause AND BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://editorconfig.org/
Source:         https://github.com/editorconfig/editorconfig-core-c/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake >= 3.16.3
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcre2-8)

%description
EditorConfig makes it easy to maintain the correct coding style when switching
between different text editors and between different projects. The EditorConfig
project maintains a file format and plugins for various text editors which allow
this file format to be read and used by those editors. For information on the
file format and supported text editors, see the EditorConfig website.

%package -n editorconfig
Summary:        Commandline utilities for EditorConfig
Group:          Productivity/Text/Utilities

%description -n editorconfig
EditorConfig makes it easy to maintain the correct coding style when switching
between different text editors and between different projects. The EditorConfig
project maintains a file format and plugins for various text editors which allow
this file format to be read and used by those editors. For information on the
file format and supported text editors, see the EditorConfig website.

This package contains command line utilities.

%package -n libeditorconfig0
Summary:        EditorConfig core library written in C
Group:          System/Libraries

%description -n libeditorconfig0

EditorConfig makes it easy to maintain the correct coding style when switching
between different text editors and between different projects. The EditorConfig
project maintains a file format and plugins for various text editors which allow
this file format to be read and used by those editors. For information on the
file format and supported text editors, see the EditorConfig website.

This package contains shared library.

%package -n libeditorconfig-devel
Summary:        Development files for EditorConfig core library written in C
Group:          Development/Libraries/C and C++
Requires:       libeditorconfig0 = %{version}

%description -n libeditorconfig-devel

EditorConfig makes it easy to maintain the correct coding style when switching
between different text editors and between different projects. The EditorConfig
project maintains a file format and plugins for various text editors which allow
this file format to be read and used by those editors. For information on the
file format and supported text editors, see the EditorConfig website.

This package contains files for developing and building with %{name}

%prep
%autosetup -p1

%build
%cmake \
	-DLIB_SUFFIX=%{_lib} \
	%{nil}
%make_build

%install
%cmake_install
find %{buildroot}/%{_libdir} -type f -name "*.a" -print -delete

%check
%ctest

%ldconfig_scriptlets -n libeditorconfig0

%files -n editorconfig
%license LICENSE
%{_bindir}/editorconfig*
%{_mandir}/man1/editorconfig*
%{_mandir}/man5/editorconfig*

%files -n libeditorconfig0
%license LICENSE
%{_libdir}/libeditorconfig.so.0*

%files -n libeditorconfig-devel
%license LICENSE
%doc CONTRIBUTORS README.md
%{_includedir}/editorconfig
%{_libdir}/libeditorconfig.so
%{_mandir}/man3/editorconfig*
%{_libdir}/pkgconfig/editorconfig.pc
%{_libdir}/cmake/EditorConfig

%changelog
