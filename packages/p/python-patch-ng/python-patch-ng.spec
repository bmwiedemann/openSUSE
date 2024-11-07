#
# spec file for package python-patch-ng
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-patch-ng
Version:        1.18.1
Release:        0
Summary:        Library to parse and apply unified diffs
License:        MIT
URL:            https://github.com/conan-io/python-patch
# PyPI sources do not include tests
Source:         https://github.com/conan-io/python-patch-ng/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Patch-ng is a Python library to parse and apply unified diffs.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
sed -Ei "1{\@%{_bindir}/env python@d}" %{buildroot}%{$python_sitelib}/patch_ng.py
}

%check
# run_tests.py is a proprietary ultra-complicated beast
# not replaceable by anything standard
%python_exec tests/run_tests.py -v

%files %{python_files}
%doc README.md
%{python_sitelib}/patch_ng.py
%{python_sitelib}/patch_ng-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/patch_ng*.pyc

%changelog
