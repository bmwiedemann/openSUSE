#
# spec file for package prewikka
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           prewikka
Version:        4.0.0
Release:        0
Summary:        Graphical front-end analysis console for the Prelude Framework
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Frontends
Url:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Patch0:         prewikka-fix_python3.patch
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module lesscpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
Requires:       prewikka-core >= %{version}
Requires:       prewikka-lang >= %{version}
Requires:       python-Babel
Requires:       python-Mako
Requires:       python-PyYAML
Requires:       python-Werkzeug
Requires:       python-libprelude
Requires:       python-libpreludedb
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       xorg-x11-fonts
BuildArch:      noarch

%python_subpackages

%description
Prewikka is the graphical front-end analysis console for the Prelude
Universal SIM. Prewikka provides alert aggregation and sensor and
hearbeat views, and has user management and configurable filters, as
well as access to external tools such as whois and traceroute.

%package core
Summary:        Prewikka core files
Group:          Productivity/Networking/Web/Frontends

%description core
Core files for prewikka.

%package lang
Summary:        Prewikka lang files
Group:          Productivity/Networking/Web/Frontends

%description lang
Lang files for prewikka.

%prep
%setup -q
%patch0

%build

%install
install -d -m 0755 %{buildroot}%{_sbindir}

%{python_expand $python setup.py install -O1 --force --root %{buildroot}
mv %{buildroot}%{_bindir}/%{name}-httpd %{buildroot}%{_sbindir}/%{name}-httpd-%{$python_bin_suffix}
%fdupes %{buildroot}%{$python_sitelib}/prewikka
}

ln -s ./%{name}-httpd-%{python3_bin_suffix} %{buildroot}%{_sbindir}/%{name}-httpd

install -d -m 0755 %{buildroot}%{_datadir}/locale
cp -r %{buildroot}%{python2_sitelib}/%{name}/locale/* %{buildroot}%{_datadir}/locale/
rm -rf %{buildroot}%{python2_sitelib}/%{name}/locale
rm -rf %{buildroot}%{python3_sitelib}/%{name}/locale
ln -s %{_datadir}/locale %{buildroot}%{python2_sitelib}/%{name}/locale
ln -s %{_datadir}/locale %{buildroot}%{python3_sitelib}/%{name}/locale

rm %{buildroot}%{_sysconfdir}/%{name}/*-dist

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}

%find_lang %{name}

%files -n %{name}-core
%defattr(-, root, root, -)
%attr(0750, -,-) %dir %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640, -,-) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %attr(0640, -,-) %{_sysconfdir}/%{name}/menu.yml
%{_datadir}/%{name}
%doc COPYING* AUTHORS README NEWS HACKING.README

%files -n %{name}-lang -f %{name}.lang

%files %python_files
%{python_sitelib}/prewikka/
%{python_sitelib}/prewikka*.egg-info
%{_sbindir}/prewikka-httpd-%{python_bin_suffix}
%python3_only %{_sbindir}/prewikka-httpd

%changelog
