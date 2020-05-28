#
# spec file for package python-acefile
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-acefile
Version:        0.6.12
Release:        0
Summary:        ACE 1.0 and 2.0 archive reader/extractor in pure Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://www.roe.ch/acefile
Source:         https://files.pythonhosted.org/packages/source/a/acefile/acefile-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Read/test/extract ACE 1.0 and 2.0 archives in pure python.

%prep
%setup -q -n acefile-%{version}
sed -i '1 {/^#!/d}' acefile.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/acefile-unace
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative acefile-unace

%postun
%python_uninstall_alternative acefile-unace

%files %{python_files}
%doc NEWS.md README.md
%license LICENSE.md
%python_alternative %{_bindir}/acefile-unace
%{python_sitearch}/*

%check
# no testsuite found

%changelog
