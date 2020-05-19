#
# spec file for package python-pyannotate
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
Name:           python-pyannotate
Version:        1.2.0
Release:        0
Summary:        PyAnnotate: Auto-generate PEP-484 annotations
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/dropbox/pyannotate
Source:         https://github.com/dropbox/pyannotate/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 28.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mypy_extensions
Requires:       python-six >= 1.11.0
Requires:       python-typing
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mypy_extensions}
BuildRequires:  %{python_module pytest => 3.3.0}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  %{python_module typing}
BuildRequires:  python3-testsuite
# /SECTION
%python_subpackages

%description
This module inserts annotations into source code based on call
arguments and return types observed at runtime.

%prep
%setup -q -n pyannotate-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyannotate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pyannotate

%postun
%python_uninstall_alternative pyannotate

%files %{python_files}
%doc README.md example/
%license LICENSE
%python_alternative %{_bindir}/pyannotate
%{python_sitelib}/*

%changelog
