#
# spec file for package python-charset-normalizer
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
%define skip_python2 1
Name:           python-charset-normalizer
Version:        1.3.4
Release:        0
Summary:        Python Universal Charset detector
License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source:         https://github.com/Ousret/charset_normalizer/archive/%{version}.tar.gz#/charset_normalizer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable
Requires:       python-cached-property
Requires:       python-dragonmapper
Requires:       python-loguru
Requires:       python-zhon
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-requests
Suggests:       python-requests-html
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PrettyTable}
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module dragonmapper}
BuildRequires:  %{python_module loguru}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module zhon}
# /SECTION
%python_subpackages

%description
Python Universal Charset detector.

%prep
%setup -q -n charset_normalizer-%{version}
dos2unix README.md

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/normalizer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py pytest

%post
%python_install_alternative normalizer

%postun
%python_uninstall_alternative normalizer

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/normalizer
%{python_sitelib}/*

%changelog
