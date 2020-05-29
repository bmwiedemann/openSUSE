#
# spec file for package python-psautohint
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
Name:           python-psautohint
Version:        2.0.1
Release:        0
Summary:        Python wrapper for Adobe's PostScript autohinter
License:        Apache-2.0
URL:            https://github.com/adobe-type-tools/psautohint
Source:         https://files.pythonhosted.org/packages/source/p/psautohint/psautohint-%{version}.zip
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 4.5.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 4.5.0}
BuildRequires:  %{python_module pytest >= 3.0}
# /SECTION
%python_subpackages

%description
Python wrapper for Adobe's PostScript autohinter

%prep
%setup -q -n psautohint-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%python_clone -a %{buildroot}%{_bindir}/psautohint
%python_clone -a %{buildroot}%{_bindir}/psstemhist
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch tests/unittests

%post
%python_install_alternative psautohint psstemhist

%postun
%python_uninstall_alternative psautohint psstemhist

%files %{python_files}
%doc NEWS.md README.md
%license COPYING LICENSE
%python_alternative %{_bindir}/psautohint
%python_alternative %{_bindir}/psstemhist
%{python_sitearch}/*

%changelog
