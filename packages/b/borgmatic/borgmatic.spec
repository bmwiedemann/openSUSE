#
# spec file for package borgmatic
#
# Copyright (c) 2025 SUSE LLC
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


%define pythons python3
Name:           borgmatic
Version:        1.9.5
Release:        0
Summary:        Automation tool for borgbackup
License:        GPL-3.0-only
URL:            https://torsion.org/borgmatic
Source:         https://github.com/borgmatic-collective/borgmatic/archive/%{version}.tar.gz#/borgmatic-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module apprise}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module flexmock}
BuildRequires:  %{python_module jsonschema >= 3.2.0}
BuildRequires:  %{python_module mccabe}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pyflakes}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  borgbackup
BuildRequires:  fdupes
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
Requires:       %{pythons}-jsonschema >= 3.2.0
Requires:       %{pythons}-packaging
Requires:       %{pythons}-requests
Requires:       %{pythons}-ruamel.yaml > 0.15.0
Requires:       borgbackup
Suggests:       %{pythons}-apprise
BuildArch:      noarch
ExcludeArch:    %{ix86}
%python_subpackages

%description
borgmatic is a Python wrapper script for the Borg backup software
that initiates a backup, prunes any old backups according to a
retention policy, and validates backups for consistency. The script
supports specifying your settings in a declarative configuration file
rather than having to put them all on the command-line, and handles
common errors.

%prep
%autosetup -p1

%if 0%{?suse_version} <= 1500
sed -i -e "s/^LogRateLimitIntervalSec=/#LogRateLimitIntervalSec=/" sample/systemd/borgmatic.service
%endif

# Make sample files use the borgmatic command on /usr/bin, not /usr/local/bin
perl -pi -e "s,PATH=\\$PATH:%{_prefix}/local/bin /root/.local/bin/borgmatic,%{_bindir}/borgmatic," sample/cron/borgmatic
perl -pi -e "s,/root/.local/bin/borgmatic,%{_bindir}/borgmatic," sample/systemd/borgmatic.service
perl -pi -e "s,/root/.local/bin/borgmatic,%{_bindir}/borgmatic," sample/systemd/borgmatic-user.service
perl -pi -e "s,=sleep,=%{_bindir}/sleep," sample/systemd/borgmatic.service
perl -pi -e "s,=sleep,=%{_bindir}/sleep," sample/systemd/borgmatic-user.service
perl -pi -e "s,=systemd-inhibit,=%{_bindir}/systemd-inhibit," sample/systemd/borgmatic.service
perl -pi -e "s/ruamel.yaml>0.15.0,<0.17.0/ruamel.yaml/" setup.py
perl -pi -e "s/packages=find_packages\(\)/packages=find_packages(exclude=('tests*',))/" setup.py

%build
%pyproject_wheel
# Create the manpage
pandoc -s -f markdown -t man README.md -o borgmatic.1

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -d %{buildroot}%{_sysconfdir}/borgmatic
install -d %{buildroot}%{_sysconfdir}/borgmatic.d
install -d %{buildroot}%{_docdir}/%{name}/sample/cron
install -m 0644 sample/cron/borgmatic %{buildroot}%{_docdir}/%{name}/sample/cron/
install -d %{buildroot}%{_docdir}/%{name}/sample/systemd
install -m 0644 sample/systemd/borgmatic* %{buildroot}%{_docdir}/%{name}/sample/systemd/
install -d %{buildroot}%{_unitdir}/
install -m 0644 sample/systemd/borgmatic.* %{buildroot}%{_unitdir}/

install -D -m 0644 borgmatic.1 %{buildroot}%{_mandir}/man1/borgmatic.1
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcborgmatic

%check
# testing the build is a little awkward, since the original testsuite is based on tox and
# tox tries to create a virtual environment, that we need tight control on in order to get
# it to behave in our build system (offline mode, use site packages). OTOH, without the
# venv, we face problems with setuptools (borg uses pkg_resources to locate the installed
# package), while py.test relies on the usual module handling. <hpj@urpla.net>
export LANG=en_US.UTF-8
%python_exec -m venv --system-site-packages --without-pip borgmatic-env
source borgmatic-env/bin/activate
%python_exec -m pip install --disable-pip-version-check --no-compile --ignore-installed --no-deps --no-index --find-links ./build borgmatic==1.9.5
PYTHONPATH=$(pwd):%{buildroot} py.test -v --pyargs borgmatic tests

%post
%service_add_post borgmatic.service
if [ "$1" = 1 -a ! -f "%{_sysconfdir}/borgmatic/config.yaml" ]; then
    %{_bindir}/borgmatic config generate
fi

%pre
%service_add_pre borgmatic.service

%preun
%service_del_preun borgmatic.service

%postun
%service_del_postun borgmatic.service

%files
%doc AUTHORS NEWS README.md
%license LICENSE
%config %ghost %attr(0600,root,root) %{_sysconfdir}/borgmatic/config.yaml
%dir %{_sysconfdir}/borgmatic
%dir %{_sysconfdir}/borgmatic.d
%dir %{_docdir}/%{name}/sample
%{python_sitelib}/borgmatic/
%{python_sitelib}/borgmatic-%{version}*info
%{_unitdir}/borgmatic.service
%{_unitdir}/borgmatic.timer
%{_bindir}/borgmatic
%{_sbindir}/rcborgmatic
%{_bindir}/generate-borgmatic-config
%{_bindir}/validate-borgmatic-config
%{_mandir}/man1/borgmatic.1%{?ext_man}
%{_docdir}/%{name}/sample/cron/
%{_docdir}/%{name}/sample/systemd/

%changelog
