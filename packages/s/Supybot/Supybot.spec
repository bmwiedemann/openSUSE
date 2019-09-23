#
# spec file for package Supybot
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           Supybot
Summary:        IRC Bot
License:        BSD-3-Clause AND GPL-2.0-or-later AND Python-2.0
Group:          Productivity/Networking/IRC
Version:        0.83.4.1
Release:        0
URL:            https://github.com/Supybot/Supybot
Requires:       python-twisted
Recommends:     python-sqlite2
BuildRequires:  fdupes
BuildRequires:  python-devel
Source:         %{name}-%{version}.tar.bz2
%define plugins_version 20060723
Source1:        %{name}-plugins-%{plugins_version}.tar.bz2
Source2:        %{name}.sysconfig
Source3:        %{name}.init
Source4:        %{name}.service
Source10:       Supybot-rpmlintrc
Patch1:         Supybot-0.83.4.1-popen_deprecated.patch
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}
%{py_requires}
%{!?python_sitelib:  %global python_sitelib  %(%__python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%__python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%description
Supybot is a robust, user and programmer friendly IRC bot written in
Python. It aims to be an adequate replacement for most existing IRC
bots. It includes a very flexible and powerful ACL system for
controlling access to commands, as well as more than 50 builtin plugins
providing around 400 actual commands.


%prep
%setup -q -b 1
%patch1 -p0
cp -a ../%{name}-plugins-%{plugins_version}/* plugins/

%build
export CFLAGS=$RPM_OPT_FLAGS
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot} --record-rpm=INSTALLED_FILES
install -d %{buildroot}/%{_mandir}/man1
install -m 644 docs/man/*.1 %{buildroot}/%{_mandir}/man1
# fix non executable scripts
chmod +x %{buildroot}/%{python_sitelib}/supybot/plugins/RSS/local/feedparser.py
chmod +x %{buildroot}/%{python_sitelib}/supybot/plugins/Supybot/plugin.py
chmod +x %{buildroot}/%{python_sitelib}/supybot/plugins/ExternalNotice/supybot-external-notice.py
# install init and sysconfig script
install -Dm644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.supybot
install -d %{buildroot}/%{_datadir}/%{name}/scripts
install -Dm755 %{SOURCE3} %{buildroot}/%{_datadir}/%{name}/scripts/supybot
install -d %{buildroot}/%{_unitdir}
install -Dm644 %{SOURCE4} %{buildroot}/%{_unitdir}/supybot.service
mkdir -p %{buildroot}/%{_sbindir}
ln -s service %{buildroot}/%{_sbindir}/rcsupybot
%fdupes %{buildroot}

%pre
%service_add_pre supybot.service

%post
%service_add_post supybot.service

%preun
%service_del_preun supybot.service

%postun
%service_del_postun supybot.service

%files -f INSTALLED_FILES
%defattr(-, root, root)
%doc ACKS ChangeLog LICENSE README RELNOTES docs/GETTING_STARTED
%doc %{_mandir}/man1/*.gz
%{_fillupdir}/sysconfig.supybot
%{_datadir}/%{name}
%{_unitdir}/supybot.service
%{_sbindir}/rcsupybot

%changelog
