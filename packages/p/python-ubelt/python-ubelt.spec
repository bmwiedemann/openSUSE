#
# spec file for package python-ubelt
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


%{?sle15_python_module_pythons}
Name:           python-ubelt
Version:        1.3.7
Release:        0
Summary:        Python utility belt containing simple tools
License:        Apache-2.0
URL:            https://github.com/Erotemic/ubelt
Source:         https://github.com/Erotemic/ubelt/archive/refs/tags/v%{version}.tar.gz#/ubelt-%{version}-gh.tar.gz
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools >= 41.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xdoctest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python utility belt containing simple tools, a stdlib like feel, and extra batteries

%prep
%autosetup -p1 -n ubelt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/ubelt
%{python_sitelib}/ubelt-%{version}.dist-info

%changelog
