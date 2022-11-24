#
# spec file for package apache2-mod_wsgi
#
# Copyright (c) 2022 SUSE LLC
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


%define modname mod_wsgi
%if 0%{?suse_version}
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
%else
%define apache_apxs %{bindir}/apxs
%define apache_sysconfdir %(%{apache_apxs} -q PREFIX)
BuildRequires:  httpd
BuildRequires:  httpd-devel
%endif
Name:           apache2-mod_wsgi
Version:        4.9.4
Release:        0
Summary:        A WSGI interface for Python3 web applications in Apache
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://github.com/GrahamDumpleton/mod_wsgi
Source:         https://github.com/GrahamDumpleton/mod_wsgi/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  apache-rex
%apache_rex_deps
BuildRequires:  python3-devel
%if 0%{?suse_version} >= 1500 || 0%{?fedora} || 0%{?rhel}
BuildRequires:  python3-setuptools
%endif
Obsoletes:      apache2-mod_wsgi-python3 < %{version}-%{release}
Provides:       %{modname} = %{version}-%{release}
Provides:       apache2-mod_wsgi-python3 = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2
%else
Requires:       httpd
%endif

%description
The mod_wsgi adapter is an Apacheache module that provides a WSGI compliant
interface for hosting Python based web applications within Apache. The
adapter is written completely in C code against the Apache C runtime and
for hosting WSGI applications within Apache has a lower overhead than using
existing WSGI adapters for mod_python or CGI.

%prep
%autosetup -n %{modname}-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --with-apxs="%{apache_apxs}" \
    --with-python="python3"
make %{?_smp_mflags}
%if 0%{?suse_version} >= 1500 || 0%{?fedora} || 0%{?rhel}
%py3_build
%endif

%install
make install DESTDIR=%{buildroot} LIBEXECDIR=%{apache_libexecdir}
%if 0%{?suse_version} >= 1500 || 0%{?fedora} || 0%{?rhel}
%py3_install
%endif

%check
%apache_rex_check -m ./src/server/.libs mod_wsgi-basic

%post
%if 0%{?suse_version}
if ! %{_sbindir}/a2enmod -q wsgi; then
  %{_sbindir}/a2enmod wsgi
fi
%endif

%postun
%if 0%{?suse_version}
if [ "$1" = "0" ]; then
  if a2enmod -q wsgi; then
    %{_sbindir}/a2enmod -d wsgi
  fi
fi
%endif

%files
%defattr(-,root,root)
%doc LICENSE README.rst docs/release-notes
%dir %{apache_libexecdir}
%{apache_libexecdir}/%{modname}.so
%if 0%{?suse_version} >= 1500 || 0%{?fedora} || 0%{?rhel}
%{python3_sitearch}/mod_wsgi-*.egg-info
%{python3_sitearch}/mod_wsgi
%{_bindir}/mod_wsgi-express
%endif

%changelog
