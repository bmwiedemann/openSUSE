#
# spec file for package python-queuelib
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-queuelib
Version:        1.7.0
Release:        0
Summary:        Collection of Persistent (Disk-Based) Queues
License:        BSD-2-Clause
URL:            https://github.com/scrapy/queuelib
Source:         https://files.pythonhosted.org/packages/source/q/queuelib/queuelib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Queuelib is a collection of persistent (disk-based) queues for Python.

Queuelib goals are speed and simplicity. It was originally part of the
`Scrapy framework`_ and stripped out on its own library.

%prep
%setup -q -n queuelib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst NEWS
%license LICENSE
%{python_sitelib}/*

%changelog
