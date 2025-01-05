#
# spec file for package composefs
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


%define         sover 1
Name:           composefs
Version:        1.0.8
Release:        0
Summary:        The reliability of disk images, the flexibility of files
License:        Apache-2.0 OR GPL-2.0-or-later
URL:            https://github.com/containers/composefs
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go-md2man
BuildRequires:  meson
BuildRequires:  pkgconfig(fuse3) >= 3.10.0
BuildRequires:  pkgconfig(openssl) >= 3.0.0

%description
Tools to handle creating and mounting composefs images. The composefs
project combines several underlying Linux features to provide a very
flexible mechanism to support read-only mountable filesystem trees,
stacking on top of an underlying "lower" Linux filesystem.

%package -n     lib%{name}%{sover}
Summary:        Libraries for %{name}

%description -n lib%{name}%{sover}
Library files for %{name}.

%package        devel
Summary:        Devel files for %{name}
Requires:       %{name} = %{version}
Requires:       lib%{name}%{sover} = %{version}

%description devel
Devel files for %{name}.

%prep
%autosetup

%build
%meson \
  -Dfuse=enabled \
  -Dman=enabled
%meson_build

%install
%meson_install
rm -rf %{buildroot}%{_libdir}/libcomposefs.{a,la}

%check
%meson_test

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%license COPYING COPYING.GPL-2.0-only COPYING.GPL-2.0-or-later COPYING.LGPL-2.1-or-later LICENSE.Apache-2.0
%doc README.md
%{_bindir}/mk%{name}
%{_bindir}/%{name}-info
%{_sbindir}/mount.%{name}
%{_mandir}/man?/%{name}-{info,dump}.?%{?ext_man}
%{_mandir}/man?/mk%{name}.?%{?ext_man}
%{_mandir}/man?/mount.%{name}.?%{?ext_man}

%files devel
%{_includedir}/lib%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%changelog
