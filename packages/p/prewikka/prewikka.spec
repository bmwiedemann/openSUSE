#
# spec file for package prewikka
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


Name:           prewikka
Version:        5.2.0
Release:        0
Summary:        Graphical front-end analysis console for the Prelude Framework
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Frontends
URL:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://www.prelude-siem.org/attachments/download/233/RPM-GPG-KEY-Prelude-IDS#/%{name}.keyring
Patch0:         prewikka-fix_shebang.patch
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  python3-Babel
BuildRequires:  python3-devel
BuildRequires:  python3-lesscpy
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
Requires:       prewikka-lang >= %{version}
Requires:       python3-Babel
Requires:       python3-Mako
Requires:       python3-PyYAML
Requires:       python3-Werkzeug
Requires:       python3-croniter
Requires:       python3-gevent
Requires:       python3-lark-parser
Requires:       python3-libprelude
Requires:       python3-libpreludedb
Requires:       python3-python-dateutil
Requires:       python3-pytz
Requires:       python3-voluptuous
Requires:       xorg-x11-fonts
Obsoletes:      prewikka-core < %{version}-%{release}
Provides:       prewikka-core = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Prewikka is the graphical front-end analysis console for the Prelude
Universal SIM. Prewikka provides alert aggregation and sensor and
hearbeat views, and has user management and configurable filters, as
well as access to external tools such as whois and traceroute.

%package lang
# FIXME: consider using %%lang_package macro
Summary:        Prewikka lang files
Group:          Productivity/Networking/Web/Frontends

%description lang
Lang files for prewikka.

%prep
%setup -q
%patch0

%build

%install
python3 setup.py install -O1 --force --root %{buildroot}
%fdupes %{buildroot}%{$python3_sitelib}/prewikka

install -d -m 0755 %{buildroot}%{_datadir}/locale
cp -r %{buildroot}%{python3_sitelib}/%{name}/locale/* %{buildroot}%{_datadir}/locale/
rm -rf %{buildroot}%{python3_sitelib}/%{name}/locale
ln -s %{_datadir}/locale %{buildroot}%{python3_sitelib}/%{name}/locale

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}

find %{buildroot} -name __pycache__ -exec rm -rfv {} +

%find_lang %{name}

%files -n python3-%{name}
%license COPYING*
%doc AUTHORS README NEWS HACKING.README
%attr(0750, -,-) %dir %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640, -,-) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %attr(0640, -,-) %{_sysconfdir}/%{name}/menu.yml
%attr(0750, -,-) %dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %attr(0640, -,-) %{_sysconfdir}/%{name}/conf.d/*.conf
%{_datadir}/%{name}
%{python3_sitelib}/prewikka/
%{python3_sitelib}/prewikka*.egg-info
%{_bindir}/prewikka-httpd
%{_bindir}/prewikka-cli
%{_bindir}/prewikka-crontab

%files -n %{name}-lang -f %{name}.lang

%changelog
