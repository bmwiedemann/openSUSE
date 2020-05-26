#
# spec file for package python-o2sclpy
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
Name:           python-o2sclpy
Version:        0.924
Release:        0
Summary:        Python extensions for O2scl
License:        GPL-3.0-only
URL:            https://neutronstars.utk.edu/code/o2sclpy
Source0:        https://files.pythonhosted.org/packages/source/o/o2sclpy/o2sclpy-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/awsteiner/o2sclpy/master/LICENSE
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module matplotlib >= 3.1}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       o2scl-devel
Requires:       python-h5py
Requires:       python-matplotlib >= 3.1
Requires:       python-numpy
Requires:       python-requests
Requires:       texlive-latex
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python extensions for O2scl

%prep
%setup -q -n o2sclpy-%{version}
cp %{SOURCE1} ./

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/o2graph
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative o2graph

%postun
%python_uninstall_alternative o2graph

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/o2graph
%{python_sitelib}/*

%changelog
