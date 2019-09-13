#
# spec file for package python-capturer
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with     test
Name:           python-capturer
Version:        2.4
Release:        0
Summary:        Python module for capturing stdout/stderr of the current process group
License:        MIT
Group:          Development/Languages/Python
Url:            https://capturer.readthedocs.io
Source:         https://files.pythonhosted.org/packages/source/c/capturer/capturer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module humanfriendly >= 2.1}
%endif
Requires:       python-humanfriendly >= 2.1
BuildArch:      noarch

%python_subpackages

%description
The capturer package captures the stdout and stderr streams
of the current process *and subprocesses*. Output can be relayed to the
terminal in real time, but is also available to the Python program for
additional processing. It's currently tested on cPython 2.6, 2.7, 3.4, 3.5, 3.6
and PyPy (2.7). It's tested on Linux and Mac OS X and may work on other unixes
but definitely won't work on Windows (due to the use of the platform dependent
"pty" module).

%prep
%setup -q -n capturer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
