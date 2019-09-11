#
# spec file for package python-xmldiff
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
Name:           python-xmldiff
Version:        2.3
Release:        0
Summary:        Tree to tree correction between XML documents
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Shoobx/xmldiff
Source:         https://files.pythonhosted.org/packages/source/x/xmldiff/xmldiff-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml >= 3.1.0
Requires:       python-setuptools
Requires:       python-six
Conflicts:      %{oldpython}-xmldiff < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lxml >= 3.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
XMLdiff shows the differences between two similar XML files in the same
way `diff` does with text files. It can also be used as a library or as
a command line tool and can work either with XML files or DOM trees.
The implementation is based on "Change detection in hierarchically
structured information", by S. Chawathe, A. Rajaraman, H.
Garcia-Molina, and J. Widom, Stanford University, 1996.

%prep
%setup -q -n xmldiff-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.rst README.rst README.txt
%license LICENSE.txt
%python3_only %{_bindir}/xmldiff
%python3_only %{_bindir}/xmlpatch
%{python_sitelib}/*

%changelog
