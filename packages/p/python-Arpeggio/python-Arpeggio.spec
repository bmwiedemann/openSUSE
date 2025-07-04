#
# spec file for package python-Arpeggio
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
Name:           python-Arpeggio
Version:        2.0.2
Release:        0
Summary:        Packrat parser interpreter
License:        MIT
URL:            https://github.com/textX/Arpeggio/
Source:         https://github.com/textX/Arpeggio/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Arpeggio is a recursive descent parser with memoization based on PEG grammars
(aka Packrat parser).

For a higher level parsing/language tool (i.e., a nicer interface to
Arpeggio) see textX

%prep
%setup -q -n Arpeggio-%{version}
# remove shebang
sed -i '1d' arpeggio/tests/regressions/issue_16/test_issue_16.py
# https://github.com/textX/Arpeggio/issues/94
sed -i '/pytest-runner/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest arpeggio/tests

%files %{python_files}
%doc README.md CHANGELOG.md AUTHORS.md
%license LICENSE
%{python_sitelib}/arpeggio
%{python_sitelib}/[Aa]rpeggio-%{version}.dist-info

%changelog
