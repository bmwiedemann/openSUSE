#
# spec file for package python-portpicker
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
Name:           python-portpicker
Version:        1.3.1
Release:        0
Summary:        A library to choose unique available network ports
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/google/python_portpicker
Source0:        https://files.pythonhosted.org/packages/source/p/portpicker/portpicker-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
# /SECTION
%python_subpackages

%description
Portpicker provides an API to find and return an available network port for
an application to bind to. Ideally suited for use from unittests or for test
harnesses that launch local servers.

%prep
%setup -q -n portpicker-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/portserver.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python src/tests/portpicker_test.py

%post
%python_install_alternative portserver.py

%postun
%python_uninstall_alternative portserver.py

%files %{python_files}
%license LICENSE
%doc CONTRIBUTING.md README.md
%{python_sitelib}/*
# import asyncio
%python_alternative %{_bindir}/portserver.py

%changelog
