#
# spec file for package libaiff
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


%define sover 2
Name:           libaiff
Version:        6.0
Release:        0
Summary:        Open-source implementation of the AIFF format
License:        MIT
URL:            https://github.com/mtszb/libaiff
Source:         https://github.com/mtszb/libaiff/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
ExcludeArch: %ix86

%description
LibAiff is a library with support for reading and writing Audio Interchange
File Format (AIFF) files.

%package -n %{name}%{sover}
Summary:        Open-source implementation of the AIFF format

%description -n %{name}%{sover}
LibAiff is a library with support for reading and writing Audio Interchange
File Format (AIFF) files.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description devel
LibAiff is a library with support for reading and writing Audio Interchange
File Format (AIFF) files.

This package contains files required for development with %{name}.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSE
%{_libdir}/libaiff.so.%{sover}
%{_libdir}/libaiff.so.%{sover}.*

%files devel
%license LICENSE
%doc README MANUAL.html
%{_includedir}/libaiff
%{_libdir}/libaiff.so

%changelog
