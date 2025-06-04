#
# spec file for package python-cfgdiff
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


%bcond_without libalternatives
Name:           python-cfgdiff
Version:        0.0.0+git.1641843506.dc1234a
Release:        0
Summary:        Cfgdiff -- diff(1) all your configuration files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/evgeni/cfgdiff
Source:         cfgdiff-%{version}.tar.xz
### SECTION test requirements
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
## /SECTION
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Provides:       cfgdiff
BuildArch:      noarch
%python_subpackages

%description
cfgdiff will try to parse your configuration files, fetching all
the relevant keys and values from them and then pretty-printing
them in the original format.
These results are then diffed and the diff is shown to you.

cfgdiff currently supports the following formats:
 - INI using Python's ConfigParser library
 - JSON using Python's JSON library
 - YAML if the Python YAML library is installed
 - XML if the Python lxml library is installed

%prep
%setup -q -n cfgdiff-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/cfgdiff

%pre
# Removing old update-alternatives entries.
%python_libalternatives_reset_alternative cfgdiff

%check
export PYTHONPATH=.
%pyunittest tests/test_cfgdiff.py -v

%files %{python_files}
%license LICENSE README.md
%{python_sitelib}/cfgdiff.py
%{python_sitelib}/cfgdiff-*-info
%pycache_only %{python_sitelib}/__pycache__/cfgdiff*
%python_alternative %{_bindir}/cfgdiff

%changelog
