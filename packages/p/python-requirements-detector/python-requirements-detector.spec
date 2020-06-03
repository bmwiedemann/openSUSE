#
# spec file for package python-requirements-detector
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
%define         oldpython python
Name:           python-requirements-detector
Version:        0.6
Release:        0
Summary:        Python tool to find and list requirements of a Python project
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/landscapeio/requirements-detector
# https://github.com/landscapeio/requirements-detector/issues/25
Source:         https://github.com/landscapeio/requirements-detector/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astroid >= 1.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astroid}
BuildRequires:  %{python_module pytest}
# /SECTION
%ifpython3
Conflicts:      %{oldpython}-requirements-detector < 0.6
%endif
%python_subpackages

%description
Requirements-detector is a Python tool which attempts to find and list
the requirements of a Python project.

When run from the root of a Python project, it will try to ascertain
which libraries and the versions of those libraries that the project
depends on.

%prep
%setup -q -n requirements-detector-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/detect-requirements
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative detect-requirements

%postun
%python_uninstall_alternative detect-requirements

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/detect-requirements

%changelog
