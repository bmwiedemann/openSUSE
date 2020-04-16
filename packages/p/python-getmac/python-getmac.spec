#
# spec file for package python-getmac
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.8.2
Release:        0
Summary:        Module to get MAC addresses of remote hosts and local interfaces
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/GhostofGoes/getmac
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
rm -r *egg-info
find . -type f -exec chmod -x {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.UTF-8
# test_cli_main fails in OBS not local run
# test_cli_multiple_debug_levels  same as above
%pytest tests -k 'not test_get_default_iface_freebsd and not test_cli_main and not test_cli_multiple_debug_levels'

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python3_only %{_bindir}/getmac
%python3_only %{_mandir}/man1/getmac.1*
%{python_sitelib}/getmac*

%changelog
