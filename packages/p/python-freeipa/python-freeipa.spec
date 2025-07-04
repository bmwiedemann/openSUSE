#
# spec file for package python-freeipa
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


%global pypi_name python-freeipa
%global srcname freeipa

Name:           python-%{srcname}
Version:        1.0.6
Release:        0
Summary:        Lightweight FreeIPA client
License:        MIT
URL:            https://python-freeipa.readthedocs.io/
Source0:        https://github.com/opennode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

Requires:       python-requests

%python_subpackages

%description
python-freeipa is lightweight FreeIPA client.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest src/python_freeipa/tests/suite.py

%files %{python_files}
%license LICENSE.md
%doc README.rst
%{python_sitelib}/python_freeipa/
%{python_sitelib}/python_freeipa-%{version}.dist-info/

%changelog
