#
# spec file for package python-python-crontab
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-python-crontab
Version:        2.7.1
Release:        0
Summary:        Python Crontab API
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://gitlab.com/doctormo/python-crontab/
Source:         https://files.pythonhosted.org/packages/source/p/python-crontab/python-crontab-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Recommends:     cronie
Recommends:     python-cron-descriptor
Recommends:     python-croniter
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cron-descriptor}
BuildRequires:  %{python_module croniter}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module testsuite if %python-base >= 3}
BuildRequires:  cronie
# /SECTION
%python_subpackages

%description
Crontab module for reading and writing crontab files and
accessing the system cron automatically using an API.

%prep
%setup -q -n python-crontab-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%{python_expand mkdir -p build/bin
ln -s %{_bindir}/$python build/bin/python
}
export PATH=$PWD/build/bin:$PATH
# test_07_non_posix_shell - only for Windows
%pytest -k "not test_07_non_posix_shell"

%files %{python_files}
%doc README.rst
%license COPYING AUTHORS
%{python_sitelib}/cronlog.py
%{python_sitelib}/crontab.py
%{python_sitelib}/crontabs.py
%{python_sitelib}/python_crontab-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
