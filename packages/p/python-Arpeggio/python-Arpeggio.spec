#
# spec file for package python-Arpeggio
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
Name:           python-Arpeggio
Version:        1.9.2
Release:        0
Summary:        Packrat parser interpreter
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/textX/Arpeggio/
Source:         https://github.com/textX/Arpeggio/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/textX/Arpeggio/issues/57
BuildRequires:  %{python_module pytest < 5.0}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
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
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest arpeggio/tests

%files %{python_files}
%doc README.rst CHANGELOG.md AUTHORS.md
%license LICENSE
%{python_sitelib}/*

%changelog
