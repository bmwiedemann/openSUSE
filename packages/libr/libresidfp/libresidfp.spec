#
# spec file for package libresidfp
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define sover 0
Name:           libresidfp
Version:        1.1.0
Release:        0
Summary:        Cycle exact SID emulation
License:        GPL-2.0-or-later
URL:            https://github.com/libsidplayfp/libresidfp
Source0:        https://github.com/libsidplayfp/libresidfp/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
Cycle exact SID emulation.

This project is meant to replicate the SID as faithfully as possible
while keeping good performance for realtime use. It is not intended
to expose the chip internal state or adding fancy effects. Both the
6581 and the 8580 models are emulated.

%package -n lib%{name}%{sover}
Summary:        Shared library files for libresidfp

%description -n lib%{name}%{sover}
Cycle exact SID emulation.

This project is meant to replicate the SID as faithfully as possible
while keeping good performance for realtime use. It is not intended
to expose the chip internal state or adding fancy effects. Both the
6581 and the 8580 models are emulated.
This package provides the shared library files for libresidfp.

%package devel
Summary:        Development files for libresidfp
Requires:       lib%{name}%{sover} = %{version}

%description devel
Development files for libresidfp.

%prep
%autosetup -p1

%build
%configure --disable-static --enable-lto=yes
%make_build

%check
%make_build check

%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%license COPYING
%doc README.md NEWS.md
%{_libdir}/%{name}.so.%{sover}*

%files devel
%dir %{_includedir}/residfp
%{_includedir}/residfp/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
