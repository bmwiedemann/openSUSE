#
# spec file for package python-peppercorn
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 LISA GmbH, Bingen, Germany.
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
Name:           python-peppercorn
Version:        0.6
Release:        0
Summary:        Pyramid exceptions logger
License:        BSD-4-Clause AND ZPL-2.1 AND MIT
URL:            https://docs.pylonsproject.org/projects/peppercorn/en/latest/
Source:         https://files.pythonhosted.org/packages/source/p/peppercorn/peppercorn-%{version}.tar.gz
# Testing requirements:
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pylons-sphinx-themes}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Documentation requirements:
BuildRequires:  python3-Sphinx
BuildArch:      noarch
%python_subpackages

%description
A library for converting a token stream into a data structure comprised of
sequences, mappings, and scalars, developed primarily for converting HTTP form
POST data into a richer data structure.

Please see the -doc package or
http://docs.pylonsproject.org/projects/peppercorn/en/latest/ for the
documentation.

%package -n %{name}-doc
Summary:        Documentation for Pyramid exceptions logger

%description -n %{name}-doc
This package contains documentation for %{name}.

%prep
%setup -q -n peppercorn-%{version}

%build
%python_build
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py nosetests --with-coverage

%files %{python_files}
%if 0%{?leap_version} >= 420200 || 0%{?suse_version} > 1320
%license LICENSE.txt
%else
%license LICENSE.txt
%endif
%doc CHANGES.rst CONTRIBUTORS.txt COPYRIGHT.txt README.rst contributing.md
%{python_sitelib}/*

%files -n %{name}-doc
%doc build/sphinx/html

%changelog
