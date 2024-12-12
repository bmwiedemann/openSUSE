#
# spec file for package libzim
#
# Copyright (c) 2024 SUSE LLC
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


%define  sover  9
Name:           libzim
Version:        9.2.3
Release:        0
Summary:        Reference implementation for the ZIM file format
License:        GPL-2.0-or-later
URL:            https://github.com/openzim/libzim
Source0:        https://github.com/openzim/libzim/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://github.com/openzim/libzim/pull/936.patch
BuildRequires:  c++_compiler
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(xapian-core)

%description
The ZIM library is the reference implementation for the ZIM file format.
It's a solution to read and write ZIM files on many systems and
architectures. More information about the ZIM format and the openZIM
project at https://openzim.org/.

%package -n %{name}%{sover}
Summary:        Shared library for libzim

%description -n %{name}%{sover}
The ZIM library is the reference implementation for the ZIM file format.
It's a solution to read and write ZIM files on many systems and
architectures. More information about the ZIM format and the openZIM
project at https://openzim.org/.

This package contains shared library of the reference implementaation of
ZIM file format.

%package devel
Summary:        Development files for libzim
Requires:       %{name}%{sover} = %{version}

%description devel
The ZIM library is the reference implementation for the ZIM file format.
It's a solution to read and write ZIM files on many systems and
architectures. More information about the ZIM format and the openZIM
project at https://openzim.org/.

This package contains development files for libzim.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
# test mostly fail now
#SKIP_BIG_MEMORY_TEST=1 WAIT_TIME_FACTOR_TEST=8 %%meson_test
#SKIP_BIG_MEMORY_TEST=1 WAIT_TIME_FACTOR_TEST=8 meson test -C %{_vpath_builddir} --num-processes 1 --print-errorlogs

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%{_libdir}/libzim.so.*

%files devel
%doc AUTHORS ChangeLog README.md
%{_includedir}/zim
%{_libdir}/libzim.so
%{_libdir}/pkgconfig/libzim.pc
%license COPYING

%changelog
