#
# spec file for package python-preggy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-preggy
Version:        1.4.2
Release:        0
Summary:        Assertion library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/heynemann/preggy
Source:         https://files.pythonhosted.org/packages/source/p/preggy/preggy-%{version}.tar.gz
# https://github.com/heynemann/preggy/issues/32 re LICENSE
Patch0:         split-readme.patch
BuildRequires:  %{python_module Unidecode}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Unidecode
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
preggy is an assertion library for Python. (What were you ``expect()``ing?)
Part of the pyVows test framework.

%prep
%setup -q -n preggy-%{version}
%patch0 -p1
sed -i '/^#!/d' preggy/__main__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
