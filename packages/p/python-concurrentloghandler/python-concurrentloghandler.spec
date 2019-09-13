#
# spec file for package python-concurrentloghandler
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define modname ConcurrentLogHandler
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-concurrentloghandler
Version:        0.9.1
Release:        0
Summary:        Concurrent logging handler
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            http://pypi.python.org/pypi/ConcurrentLogHandler
Source:         https://files.pythonhosted.org/packages/source/C/ConcurrentLogHandler/%{modname}-%{version}.tar.gz
Patch0:         %{modname}-0.9.1-testpath.patch
BuildRequires:  %{python_module portalocker}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sed
BuildArch:      noarch
%python_subpackages

%description
This module provides an additional log handler for Python's
standard logging package (PEP 282). This handler will write log
events to log file which is rotated when the log file reaches
a certain size. Multiple processes can safely write to the same
log file concurrently.

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1
rm -v src/portalocker.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} sh run_tests.sh $python }

%files %{python_files}
%license LICENSE
%doc README
%{python_sitelib}/*

%changelog
