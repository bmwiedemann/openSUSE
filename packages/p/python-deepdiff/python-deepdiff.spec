#
# spec file for package python-deepdiff
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-deepdiff
Version:        5.2.3
Release:        0
Summary:        Deep Difference and Search of any Python object/data
License:        MIT
URL:            https://github.com/seperman/deepdiff
Source:         https://github.com/seperman/deepdiff/archive/%{version}.tar.gz#/deepdiff-%{version}-gh.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module ordered-set}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
#BuildRequires:  %%{python_module clevercsv} # not available
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires:       python-ordered-set
Recommends:     python-clevercsv
Recommends:     python-click
Recommends:     python-jsonpickle
Recommends:     python-numpy
Recommends:     python-pyyaml
Recommends:     python-toml
BuildArch:      noarch
%python_subpackages

%description
A Python module to calculate Deep Difference of dictionaries,
iterables, strings and other objects. It can search for objects
within other objects, and hash any object based on their content.

%prep
%autosetup -p1 -n deepdiff-%{version}
sed -i '1{/env python/d}' deepdiff/deephash.py deepdiff/diff.py deepdiff/search.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/deep
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we don't have the (optional) requirement CleverCSV for csv diffing
donttest="(TestCommands and (csv or group_by)) or (test_load_path_content and csv)"
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # reference expects int64 where 32-bit platforms return int32
  donttest+=" or (test_numpy_delta_cases and delta_numpy7_arrays_of_different_sizes)"
fi
%pytest -k "not ($donttest)"

%post
%python_install_alternative deep

%postun
%python_uninstall_alternative deep

%files %{python_files}
%license LICENSE
%doc README.md AUTHORS.md
%{python_sitelib}/deepdiff
%{python_sitelib}/deepdiff-%{version}*-info
%python_alternative %{_bindir}/deep

%changelog
