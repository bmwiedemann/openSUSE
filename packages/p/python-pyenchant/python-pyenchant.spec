#
# spec file for package python-pyenchant
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
%define skip_python2 1
Name:           python-pyenchant
Version:        3.1.0
Release:        0
Summary:        Python bindings for the Enchant spellchecking system
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://pyenchant.github.io/pyenchant
Source:         https://github.com/pyenchant/pyenchant/archive/v%{version}.tar.gz#/pyenchant-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
%if 0%{?suse_version} > 1500
BuildRequires:  enchant-2-backend-hunspell
%else
BuildRequires:  enchant
%endif
BuildRequires:  fdupes
BuildRequires:  myspell-en
BuildRequires:  myspell-en_AU
BuildRequires:  myspell-en_US
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} > 1500
Requires:       enchant-2-backend-hunspell
%else
Requires:       enchant
%endif
Provides:       python-enchant
BuildArch:      noarch
%python_subpackages

%description
PyEnchant is a spellchecking library for Python, based on the excellent Enchant library.

%prep
%setup -q -n pyenchant-%{version}
chmod a-x *.txt
# cleanup github tarball
rm -rf website .github archive tools

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec -c 'import enchant; print(vars(enchant.Dict()))'
# gh#pyenchant/pyenchant#203
%pytest -k 'not test_docstrings'

%files %{python_files}
%license LICENSE.txt
%doc README.rst TODO.txt
%{python_sitelib}/enchant
%{python_sitelib}/pyenchant-%{version}-py*.egg-info

%changelog
