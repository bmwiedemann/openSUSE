#
# spec file for package python-stem
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
Name:           python-stem
Version:        1.8.0
Release:        0
Summary:        Python controller library for Tor
License:        LGPL-3.0-only
URL:            https://stem.torproject.org/
Source:         https://files.pythonhosted.org/packages/source/s/stem/stem-%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
Requires:       python
Requires:       python-cryptography
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Stem is a Python controller library that allows applications
to interact with Tor (https://www.torproject.org/).

%prep
%setup -q -n stem-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/tor-prompt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec run_tests.py -u

%post
%python_install_alternative tor-prompt

%postun
%python_uninstall_alternative tor-prompt

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/tor-prompt
%{python_sitelib}/*

%changelog
