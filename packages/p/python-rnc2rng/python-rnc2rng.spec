#
# spec file for package python-rnc2rng
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-rnc2rng
Version:        2.6.6
Release:        0
Summary:        RELAX NG Compact to regular syntax conversion library
License:        MIT
URL:            https://github.com/djc/rnc2rng
Source:         https://files.pythonhosted.org/packages/source/r/rnc2rng/rnc2rng-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module rply}
# /SECTION
BuildRequires:  fdupes
Requires:       python-rply
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives


%python_subpackages

%description
RELAX NG Compact to regular syntax conversion library

%prep
%autosetup -p1 -n rnc2rng-%{version}

find . -name \*.py -exec sed -i -e '1{\@^#!\s*%{_bindir}/env python@d}' '{}' \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rnc2rng
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests are self-generated and mechanism doesn't work with the
# standard unittest runner.
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test.py -v
}

%post
%python_install_alternative rnc2rng

%postun
%python_uninstall_alternative rnc2rng

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%python_alternative %{_bindir}/rnc2rng
%{python_sitelib}/rnc2rng
%{python_sitelib}/rnc2rng-%{version}*-info

%changelog
