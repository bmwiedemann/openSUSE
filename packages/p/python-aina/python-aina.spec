#
# spec file for package python-aina
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
%define skip_python2 1
Name:           python-aina
Version:        0.1.3
Release:        0
Summary:        A general-purpose stream processing framework
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/ilovetux/aina
Source:         https://github.com/iLoveTux/aina/archive/%{version}.tar.gz#/aina-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base >= 3.5
Requires:       python-click >= 6.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 6.0}
# /SECTION
%python_subpackages

%description
Aina is a general-purpose stream processing framework. It includes a
templating system which powers a command line utility.

%prep
%setup -q -n aina-%{version}
dos2unix AUTHORS.rst README.rst

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/aina
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python setup.py test

%post
%python_install_alternative aina

%postun
%python_uninstall_alternative aina

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/aina
%{python_sitelib}/*

%changelog
