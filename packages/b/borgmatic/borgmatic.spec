#
# spec file for package borgmatic
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


Name:           borgmatic
Version:        1.7.5
Release:        0
Summary:        Automation tool for borgbackup
License:        GPL-3.0-only
Group:          Productivity/Archiving/Backup
URL:            https://torsion.org/borgmatic/
Source:         https://github.com/witten/borgmatic/archive/%{version}.tar.gz#/borgmatic-%{version}.tar.gz
Patch1:         skip-tests.patch
# testing requirements
BuildRequires:  borgbackup
# To create the manpage
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.7
BuildRequires:  python3-PyYAML
BuildRequires:  python3-appdirs
BuildRequires:  python3-atomicwrites
BuildRequires:  python3-attrs
BuildRequires:  python3-click
BuildRequires:  python3-colorama
BuildRequires:  python3-coverage
BuildRequires:  python3-docopt
BuildRequires:  python3-flake8
BuildRequires:  python3-flexmock
BuildRequires:  python3-jsonschema >= 3.2.0
BuildRequires:  python3-mccabe
BuildRequires:  python3-more-itertools
BuildRequires:  python3-pluggy
BuildRequires:  python3-py
BuildRequires:  python3-pycodestyle
BuildRequires:  python3-pyflakes
BuildRequires:  python3-pykwalify
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-requests
BuildRequires:  python3-ruamel.yaml
BuildRequires:  python3-setuptools
BuildRequires:  python3-toml
BuildRequires:  pkgconfig(libsystemd)
Requires:       borgbackup
Requires:       python3-colorama
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-pykwalify
Requires:       python3-requests
Requires:       python3-ruamel.yaml < 0.18.0
Requires:       python3-ruamel.yaml > 0.15.0
Requires:       python3-setuptools
ExcludeArch:    %ix86
BuildArch:      noarch

%description
borgmatic is a Python wrapper script for the Borg backup software
that initiates a backup, prunes any old backups according to a
retention policy, and validates backups for consistency. The script
supports specifying your settings in a declarative configuration file
rather than having to put them all on the command-line, and handles
common errors.

%prep
%setup -q
%patch1 -p1

sed -i -e "s/colorama>=0.4.1,<0.5/colorama>=0.3.9/" setup.py
%if 0%{?suse_version} <= 1500
sed -i -e "s/^LogRateLimitIntervalSec=/#LogRateLimitIntervalSec=/" sample/systemd/borgmatic.service
%endif

# Make sample files use the borgmatic command on /usr/bin, not /usr/local/bin
perl -pi -e "s,PATH=\\$PATH:/usr/local/bin /root/.local/bin/borgmatic,/usr/bin/borgmatic," sample/cron/borgmatic
perl -pi -e "s,/root/.local/bin/borgmatic,/usr/bin/borgmatic," sample/systemd/borgmatic.service
perl -pi -e "s,=sleep,=/usr/bin/sleep," sample/systemd/borgmatic.service
perl -pi -e "s,=systemd-inhibit,=/usr/bin/systemd-inhibit," sample/systemd/borgmatic.service
perl -pi -e "s/ruamel.yaml>0.15.0,<0.17.0/ruamel.yaml/" setup.py
perl -pi -e "s/packages=find_packages\(\)/packages=find_packages(exclude=('tests*',))/" setup.py

%build
# Create the manpage
pandoc -s -f markdown -t man README.md -o borgmatic.1

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -d %{buildroot}%{_sysconfdir}/borgmatic
install -d %{buildroot}%{_sysconfdir}/borgmatic.d
install -d %{buildroot}%{_docdir}/%{name}/sample/cron
install -m 0644 sample/cron/borgmatic %{buildroot}%{_docdir}/%{name}/sample/cron/
install -d %{buildroot}%{_unitdir}/
install -m 0644 sample/systemd/borgmatic* %{buildroot}%{_unitdir}/

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
python3 -m venv --system-site-packages --without-pip borgmatic-env
source borgmatic-env/bin/activate
python3 setup.py install
PYTHONPATH=$(pwd) py.test -v --pyargs borgmatic tests

%post
%service_add_post borgmatic.service
if [ "$1" = 1 -a ! -f "%{_sysconfdir}/borgmatic/config.yaml" ]; then
    %{_bindir}/generate-borgmatic-config
elif [ "$1" = 2 ]; then
    if [ -f "%{_sysconfdir}/borgmatic/config" -a ! -f "%{_sysconfdir}/borgmatic/config.yaml" ]; then
       echo "The configuration files have changed. %{_bindir}/upgrade-borgmatic-config will be run now to upgrade the configuration to the new format."
       echo ""
       %{_bindir}/upgrade-borgmatic-config
    fi
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
%config %ghost %{_sysconfdir}/borgmatic/config.yaml
%dir %{_sysconfdir}/borgmatic
%dir %{_sysconfdir}/borgmatic.d
%dir %{_docdir}/%{name}/sample
%dir %{_docdir}/%{name}/sample/cron
%{python3_sitelib}/borgmatic/
%{python3_sitelib}/borgmatic-%{version}-py%{py3_ver}.egg-info
%{_unitdir}/borgmatic.service
%{_unitdir}/borgmatic.timer
%{_bindir}/borgmatic
%{_sbindir}/rcborgmatic
%{_bindir}/generate-borgmatic-config
%{_bindir}/upgrade-borgmatic-config
%{_bindir}/validate-borgmatic-config
%{_mandir}/man1/borgmatic.1%{?ext_man}
%{_docdir}/%{name}/sample/cron

%changelog
