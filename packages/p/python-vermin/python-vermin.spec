#
# spec file for package python-vermin
#
# Copyright (c) 2026 SUSE LLC
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

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-vermin
Version:        1.8.0
Release:        0
Summary:        Concurrently detect the minimum Python versions needed to run code
License:        MIT
URL:            https://github.com/netromdk/vermin
Source:         https://github.com/netromdk/vermin/archive/refs/tags/v%{version}.tar.gz#/vermin-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 80}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
Concurrently detect the minimum Python versions needed to run code

%prep
%autosetup -p1 -n vermin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/vermin
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i "1s@#!.*python.*@#!$(realpath /usr/bin/python3)@" ./runtests.py
%{python_expand ./runtests.py}

%post
%python_install_alternative vermin

%postun
%python_uninstall_alternative vermin

%files %{python_files}
%doc README.rst
%license LICENSE.txt LICENSE.txt
%python_alternative %{_bindir}/vermin
%{python_sitelib}/vermin
%{python_sitelib}/vermin-%{version}.dist-info

%changelog
