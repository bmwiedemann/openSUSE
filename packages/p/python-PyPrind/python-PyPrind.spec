#
# spec file for package python-PyPrind
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
Name:           python-PyPrind
Version:        2.11.2
Release:        0
Summary:        Python progress bar and percent indicator utility
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rasbt/pyprind
Source0:        https://files.pythonhosted.org/packages/source/P/PyPrind/PyPrind-%{version}.tar.gz
BuildRequires:  %{python_module psutil >= 3.2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-psutil >= 3.2.0
BuildArch:      noarch
%python_subpackages

%description
The PyPrind (Python Progress Indicator) module provides a progress
bar and a percentage indicator object that let track the progress
of a loop structure or other iterative computation.
A typical application is the processing of large data sets for
which to provide an intuitive estimate at runtime about the
computation progress.

%prep
%setup -q -n PyPrind-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v tests

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
