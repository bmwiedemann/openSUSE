#
# spec file for package queue
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


Name:           queue
Version:        1.2.0
Release:        0
Summary:        Tool for queuing shell commands
License:        GPL-3.0-or-later
URL:            https://github.com/asdil12/%{name}
Source0:        https://github.com/asdil12/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-base >= 3.6
BuildRequires:  python3-pip
BuildRequires:  python3-psutil
BuildRequires:  python3-setuptools
BuildRequires:  python3-termcolor
BuildRequires:  python3-tomlkit
BuildRequires:  python3-wheel
Requires:       python3-psutil
Requires:       python3-termcolor
Requires:       python3-tomlkit
BuildArch:      noarch

%description
This tool allows to queue shell commands.
It supports multiple queues as well as multiple queue workers.

%prep
%setup -q

%build
./bin/queue
help2man -s8 -N ./bin/queue -n "Queue shell commands" > queue.8
%python3_pyproject_wheel

%install
%python3_pyproject_install
install -m 644 -D -v queue.8 %{buildroot}%{_mandir}/man8/queue.8
%{python3_fix_shebang}
%fdupes %{buildroot}%{python3_sitelib}

%check
python3 setup.py --version | grep %{version}

%files
%license LICENSE
%doc README.md
%{_bindir}/queue
%{_mandir}/man8/queue.8%{?ext_man}
%{python3_sitelib}/cmdqueue
%{python3_sitelib}/cmdqueue-%{version}*-info

%changelog
