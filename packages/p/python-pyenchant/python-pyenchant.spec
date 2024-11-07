#
# spec file for package python-pyenchant
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


%{?sle15_python_module_pythons}
Name:           python-pyenchant
Version:        3.2.2
Release:        0
Summary:        Python bindings for the Enchant spellchecking system
License:        LGPL-2.1-or-later
URL:            https://pyenchant.github.io/pyenchant
Source:         https://github.com/pyenchant/pyenchant/archive/v%{version}.tar.gz#/pyenchant-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec -c 'import enchant; print(vars(enchant.Dict()))'
ignore=""
%if 0%{suse_version} == 1600
# test_can_use_multiprocessing fails to build in OBS for ALP,
# bsc#1221034
ignore="--ignore tests/test_multiprocessing.py"
%endif
# two tests fail with enchant 2.5.0+, upstream is almost dead https://github.com/pyenchant/pyenchant/issues/313
%pytest $ignore -k "not (pwl and (test_suggestions or test_dwpwl))"

%files %{python_files}
%license LICENSE.txt
%doc README.rst TODO.txt
%{python_sitelib}/enchant
%{python_sitelib}/pyenchant-%{version}.dist-info

%changelog
