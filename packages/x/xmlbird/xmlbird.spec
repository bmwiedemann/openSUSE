#
# spec file for package xmlbird
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname libxmlbird
%define sover 1
Name:           xmlbird
Version:        1.2.10
Release:        0
Summary:        XML parser
License:        LGPL-3.0-or-later
Group:          Productivity/Publishing/XML
URL:            https://birdfont.org/xmlbird.php
Source0:        https://github.com/johanmattssonm/xmlbird/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)

%description
XML parser with support for Vala iterators.

%package -n     %{soname}%{sover}
Summary:        The XML-Parse library
Group:          System/Libraries

%description -n %{soname}%{sover}
XML parser with support for Vala iterators.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description    devel
XML parser with support for Vala iterators.

This package contains the pkgconfig, header files and libraries needed to
develop application that use %{name}.

%prep
%setup -q

%build
python3 configure \
    --cflags="%{optflags}" \
	  --prefix=%{_prefix} \
	  --libdir=%{_lib}
python3 build.py

%install
python3 install.py --dest=%{buildroot}

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/%{name}.vapi

%changelog
