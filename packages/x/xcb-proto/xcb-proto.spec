#
# spec file for package xcb-proto
#
# Copyright (c) 2020 SUSE LLC
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


%define dirsuffix 1.14.1
%if 0%{?suse_version} >= 1500
%bcond_with python2
%else
%bcond_without python2
%endif
Name:           xcb-proto
Version:        7.6_%{dirsuffix}
Release:        0
Summary:        The X11 Protocol: X Protocol C Bindings
License:        X11
Group:          Development/Libraries/X11
URL:            http://xorg.freedesktop.org/
#Git-Web:	https://cgit.freedesktop.org/xcb/proto
Source:         http://xorg.freedesktop.org/archive/individual/proto/%{name}-%{dirsuffix}.tar.xz
BuildRequires:  autoconf >= 2.57
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-base
%else
BuildRequires:  python3-base
%endif

%description
The XCB protocol headers for X11 development. xcb-proto provides the
XML-XCB protocol descriptions that libxcb uses to generate the majority of
its code and API.

%package devel
Summary:        The X11 Protocol: X Protocol C Bindings
Group:          Development/Libraries/X11
Provides:       xorg-x11-proto-devel = 7.6
Obsoletes:      xorg-x11-proto-devel <= 7.6
%if %{with python2}
Requires:       python2-xcb-proto-devel = %{version}
%else
Requires:       python3-xcb-proto-devel = %{version}
%endif

%description devel
The XCB protocol headers for X11 development. xcb-proto provides the
XML-XCB protocol descriptions that libxcb uses to generate the majority of
its code and API.

%package -n python2-xcb-proto-devel
Summary:        Python libraries mandatory for XML-XCB Development
Group:          Development/Libraries/X11
Provides:       python-xcb-proto-devel = %{version}-%{release}
Obsoletes:      python-xcb-proto-devel < %{version}-%{release}
Provides:       python-xcb-proto-devel = 7.6
Obsoletes:      python-xcb-proto-devel <= 7.6

%description -n python2-xcb-proto-devel
Language-independent Python libraries that used to parse an XML description
and create objects used by Python code generators in individual language
bindings.

%package -n python3-xcb-proto-devel
Summary:        Python libraries mandatory for XML-XCB Development
Group:          Development/Libraries/X11

%description -n python3-xcb-proto-devel
Language-independent Python libraries that used to parse an XML description
and create objects used by Python code generators in individual language
bindings.

%prep
%setup -q -n %{name}-%{dirsuffix}
%autopatch -p1

%build
autoreconf -fiv
%if %{with python2}
export PYTHON="python2"
%else
export PYTHON="python3"
%endif
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}/%{_prefix}

%files devel
%dir %{_datadir}/xcb
%doc %{_datadir}/xcb/*
%{_libdir}/pkgconfig/*.pc

%if %{with python2}
%files -n python2-xcb-proto-devel
%doc COPYING
%{python_sitelib}/xcbgen/
%else
%files -n python3-xcb-proto-devel
%license COPYING
%{python3_sitelib}/xcbgen/
%endif

%changelog
