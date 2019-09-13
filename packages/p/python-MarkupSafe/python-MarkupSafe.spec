#
# spec file for package python-MarkupSafe
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-MarkupSafe
Version:        1.1.1
Release:        0
URL:            https://github.com/pallets/markupsafe
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%ifpython2
Provides:       %{oldpython}-markupsafe = %{version}
Obsoletes:      %{oldpython}-markupsafe < %{version}
%endif

%python_subpackages

%description
Implements a unicode subclass that supports HTML strings. This can be used to
safely encode strings for dynamically generated web pages.

%prep
%setup -q -n MarkupSafe-%{version}
rm docs/make.bat docs/Makefile docs/conf.py docs/requirements.txt

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/markupsafe/_speedups.c

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m pytest

%files %{python_files}
%license LICENSE.rst
%doc README.rst docs/
%{python_sitearch}/markupsafe/
%{python_sitearch}/MarkupSafe-%{version}-py*.egg-info

%changelog
