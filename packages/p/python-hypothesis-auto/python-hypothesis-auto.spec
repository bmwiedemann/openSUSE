#
# spec file for package python-hypothesis-auto
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
# no tags no releases on github.
%define commitid 4ed588ab631d6c44c8959334a3425a8c0d207eff
Name:           python-hypothesis-auto
Version:        1.1.4
Release:        0
Summary:        Extends Hypothesis to add fully automatic testing of type annotated functions
License:        MIT
Group:          Development/Languages/Python
URL:            https://timothycrosley.github.io/hypothesis-auto/
Source0:        https://files.pythonhosted.org/packages/source/h/hypothesis-auto/hypothesis-auto-%{version}.tar.gz
# for the unit tests
Source1:        https://github.com/timothycrosley/hypothesis-auto/archive/%{commitid}.tar.gz#/hypothesis-auto-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hypothesis >= 4.36
Requires:       python-pydantic >= 0.32.2
Suggests:       python-pytest >= 4.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 4.36}
BuildRequires:  %{python_module pydantic >= 0.32.2}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
An extension for the Hypothesis project that enables fully automatic tests for type annotated functions.

%prep
%setup -q -n hypothesis-auto-%{version}
tar -x --strip-components=1 -f %{SOURCE1} hypothesis-auto-%{commitid}/tests/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/hypothesis_auto
%{python_sitelib}/hypothesis_auto-%{version}-py*.egg-info

%changelog
