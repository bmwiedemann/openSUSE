#
# spec file for package prelude-correlator
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


Name:           prelude-correlator
Version:        5.2.0
Release:        0
Summary:        Real time correlator of events received by Prelude Manager
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}-tmpfiles.conf
Source3:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz.sig
Source4:        https://www.prelude-siem.org/attachments/download/233/RPM-GPG-KEY-Prelude-IDS#/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(systemd)
Requires:       python3-%{name} >= %{version}
Obsoletes:      %{name}-core < %{version}-%{release}
Provides:       %{name}-core = %{version}-%{release}
BuildArch:      noarch
%{?systemd_requires}

%description
Prelude-Correlator allows conducting multi-stream correlations
thanks to a powerful programming language for writing correlation
rules. With any type of alert able to be correlated, event
analysis becomes simpler, quicker and more incisive. This
correlation alert then appears within the Prewikka interface
and indicates the potential target information via the set of
correlation rules.

%package -n python3-%{name}
Summary:        Prelude Correlator python3 files
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}
Requires:       python3-libprelude
Requires:       python3-netaddr

%description -n python3-%{name}
Python 3 files for Prelude Correlator.

%prep
%setup -q

%build

%install
python3 setup.py install -O1 --force --root %{buildroot}
%fdupes %{buildroot}/%{python3_sitelib}

mkdir -p %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

rm -rf %{buildroot}/%{_localstatedir}/run/%{name}
install -D -m 444 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

rm -rf %{buildroot}/%{python3_sitelib}/preludecorrelator/__pycache__

%pre
%service_add_pre %{name}.service

%post
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc AUTHORS NEWS HACKING.README
%dir %attr(0750,-,-) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,-,-) %{_sysconfdir}/%{name}/%{name}.conf
%dir %attr(0750,-,-) %{_sysconfdir}/%{name}/rules
%dir %attr(0750,-,-) %{_sysconfdir}/%{name}/rules/python
%config(noreplace) %attr(0640,-,-) %{_sysconfdir}/%{name}/rules/python/*.py
%dir %attr(0750,-,-) %{_sysconfdir}/%{name}/conf.d
%config %attr(0640,-,-) %{_sysconfdir}/%{name}/conf.d/README
%dir %{_var}/lib/%{name}
%{_var}/lib/%{name}/*
%{_sbindir}/rc%{name}
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%dir %ghost /run/%{name}
%{_unitdir}/%{name}.service

%files -n python3-%{name}
%license COPYING
%{python3_sitelib}/preludecorrelator/
%{python3_sitelib}/prelude_correlator*.egg-info
%{_bindir}/prelude-correlator

%changelog
