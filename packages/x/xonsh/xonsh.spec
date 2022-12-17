#
# spec file for package xonsh
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


%define pythons python3
Name:           xonsh
Version:        0.13.4
Release:        0
Summary:        A general purpose, Python-powered shell
License:        BSD-2-Clause AND BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://xon.sh/
Source0:        https://github.com/xonsh/xonsh/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-base >= 3.8
BuildRequires:  python3-setuptools >= 61
BuildRequires:  python3-wheel
Recommends:     python3-Pygments >= 2.2
Recommends:     python3-distro
Recommends:     python3-ply
Recommends:     python3-prompt_toolkit >= 2.0
Recommends:     python3-setproctitle
Requires:       python3-base >= 3.5
Suggests:       %{name}-doc
Provides:       python3-xonsh = %{version}
Obsoletes:      python3-xonsh < %{version}
BuildArch:      noarch

%package -n %{name}-doc
Summary:        Documentation files for %name
Group:          Documentation/HTML

%description
xonsh is a Python-powered, Unix-gazing shell language and command prompt. The language is a superset of Python 3.5+ with additional shell primitives. xonsh (pronounced conch) is meant for the daily use of experts and novices alike.

%description -n %{name}-doc
HTML documentation on the API and examples for %name.

%prep
%setup -q -n xonsh-%{version}
sed -i '1s/^#!.*//' xonsh/xoreutils/_which.py xonsh/webconfig/main.py xonsh/xoreutils/uname.py
rm docs/api/.gitignore

%build
%python_build
# docs require unavailable theme 'furo'

%install
%python_install
%fdupes %{buildroot}
%fdupes -s docs/
%fdupes -s docs/_build/html/

%files
%{python3_sitelib}/xonsh/
%{python3_sitelib}/xontrib/
%{python3_sitelib}/xompletions/
%{python3_sitelib}/xonsh-%{version}*-info
%{_bindir}/xonsh
%{_bindir}/xonsh-cat
%{_bindir}/xonsh-uptime
%{_bindir}/xonsh-uname
%doc README.rst logo.txt CHANGELOG.rst
%doc xontrib
%license license

%files doc
%doc docs

%changelog
