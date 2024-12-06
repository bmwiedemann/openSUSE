#
# spec file for package zypper-keys-plugin
#
# Copyright (c) 2024 SUSE LLC
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


%define use_python python3
%define pythons %{use_python}

Name:           zypper-keys-plugin
Version:        0.4.0
Release:        0
Summary:        Zypper plugin to manage RPM keys
License:        AGPL-3.0-or-later
Group:          System/Packages
URL:            https://github.com/asdil12/%{name}
Source0:        https://github.com/asdil12/zyppkeys/archive/v%{version}.tar.gz#/zyppkeys-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

BuildRequires:  help2man
BuildRequires:  python3
BuildRequires:  python3-pytz
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  zypper
Requires:       sudo
# rpm --import used curl but doesn't require it explicitly
Requires:       curl
Requires:       python3-pytz
Requires:       python3-requests
Requires:       zypper

%description
Zypper plugin for RPM key management

%prep
%setup -q -n zyppkeys-%{version}

%build
ln -s zyppkeys ./bin/zypper-keys
help2man -s8 -N ./bin/zypper-keys -n "Manage RPM keys" > zypper-keys.8
%pyproject_wheel

%install
%pyproject_install
install -m 644 -D -v zypper-keys.8 %{buildroot}%{_datadir}/man/man8/zypper-keys.8
# Install as zypper plugin instead of standalone application
mkdir -p %{buildroot}/usr/lib/zypper/commands/
mv -v %{buildroot}/%{_bindir}/zyppkeys %{buildroot}/usr/lib/zypper/commands/zypper-keys
%python3_fix_shebang
%fdupes %{buildroot}%{python3_sitelib}

%check
python3 setup.py --version | grep %{version}

%files
%license LICENSE
%doc README.md
%dir /usr/lib/zypper/commands/
/usr/lib/zypper/commands/zypper-keys
%{_datadir}/man/man8/zypper-keys.8%{?ext_man}
%{python3_sitelib}/*

%changelog
