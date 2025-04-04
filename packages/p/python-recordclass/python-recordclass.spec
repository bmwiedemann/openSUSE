#
# spec file for package python-recordclass
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


Name:           python-recordclass
Version:        0.22.1
Release:        0
Summary:        Library implementing a mutable variant of namedtuple
License:        MIT
URL:            https://github.com/intellimath/recordclass
Source:         https://files.pythonhosted.org/packages/source/r/recordclass/recordclass-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#intellimath/recordclass#338044cbf771e5665a744d3b36b5d7edd126d16a
Patch0:         do-not-use-pytuple-get-size.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION Test requirements
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyperf}
# /SECTION
%python_subpackages

%description
Mutable variant of namedtuple -- recordclass, which support assignments, and
other memory saving variants.

%prep
%autosetup -p1 -n recordclass-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Crashes when run using pytest
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} python%{$python_version} test_all.py

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/recordclass/
%{python_sitearch}/recordclass-%{version}.dist-info

%changelog
