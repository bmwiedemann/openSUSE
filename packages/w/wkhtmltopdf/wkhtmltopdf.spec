#
# spec file for package wkhtmltopdf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   0
%define libname lib%{wk_name}%{sover}
%define wk_name wkhtmltox
Name:           wkhtmltopdf
Version:        0.12.4
Release:        0
Summary:        Convert HTML into PDF and various image formats
License:        LGPL-3.0-only
Group:          Productivity/Publishing/PDF
URL:            http://wkhtmltopdf.org
Source:         https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/%{version}/%{wk_name}-%{version}.tar.bz2
# This patch should not be used in the next release because
# it's already in upstream sources.
# Please test it without that patch next time.
Patch0:         wkhtmltopdf-0.12.4-unpatched-qt.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
Provides:       wkhtmltoimage

%description
wkhtmltopdf and wkhtmltoimage are command line tools to
render HTML into PDF and various image formats using the Qt Webkit rendering
engine. These run entirely "headless" and do not require a display or display
service.

%package -n %{libname}
Summary:        Convert HTML into PDF and various image formats
Group:          System/Libraries

%description -n %{libname}
wkhtmltopdf and wkhtmltoimage are command line tools to
render HTML into PDF and various image formats using the Qt Webkit rendering
engine.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
wkhtmltopdf and wkhtmltoimage are command line tools to
render HTML into PDF and various image formats using the Qt Webkit rendering
engine.

This package contains the headers for the wkhtmltopdf library.

%prep
%setup -q -n %{wk_name}-%{version}
%patch0

%build
%qmake5
%make_jobs

%install
%make_install INSTALL_ROOT=%{buildroot}/%{_prefix}
%if %{__isa_bits} ==64
mv %{buildroot}%{_libexecdir} %{buildroot}%{_libdir}
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc CHANGELOG-OLD CHANGELOG.md README.md
%license LICENSE
%{_bindir}/wkhtmltopdf
%{_bindir}/wkhtmltoimage
%{_mandir}/man1/wkhtmltopdf.1%{?ext_man}
%{_mandir}/man1/wkhtmltoimage.1%{?ext_man}

%files -n %{libname}
%license LICENSE
%{_libdir}/libwkhtmltox.so.%{sover}*

%files devel
%license LICENSE
%{_includedir}/wkhtmltox
%{_libdir}/libwkhtmltox.so

%changelog
