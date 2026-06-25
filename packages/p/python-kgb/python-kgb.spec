#
# spec file for package python-kgb
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-kgb
Version:        7.3
Release:        0
Summary:        Function spies for Python unit tests
License:        MIT
URL:            https://github.com/beanbaginc/kgb
Source:         https://files.pythonhosted.org/packages/source/k/kgb/kgb-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
kgb installs spies onto functions and methods, letting Python unit
tests assert how and how often a function was called, transparently
record or fake its behaviour, and inspect the arguments it received.

%prep
%autosetup -p1 -n kgb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/kgb
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest kgb

%files %{python_files}
%license LICENSE
%doc AUTHORS NEWS.rst README.rst
%{python_sitelib}/kgb
%{python_sitelib}/kgb-%{version}.dist-info

%changelog
