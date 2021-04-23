#
# spec file for package python-identify
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
Name:           python-identify
Version:        1.4.14
Release:        0
Summary:        File identification library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/chriskuehl/identify
Source:         https://github.com/chriskuehl/identify/archive/v%{version}.tar.gz#/identify-%{version}.tar.gz
BuildRequires:  %{python_module editdistance}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-editdistance
BuildArch:      noarch
%python_subpackages

%description
File identification library for Python, including license file SPDX identifier.

%prep
%setup -q -n identify-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/identify-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py pytest

%post
%python_install_alternative identify-cli

%postun
%python_uninstall_alternative identify-cli

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/identify-cli
%{python_sitelib}/*

%changelog
