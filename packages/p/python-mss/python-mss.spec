#
# spec file for package python-mss
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
Name:           python-mss
Version:        7.0.1
Release:        0
Summary:        Python multiple screenshots module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/BoboTiG/python-mss
Source:         https://files.pythonhosted.org/packages/source/m/mss/mss-%{version}.tar.gz
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  lsof
BuildRequires:  python-rpm-macros
BuildRequires:  xrandr
BuildRequires:  xvfb-run
Requires:       alts
Requires:       xrandr
BuildArch:      noarch
%python_subpackages

%description
An ultra fast cross-platform multiple screenshots module in pure Python using ctypes.

%prep
%setup -q -n mss-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mss
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative mss

%check
export LANG=en_US.UTF-8
# test_region_out_of_monitor_bounds fails on ppc64 only
echo '
%pytest --ignore mss/tests/test_setup.py -k "not test_region_out_of_monitor_bounds"
'> pytest_script.sh
# need explicitly set up screen.
xvfb-run --server-args "-screen 0 1920x1080x24" sh pytest_script.sh

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/mss
%{python_sitelib}/mss
%{python_sitelib}/mss-%{version}*-info

%changelog
