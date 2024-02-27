#
# spec file for package python-subst
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


Name:           python-subst
Version:        0.4.0
Release:        0
Summary:        Utility to replace one string into another in given list of files
License:        MIT
URL:            https://github.com/msztolcman/subst
Source:         https://files.pythonhosted.org/packages/source/s/subst/subst-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/msztolcman/subst/master/LICENSE
Patch0:         fix-assertions.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
`subst` is simple utility to replace one string into another in given list of files.

%prep
%autosetup -p1 -n subst-%{version}
cp %{SOURCE1} .
sed -i '/argparse/d' setup.py
sed -i '1{/^#!/d}' subst.py
touch test/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/subst
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}/test
%pytest

%post
%python_install_alternative subst

%postun
%python_uninstall_alternative subst

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/subst
%{python_sitelib}/subst.py
%pycache_only %{python_sitelib}/__pycache__/subst.*.py*
%{python_sitelib}/subst-%{version}.dist-info

%changelog
