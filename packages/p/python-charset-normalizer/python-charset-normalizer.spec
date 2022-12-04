#
# spec file for package python-charset-normalizer
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-charset-normalizer
Version:        3.0.1
Release:        0
Summary:        Python Universal Charset detector
License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source:         https://github.com/Ousret/charset_normalizer/archive/refs/tags/%{version}.tar.gz#/charset_normalizer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       python-unicodedata2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python Universal Charset detector.

%prep
%setup -q -n charset_normalizer-%{version}
# remove code coverage flags from pytest
sed -i '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/normalizer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative normalizer

%postun
%python_uninstall_alternative normalizer

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/normalizer
%{python_sitelib}/charset_normalizer
%{python_sitelib}/charset_normalizer-%{version}*-info

%changelog
