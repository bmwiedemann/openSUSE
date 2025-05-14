#
# spec file for package python-ansicolors
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


Name:           python-ansicolors
Version:        1.1.8
Release:        0
Summary:        ANSI colors for Python
License:        ISC
URL:            https://github.com/jonathaneunice/colors/
Source:         https://files.pythonhosted.org/packages/source/a/ansicolors/ansicolors-%{version}.zip
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Add ANSI colors and decorations to your strings.

%prep
%setup -q -n ansicolors-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.yml README.rst
%license LICENSE
%{python_sitelib}/colors
%{python_sitelib}/ansicolors-%{version}*-info

%changelog
