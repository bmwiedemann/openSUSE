#
# spec file for package python-pytils
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


%{?sle15_python_module_pythons}
Name:           python-pytils
Version:        0.4.3
Release:        0
Summary:        A Russian-specific string utility module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/y10h/pytils
Source:         https://files.pythonhosted.org/packages/source/p/pytils/pytils-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Tools for processing strings in Russian (choosing proper form for plurals,
in-words representation of numerals, dates in Russian without locales,
transliteration, etc.)

%prep
%autosetup -p1 -n pytils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# requires django, it is skipped in pytils/test/__init__.py
rm -r pytils/test/templatetags
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%{python_sitelib}/pytils
%{python_sitelib}/pytils-%{version}*-info

%changelog
