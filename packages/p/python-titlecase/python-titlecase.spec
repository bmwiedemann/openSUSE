#
# spec file for package python-titlecase
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
Name:           python-titlecase
Version:        0.12.0
Release:        0
Summary:        Python library to capitalize strings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ppannuto/python-titlecase
Source:         https://files.pythonhosted.org/packages/source/t/titlecase/titlecase-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nose >= 1.0}
# /SECTION
%python_subpackages

%description
This filter changes all words to Title Caps, and attempts to be
clever about SMALL words like a/an/the in the input.

The list of "SMALL words" which are not capped comes from the New
York Times Manual of Style, plus some others like 'vs' and 'v'.

%prep
%setup -q -n titlecase-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/titlecase
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative titlecase

%postun
%python_uninstall_alternative titlecase

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/titlecase
%{python_sitelib}/*

%changelog
