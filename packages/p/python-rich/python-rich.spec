#
# spec file for package python-rich
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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
Name:           python-rich
Version:        9.1.0
Release:        0
Summary:        A Python library for rich text and beautiful formatting in the terminal
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/willmcgugan/rich
Source:         https://github.com/willmcgugan/rich/archive/v%{version}.tar.gz#/rich-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module colorama >= 0.4.0}
BuildRequires:  %{python_module commonmark >= 0.9.0}
BuildRequires:  %{python_module pygments >= 2.6.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 3.7.4}
# /SECTION
BuildRequires:  fdupes
Requires:       python-colorama >= 0.4.0
Requires:       python-commonmark >= 0.9.0
Requires:       python-pygments >= 2.6.0
Requires:       python-typing_extensions >= 3.7.4
%if %{python_version_nodots} < 37
Requires:       python-dataclasses >= 0.7
%endif
BuildArch:      noarch
%python_subpackages

%description
Render rich text, tables, progress bars, syntax highlighting,
markdown and more to the terminal.

%prep
%setup -q -n rich-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_log'

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/rich
%{python_sitelib}/rich-%{version}*-info

%changelog
