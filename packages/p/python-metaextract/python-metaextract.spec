#
# spec file for package python-metaextract
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


%{?sle15_python_module_pythons}
Name:           python-metaextract
Version:        1.0.9
Release:        0
Summary:        Module to collect metadata for Python modules
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/toabctl/metaextract
Source:         https://github.com/toabctl/metaextract/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM tests-tests_require.patch gh#toabctl/metaextract#20 mcepl@suse.com
# Fix failing tests
Patch0:         tests-tests_require.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Needed even though no tests are present
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest}
Requires:       python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
metaextract is a tool to collect metadata about a python module. For
example, it can determine and collect the dependencies of a sdist
tarball that was retrieved from the Python Package Index.

The tool was first developed in py2pack but is now its own module.

%prep
%autosetup -p1 -n metaextract-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/metaextract

%post
%python_install_alternative metaextract

%postun
%python_uninstall_alternative metaextract

%check
%pytest

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/metaextract
%{python_sitelib}/metaextract
%{python_sitelib}/metaextract-%{version}*-info

%changelog
