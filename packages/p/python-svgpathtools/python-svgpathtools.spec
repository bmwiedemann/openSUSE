#
# spec file for package python-svgpathtools
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-svgpathtools
Version:        1.7.2
Release:        0
Summary:        Tools for manipulating and analyzing SVG Path objects and Bézier curves
License:        MIT
URL:            https://github.com/mathandy/svgpathtools
Source:         https://files.pythonhosted.org/packages/source/s/svgpathtools/svgpathtools-%{version}.tar.gz
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module svgwrite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-scipy
Requires:       python-svgwrite
BuildArch:      noarch
%python_subpackages

%description
Svgpathtools is a collection of tools for manipulating and
analyzing SVG Path objects and Bézier curves.

%prep
%setup -q -n svgpathtools-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt LICENSE2.txt
%doc README.md
%{python_sitelib}/svgpathtools*

%changelog
