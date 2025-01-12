#
# spec file for package python-mistune
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


%define modname mistune
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        3.1.0
Release:        0
Summary:        Python Markdown parser with renderers and plugins
License:        BSD-3-Clause
URL:            https://github.com/lepture/mistune
Source:         https://github.com/lepture/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if "%{python_flavor}" < "python311"
Requires:       python-typing_extensions
%endif
BuildArch:      noarch
Conflicts:      python-mistune2 < %{version}
Obsoletes:      python-mistune2 < %{version}
%python_subpackages

%description
A Python Markdown parser with renderers and plugins,
compatible with sane CommonMark rules.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
