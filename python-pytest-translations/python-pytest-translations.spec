#
# spec file for package python-pytest-translations
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%bcond_without test
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-translations
Version:        2.0.0
Release:        0
License:        Apache-2.0
Summary:        py.test plugin for testing gettext, .po and .mo files
Url:            https://github.com/Thermondo/pytest-translations
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pytest-translations/pytest-translations-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pbr}
%if %{with test}
BuildRequires:  %{python_module polib >= 1.0.5}
BuildRequires:  %{python_module pyenchant >= 1.6.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  myspell-de_DE
%endif
BuildRequires:  fdupes
Requires:       python-polib >= 1.0.5
Requires:       python-pyenchant >= 1.6.0
BuildArch:      noarch

%python_subpackages

%description
pytest-translations is a py.test plugin to check gettext, .po and .mo files.
Test check for:
-  Spelling (using enchant & aspell)
-  Consistency of mo files
-  Obsolete translations
-  Fuzzy translations

%prep
%setup -q -n pytest-translations-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
export PYTHONPATH=$PWD
%python_exec %{_bindir}/py.test
%endif

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitelib}/pytest_translations-%{version}-py%{py_ver}.egg-info/
%{python_sitelib}/pytest_translations

%changelog
