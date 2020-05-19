#
# spec file for package python-topy
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
Name:           python-topy
Version:        0.2.2
Release:        0
Summary:        Tool for fixing typos in text using regular expressions
License:        MIT AND CC-BY-SA-4.0
Group:          Development/Languages/Python
URL:            https://github.com/intgr/topy
Source:         https://github.com/intgr/topy/archive/v0.2.2.tar.gz#/topy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-regex >= 2016.07.14
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module regex >= 2016.07.14}
# /SECTION
%python_subpackages

%description
A tool for fixing typos in text using regular expressions,
based on RegExTypoFix from Wikipedia.

%prep
%setup -q -n topy-%{version}
sed -i '1 { /^#!/ d }' topy/topy.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/topy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%post
%python_install_alternative topy

%postun
%python_uninstall_alternative topy

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/topy
%{python_sitelib}/*

%changelog
