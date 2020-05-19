#
# spec file for package python-wakeonlan
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-wakeonlan
Version:        1.1.6
Release:        0
Summary:        A small python module for wake on lan
License:        WTFPL
Group:          Development/Languages/Python
URL:            https://github.com/remcohaszing/pywakeonlan
Source:         https://files.pythonhosted.org/packages/source/w/wakeonlan/wakeonlan-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm >= 1.15.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A small python module for wake on lan.

%prep
%setup -q -n wakeonlan-%{version}
sed -i -e 's:~=:>=:g' setup.py

%build
export LANG=en_US.UTF8
%python_build

%install
export LANG=en_US.UTF8
%python_install
%python_clone -a %{buildroot}%{_bindir}/wakeonlan
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
export LANG=en_US.UTF8
%pytest

%post
%python_install_alternative wakeonlan

%postun
%python_uninstall_alternative wakeonlan

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/wakeonlan
%{python_sitelib}/*

%changelog
