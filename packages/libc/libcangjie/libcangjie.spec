#
# spec file for package libcangjie
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global im_name cangjie
%global sover 2
Name:           libcangjie
Version:        1.3
Release:        0
Summary:        A C library implementing the Cangjie input method
License:        LGPL-3.0+
Group:          System/I18n/Chinese
Url:            http://cangjians.github.io/projects/%{name}
Source:         https://github.com/Cangjians/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  sqlite-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} is a C library implementing the Cangjie input method,
which is mainly used on Traditional Chinese inputing.

%package -n %{name}%{sover}
Summary:        A C library implementing the Cangjie input method
Group:          System/Libraries

%description -n %{name}%{sover}
%{name} is a C library implementing the Cangjie input method,
which is mainly used on Traditional Chinese inputing.

This package provides runtime library for %{name}.

%package data
Summary:        Data files for the %{name} IME
Group:          System/I18n/Chinese
Requires:       %{name}%{sover} = %{version}
BuildArch:      noarch

%description data
%{name} is a C library implementing the Cangjie input method,
which is mainly used on Traditional Chinese inputing.

libcangjie-data contains the input mapping table to switch en_US
keyboard codes to Traditional Chinese characters, and it is designed
to be compiled into the final input engine "ibus-cangjie".

%package devel
Summary:        Development files for the %{name} IME
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       %{name}-tools = %{version}

%description devel
%{name} is a C library implementing the Cangjie input method,
which is mainly used on Traditional Chinese inputing.

This package provides development files for %{name}.

%package tools
Summary:        Tools for the %{name} IME
Group:          System/I18n/Chinese
Requires:       %{name}%{sover} = %{version}

%description tools
%{name} is a C library implementing the Cangjie input method, which
is mainly used on Traditional Chinese inputing.

This package provides tools for %{name}.

%prep
%setup -q

%build
%configure --datadir=%{_datadir}/libcangjie%{sover}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir}/ -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%doc AUTHORS README.md COPYING
%{_libdir}/%{name}.so.*

%files data
%defattr(-,root,root)
%{_datadir}/%{name}%{sover}/

%files devel
%defattr(-,root,root)
%{_includedir}/%{im_name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{im_name}.pc

%files tools
%defattr(-,root,root)
%{_bindir}/%{name}_*

%changelog
