#
# spec file for package python-FormEncode
#
# Copyright (c) 2023 SUSE LLC
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
%{?sle15_python_module_pythons}
Name:           python-FormEncode
Version:        2.0.1
Release:        0
Summary:        HTML form validation, generation, and conversion package
License:        Python-2.0
Group:          Development/Languages/Python
URL:            http://formencode.org
Source:         https://files.pythonhosted.org/packages/source/F/FormEncode/FormEncode-%{version}.tar.gz
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module pycountry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm_git_archive}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-formencode = %{version}
Obsoletes:      %{oldpython}-formencode < %{version}
%endif
%python_subpackages

%description
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%prep
%setup -q -n FormEncode-%{version}

%build
%python_build

%install
%python_install
rm %{buildroot}%{_prefix}/LICENSE.txt
# trick find-lang.sh into finding the translation files
%python_expand mv %{buildroot}%{$python_sitelib}/formencode/{i18n,locale}
%python_find_lang FormEncode
sed -i s/locale/i18n/ python*-FormEncode.lang
%python_expand mv %{buildroot}%{$python_sitelib}/formencode/{locale,i18n}
# remove misplaced documentation
%python_expand rm -r %{buildroot}%{$python_sitelib}/docs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# excluded tests poll dns
donttest="(test_doctests and _wrapper-formencode.validators-False-True)"
donttest+=" or test_unicode_ascii_subgroup"
# 15.3 cannot fulfill test suite requirements with old versions; don't test on python2
python2_flags="--version"
%pytest -k "not ($donttest)" ${$python_flags}

%files %{python_files} -f %{python_prefix}-FormEncode.lang
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/formencode
%{python_sitelib}/FormEncode-%{version}*-info

%changelog
