#
# spec file for package python-lmiwbem
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


# doc generation segfaults :-/
%global with_doc 0

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           python-lmiwbem
Version:        0.7.2
Release:        1%{?dist}
Summary:        Python WBEM Client
License:        LGPL-2.0+
Group:          System/Management
Url:            https://github.com/phatina/python-lmiwbem
Source0:        https://github.com/phatina/python-lmiwbem/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE, SUSE packages internal Pegasus include files in separate directory, kkaempf@suse.de
Patch1:         include-pegasus-internal.patch
# PATCH-FIX-OPENSUSE, build service reports (some) 32bit systems as 'athlon'
Patch2:         accept-athlon.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%if 0%{?suse_version}
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python-devel
%else
BuildRequires:  python2-devel
%endif
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_python-devel
%else
BuildRequires:  boost-devel > 1.50.0
%endif
BuildRequires:  openslp-devel
BuildRequires:  tog-pegasus-devel >= 2.12.0
BuildRequires:  tog-pegasus-libs >= 2.12.0
%if %{with_doc}
BuildRequires:  python-sphinx
BuildRequires:  python-sphinx_rtd_theme
BuildRequires:  python-sphinxcontrib-napoleon
%endif
BuildRequires:  libwsman_clientpp-devel

Provides:       lmiwbem = %{version}-%{release}
Obsoletes:      lmiwbem < 0.6.1-1

%description
%{name} is a Python library, which performs CIM operations using CIM-XML
protocol. The library tries to mimic PyWBEM.

%if %{with_doc}
%package doc
Summary:        Documentation for %{name}
Group:          Documentation

%description doc
%{summary}
%endif

%prep
%setup -q -n %{name}-%{version}
%if 0%{?suse_version}
%patch1 -p1
%patch2 -p1
%endif

%build
autoreconf -fi
%configure \
%if 0%{?suse_version}
--with-default-trust-store=/etc/pki/trust/anchors \
%endif
--with-wsman=yes \
%if %{with_doc}
--with-doc=yes
%endif

CPPFLAGS="-I /usr/include/Pegasus-internal" make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' | xargs rm -f

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{python_sitearch}/lmiwbem/

%if %{with_doc}
%files doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/html
%endif

%changelog
