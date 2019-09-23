#
# spec file for package prelude-correlator
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           prelude-correlator
Version:        4.0.0
Release:        0
Summary:        Real time correlator of events received by Prelude Manager
License:        GPL-2.0+
Group:          Productivity/Networking/Security
Url:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}-tmpfiles.conf
# Backport ez_setup to be compatible with old (Open)SuSE
Patch0:         prelude-correlator-ez_setup.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libprelude-devel
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  systemd
BuildRequires:  pkgconfig(glib-2.0)
Requires:       prelude-correlator-core >= %{version}
Requires:       python-libprelude
Requires:       python-netaddr
BuildArch:      noarch
%{?systemd_requires}

%python_subpackages

%description
Prelude-Correlator allows conducting multi-stream correlations
thanks to a powerful programming language for writing correlation
rules. With any type of alert able to be correlated, event
analysis becomes simpler, quicker and more incisive. This
correlation alert then appears within the Prewikka interface
and indicates the potential target information via the set of
correlation rules.

%package -n %{name}-core
Summary:        Prelude Correlator core files
Group:          Productivity/Networking/Security

%description -n %{name}-core
Core files for Prelude Correlator.

%prep
%setup -q
%patch0

%build

%install
%{python_expand $python setup.py install -O1 --force --root %{buildroot}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-%{$python_bin_suffix}
%fdupes %{buildroot}%{$python_sitelib}/preludecorrelator
}
ln -s ./%{name}-%{python3_bin_suffix} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

rm -rf %{buildroot}/%{_localstatedir}/run/%{name}
install -D -m 444 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%pre -n %{name}-core
%service_add_pre %{name}.service

%post -n %{name}-core
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.service

%preun -n %{name}-core
%service_del_preun %{name}.service

%postun -n %{name}-core
%service_del_postun %{name}.service

%files -n %{name}-core
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS HACKING.README
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

%files %{python_files}
%{python_sitelib}/preludecorrelator/
%{python_sitelib}/prelude_correlator*.egg-info
%{_bindir}/prelude-correlator-%{python_bin_suffix}
%python3_only %{_bindir}/prelude-correlator

%changelog
