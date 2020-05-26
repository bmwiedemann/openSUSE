#
# spec file for package python-jsondiff
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
Name:           python-jsondiff
Version:        1.2.0
Release:        0
Summary:        Module to diff JSON and JSON-like structures in Python
License:        MIT
URL:            https://github.com/ZoomerAnalytics/jsondiff
Source:         https://files.pythonhosted.org/packages/source/j/jsondiff/jsondiff-%{version}.tar.gz
BuildRequires:  %{python_module nose-random}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Package to show differences between JSON and JSON-like structures in Python

%prep
%setup -q -n jsondiff-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/jsondiff
%python_clone -a %{buildroot}%{_bindir}/jdiff
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix}

%post
%python_install_alternative jsondiff
%python_install_alternative jdiff

%postun
%python_uninstall_alternative jsondiff
%python_uninstall_alternative jdiff

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/jdiff
%python_alternative %{_bindir}/jsondiff

%changelog
