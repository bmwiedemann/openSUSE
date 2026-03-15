#
# spec file for package python-croniter
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-croniter
Version:        6.1.0
Release:        0
Summary:        Python iterators for datetime objects with cron-like format
License:        MIT
URL:            https://github.com/kiorky/croniter
Source:         https://files.pythonhosted.org/packages/source/c/croniter/croniter-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 8.3.3}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz > 2021.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
croniter provides iterators for datetime object with cron-like format.

%prep
%setup -q -n croniter-%{version}
find . -name "*.py" | xargs chmod -x
find . -name "*.py" | xargs sed -i '1 { /^#!/ d }'

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest src

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/croniter
%{python_sitelib}/croniter-%{version}.dist-info

%changelog
