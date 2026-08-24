#
# spec file for package python-easydict
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


%{?sle15_python_module_pythons}
Name:           python-easydict
Version:        1.13
Release:        0
Summary:        Access dict values as attributes (works recursively)
License:        LGPL-3.0-only
URL:            https://github.com/makinacorpus/easydict
Source:         https://files.pythonhosted.org/packages/source/e/easydict/easydict-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
EasyDict allows accessing dict values as attributes (works
recursively). It provides Javascript-like properties dot notation
for Python dicts.

%prep
%autosetup -p1 -n easydict-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Upstream ships no pytest suite; CI runs doctest on the module.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import doctest, easydict; r = doctest.testmod(easydict); raise SystemExit(r.failed)"

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES
%{python_sitelib}/easydict
%{python_sitelib}/easydict-%{version}.dist-info

%changelog
