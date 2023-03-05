#
# spec file for package xbitmaps
#
# Copyright (c) 2023 SUSE LLC
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


Name:           xbitmaps
Version:        1.1.3
Release:        0
Summary:        Base X bitmaps
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/releases/individual/data/
Source:         http://xorg.freedesktop.org/releases/individual/data/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildArch:      noarch

%description
This package contains the base X bitmaps, which are used in many
legacy X clients.

%package devel
Summary:        Development files for the base X bitmaps
Group:          Development/Libraries/C and C++

%description devel
This package contains the base X bitmaps, which are used in many
legacy X clients.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%{_includedir}/X11/bitmaps

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/xbitmaps.pc

%changelog
