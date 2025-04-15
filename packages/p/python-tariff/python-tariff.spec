#
# spec file for package python-tariff
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


Name:           python-tariff
Version:        1.0.0
Release:        0
Summary:        Make importing great again!
License:        MIT
URL:            https://github.com/hxu296/tariff
Source:         https://files.pythonhosted.org/packages/source/t/tariff/tariff-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Conflicts:      globalization
%python_subpackages

%description
Make importing great again! A parody package that imposes tariffs on Python imports.

%prep
%autosetup -p1 -n tariff-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The greatest package like this doesn’t any stinking tests!

%files %{python_files}
%doc README.md
%license LICENSE LICENSE
%{python_sitelib}/tariff
%{python_sitelib}/tariff-%{version}.dist-info

%changelog
