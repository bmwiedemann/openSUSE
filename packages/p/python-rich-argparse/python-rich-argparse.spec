#
# spec file for package python-rich-argparse
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-rich-argparse
Version:        1.7.2
Release:        0
Summary:        Rich help formatters for argparse and optparse
License:        MIT
URL:            https://github.com/hamdanal/rich-argparse
Source:         https://files.pythonhosted.org/packages/source/r/rich-argparse/rich_argparse-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-tests.patch https://github.com/hamdanal/rich-argparse/pull/178
Patch0:         fix-tests.patch
# PATCH-FIX-UPSTREAM py3141.patch https://github.com/hamdanal/rich-argparse/pull/172
Patch1:         py3141.patch
BuildRequires:  %{python_module hatchling >= 1.11.0}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 11.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-rich >= 11.0.0
BuildArch:      noarch
%python_subpackages

%description
Format argparse and optparse help using [rich](https://pypi.org/project/rich).

*rich-argparse* improves the look and readability of argparse's help while requiring minimal
changes to the code.

%prep
%autosetup -p1 -n rich_argparse-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/rich_argparse
%{python_sitelib}/rich_argparse-%{version}*info

%changelog
