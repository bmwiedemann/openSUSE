#
# spec file for package python-Yapsy
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-Yapsy
Version:        1.12.2
Release:        0
Summary:        Yet another plugin system
License:        BSD-2-Clause
URL:            https://yapsy.sourceforge.net
Source:         https://files.pythonhosted.org/packages/source/Y/Yapsy/Yapsy-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/tibonihoo/yapsy/pull/11 Replace Deprecated API's
Patch0:         replace-deprecated-apis.patch
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-yapsy
Obsoletes:      %{name}-doc
BuildArch:      noarch
%python_subpackages

%description
Yapsy is a small library implementing the core mechanisms needed to
build a plugin system into a wider application.

The main purpose is to depend only on Python's standard libraries (at
least version 2.3) and to implement only the basic functionalities
needed to detect, load and keep track of several plugins.

%prep
%autosetup -p1 -n Yapsy-%{version}

%build
%pyproject_wheel
find yapsy/ -name "*.py" -exec sed -i -e  '/^#!\s\?\/usr\/bin\/\(env\s\)\?python$/d' {} ';'

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%{python_sitelib}/yapsy
%{python_sitelib}/yapsy-%{version}.dist-info
%doc CHANGELOG.txt README.txt
%license LICENSE.txt

%changelog
