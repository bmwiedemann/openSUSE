#
# spec file for package python-pytest-translations
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
Name:           python-pytest-translations
Version:        5.0.0
Release:        0
Summary:        Plugin for testing gettext, .po and .mo files
License:        Apache-2.0
URL:            https://github.com/Thermondo/pytest-translations
Source:         https://files.pythonhosted.org/packages/source/p/pytest-translations/pytest_translations-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  myspell-de_DE
BuildRequires:  python-rpm-macros
Requires:       python-polib >= 1.0.5
Requires:       python-pyenchant >= 1.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module polib >= 1.0.5}
BuildRequires:  %{python_module pyenchant >= 1.6.0}
BuildRequires:  %{python_module pytest > 5}
# /SECTION
%python_subpackages

%description
pytest-translations is a py.test plugin to check gettext, .po and .mo files.
Test check for:
-  Spelling (using enchant & aspell)
-  Consistency of mo files
-  Obsolete translations
-  Fuzzy translations

%prep
%setup -q -n pytest_translations-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_translations-%{version}.dist-info
%{python_sitelib}/pytest_translations

%changelog
