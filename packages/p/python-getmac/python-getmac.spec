#
# spec file for package python-getmac
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


Name:           python-getmac
Version:        0.9.5
Release:        0
Summary:        Module to get MAC addresses of remote hosts and local interfaces
License:        MIT
URL:            https://github.com/GhostofGoes/getmac
Source:         https://files.pythonhosted.org/packages/source/g/getmac/getmac-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch0:         cope-with-no-ip6.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python module to get MAC addresses of remote hosts and local interfaces.

%prep
%autosetup -p1 -n getmac-%{version}
sed -i "1,4{/\/usr\/bin\/env/d}" getmac/__main__.py
rm -r *egg-info
find . -type f -exec chmod -x {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/getmac
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.UTF-8
# test_cli_main fails in OBS not local run
# test_cli_multiple_debug_levels  same as above
%pytest tests -k 'not test_cli_main and not test_cli_multiple_debug_levels'

%post
%python_install_alternative getmac

%postun
%python_uninstall_alternative getmac

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/getmac
%{python_sitelib}/getmac
%{python_sitelib}/getmac-%{version}.dist-info

%changelog
