#
# spec file for package python-metaextract
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
Name:           python-metaextract
Version:        1.0.7
Release:        0
Summary:        Module to collect metadata for Python modules
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/toabctl/metaextract
Source:         https://github.com/toabctl/metaextract/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Needed even though no tests are present
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
Requires:       python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(preun):  update-alternatives
%python_subpackages

%description
metaextract is a tool to collect metadata about a python module. For
example, it can determine and collect the dependencies of a sdist
tarball that was retrieved from the Python Package Index.

The tool was first developed in py2pack but is now its own module.

%prep
%setup -q -n metaextract-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/metaextract

%post
%python_install_alternative metaextract

%preun
%python_uninstall_alternative metaextract

%check
%pytest

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/metaextract
%{python_sitelib}/*

%changelog
