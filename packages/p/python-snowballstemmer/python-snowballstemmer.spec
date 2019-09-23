#
# spec file for package python-snowballstemmer
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-snowballstemmer
Version:        1.9.1
Release:        0
Summary:        16 stemmer algorithms
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/shibukawa/snowball_py
Source:         https://files.pythonhosted.org/packages/source/s/snowballstemmer/snowballstemmer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package provides 16 stemmer algorithms (15 + Poerter English
stemmer) generated from Snowball algorithms.  It includes following
language algorithms: Danish, Dutch, English (Standard, Porter),
Finnish, French, German, Hungarian, Italian, Norwegian, Portuguese,
Romanian, Russian, Spanish, Swedish, Turkish. This is a pure Python
stemming library. If PyStemmer is available, this module uses it to
accelerate.

%prep
%setup -q -n snowballstemmer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*
%doc README.rst
%license COPYING

%changelog
