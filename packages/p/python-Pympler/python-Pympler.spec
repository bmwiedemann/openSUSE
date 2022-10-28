#
# spec file for package python-Pympler
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-Pympler
Version:        1.0.1
Release:        0
Summary:        A tool to analyze the memory behavior of Python objects
License:        Apache-2.0
URL:            https://github.com/pympler/pympler
Source:         https://files.pythonhosted.org/packages/source/P/Pympler/Pympler-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pympler-flaky-tests.patch gh#pympler/pympler#90 mcepl@suse.com
# More cycles needed with more recent versions of Python
Patch0:         pympler-flaky-tests.patch
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-tk
%python_subpackages

%description
Pympler is a development tool to measure, monitor and analyze the
memory behavior of Python objects in a running Python application.

By pympling a Python application, detailed insight in the size and
the lifetime of Python objects can be obtained.  Undesirable or
unexpected runtime behavior like memory bloat and other "pymples"
can easily be identified.

%prep
%autosetup -p1 -n Pympler-%{version}

# Remove bundled bottle (gh#pympler/pympler#148)
rm pympler/util/bottle.py

# Remove unnecessary shebang
sed -i '1{\@^#!%{_bindir}/env python@d}' pympler/asizeof.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#pympler/pympler#134
skiptests="test_repr_function"
# gh#pympler/pympler#148
skiptests+=" or test_findgarbage or test_prune or test_get_tree"
%pytest -k "not ($skiptests)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pympler
%{python_sitelib}/Pympler-%{version}*-info

%changelog
