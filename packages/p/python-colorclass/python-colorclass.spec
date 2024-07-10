#
# spec file for package python-colorclass
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-colorclass
Version:        2.2.2
Release:        0
Summary:        ANSI text color library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/matthewdeanmartin/colorclass/
Source:         https://github.com/matthewdeanmartin/colorclass/archive/refs/tags/v%{version}.tar.gz#/colorclass-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM colorclass-pr2-poetry-core.patch gh#matthewdeanmartin/colorclass#2
Patch0:         colorclass-pr2-poetry-core.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Yet another ANSI color text library for Python. It provides "auto
colors" for dark/light terminals.

In Python 2.x, this library subclasses `unicode`, while on
Python 3.x, it subclasses `str`.

%prep
%autosetup -p1 -n colorclass-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
# show rpmlint a non-empty metadata file (poetry creates those)
echo " " >> %{buildroot}%{$python_sitelib}/colorclass-%{version}.dist-info/entry_points.txt
# standard dedup
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest -k 'not test_piped'

%files %{python_files}
%{python_sitelib}/colorclass
%{python_sitelib}/colorclass-%{version}.dist-info

%changelog
