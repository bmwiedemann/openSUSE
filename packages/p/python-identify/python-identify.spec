#
# spec file for package python-identify
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
Name:           python-identify
Version:        2.6.3
Release:        0
Summary:        File identification library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pre-commit/identify
Source:         https://github.com/pre-commit/identify/archive/v%{version}.tar.gz#/identify-%{version}.tar.gz
# PATCH-FIX-OPENSUSE 0001-use-editdistance-not-ukkonen.patch -- ukkonen not packaged for opensuse now
Patch1:         0001-use-editdistance-not-ukkonen.patch
BuildRequires:  %{python_module editdistance}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-editdistance
BuildArch:      noarch
%python_subpackages

%description
File identification library for Python, including license file SPDX identifier.

%prep
%setup -q -n identify-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/identify-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative identify-cli

%postun
%python_uninstall_alternative identify-cli

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/identify-cli
%{python_sitelib}/identify
%{python_sitelib}/identify-%{version}-*-info

%changelog
