#
# spec file for package python-deepdiff
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-deepdiff
Version:        9.0.0
Release:        0
Summary:        Deep Difference and Search of any Python object/data
License:        MIT
URL:            https://github.com/seperman/deepdiff
Source:         https://github.com/seperman/deepdiff/archive/%{version}.tar.gz#/deepdiff-%{version}-gh.tar.gz
BuildRequires:  %{python_module PyYAML >= 6.0.3}
BuildRequires:  %{python_module click >= 8.3.1}
BuildRequires:  %{python_module flit-core >= 3.11}
BuildRequires:  %{python_module jsonpickle >= 4.1.1}
BuildRequires:  %{python_module orderly-set >= 5.5.0}
BuildRequires:  %{python_module orjson >= 3.11.7}
BuildRequires:  %{python_module pandas >= 2.2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 2.12.5}
BuildRequires:  %{python_module pytest >= 9.0.2}
BuildRequires:  %{python_module pytest-benchmark >= 5.2.3}
BuildRequires:  %{python_module python-dateutil >= 2.9.0}
BuildRequires:  %{python_module tomli >= 2.4.0}
BuildRequires:  %{python_module tomli-w >= 1.2.0}
BuildRequires:  %{python_module uuid6 == 2025.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-orderly-set >= 5.5.0

%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

# Required for cli tool
Requires:       python-PyYAML
Requires:       python-click

Recommends:     python-jsonpickle
Recommends:     python-numpy
Recommends:     python-orjson
Recommends:     python-tomli
#Suggests:     python-clevercsv
BuildArch:      noarch
%python_subpackages

%description
A Python module to calculate Deep Difference of dictionaries,
iterables, strings and other objects. It can search for objects
within other objects, and hash any object based on their content.

%prep
%autosetup -p1 -n deepdiff-%{version}
sed -i '1{/env python/d}' deepdiff/deephash.py deepdiff/diff.py deepdiff/search.py
chmod -x deepdiff/diff.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/deep
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we don't have the (optional) requirement CleverCSV for csv diffing
donttest="(TestCommands and (csv or group_by)) or (test_load_path_content and csv) or (test_polars)"
# failure on Python 3.13 https://github.com/seperman/deepdiff/issues/474
donttest+=" or (TestCommands and test_diff_command and t1_corrupt)"
%pytest -k "not ($donttest)"

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative deep

%post
%python_install_alternative deep

%postun
%python_uninstall_alternative deep

%files %{python_files}
%license LICENSE
%doc README.md AUTHORS.md
%{python_sitelib}/deepdiff
%{python_sitelib}/deepdiff-%{version}.dist-info
%python_alternative %{_bindir}/deep

%changelog
