#
# spec file for package python-iso3166
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-iso3166
Version:        1.0.1
Release:        0
Summary:        Python ISO 3166-1 country definitions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/deactivated/python-iso3166
Source:         https://files.pythonhosted.org/packages/source/i/iso3166/iso3166-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
ISO 3166-1 defines two-letter, three-letter, and three-digit country
codes. `python-iso3166` is a self-contained module that converts
between these codes and the corresponding country name.

%prep
%setup -q -n iso3166-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
