#
# spec file for package python-getmac
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-getmac
Version:        0.8.1
Release:        0
Summary:        Module to get MAC addresses of remote hosts and local interfaces
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/GhostofGoes/getmac
Source:         https://files.pythonhosted.org/packages/source/g/getmac/getmac-%{version}.tar.gz
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
A Python module to get MAC addresses of remote hosts and local interfaces.

%prep
%setup -q -n getmac-%{version}
sed -i "1,4{/\/usr\/bin\/env/d}" getmac/__main__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.UTF-8
%python_exec -m pytest tests -k 'not test_darwin_remote and not test_cli_main_basic and not test_cli_main_verbose and not test_cli_main_debug and not test_cli_multiple_debug_levels'

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python3_only %{_bindir}/getmac
%python3_only %doc %{_mandir}/man1/getmac.1*
%{python_sitelib}/getmac*

%changelog
