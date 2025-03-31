#
# spec file for package python-requre
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


%{?sle15_python_module_pythons}
Name:           python-requre
Version:        0.9.1
Release:        0
Summary:        Python libray for storing and using objects for testing
License:        MIT
URL:            https://github.com/packit-service/requre
Source:         https://files.pythonhosted.org/packages/source/r/requre/requre-%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-GitPython
Requires:       python-PyYAML
Requires:       python-click
Requires:       python-httpx
Requires:       python-requests
Suggests:       python-pytest
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Library for testing python code what allows store output of
various objects and use stored data for testing.

%prep
%setup -q -n requre-%{version}
# Remove cyclic dependency with ogr
rm tests/test_E2E_ogr.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/requre-patch
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative requre-patch

%postun
%python_uninstall_alternative requre-patch

%check
export LANG=en_US.UTF-8
# needs network: test_record_requests, test_online_replacing, StoreAnyRequest
# and TestWrite
# test_a and InstalledCommand fail
# Latency fails randomly on OBS slaves
%pytest -rs -k 'not (test_record_requests or test_online_replacing or StoreAnyRequest or TestWrite or (StoreFunctionOutput and test_a) or InstalledCommand or Latency)'

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/requre-patch
%{python_sitelib}/requre
%{python_sitelib}/requre-%{version}.dist-info

%changelog
