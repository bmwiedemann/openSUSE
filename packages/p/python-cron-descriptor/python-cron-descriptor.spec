#
# spec file for package python-cron-descriptor
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


Name:           python-cron-descriptor
Version:        1.4.5
Release:        0
Summary:        Python library that converts cron expressions into human readable strings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Salamek/cron-descriptor
Source:         https://github.com/Salamek/cron-descriptor/archive/%{version}.tar.gz#/cron_descriptor-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python library that converts cron expressions into human readable strings.

%prep
%setup -q -n cron-descriptor-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/*.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cron_descriptor
%{python_sitelib}/cron_descriptor-%{version}.dist-info
%lang(all) %{python_sitelib}/cron_descriptor/locale/

%changelog
