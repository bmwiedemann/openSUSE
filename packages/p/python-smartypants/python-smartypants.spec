#
# spec file for package python-smartypants
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-smartypants
Version:        2.0.1
Release:        0
Summary:        Python fork of perl SmartyPants
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/leohemsted/smartypants.py
Source:         https://github.com/leohemsted/smartypants.py/archive/v%{version}.tar.gz#/smartypants-%{version}.tar.gz
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
smartypants is a Python implementation of the perl SmartyPants,
which translates plain ASCII punctuation characters into smart
typographic punctuation HTML entities.

%prep
%setup -q -n smartypants.py-%{version}

%build
%python_build

%install
%python_install
%{python_expand sed -i '1{/^#!/d}' %{buildroot}%{$python_sitelib}/smartypants.py
%fdupes %{buildroot}%{$python_sitelib}
}
%python_clone -a %{buildroot}%{_bindir}/smartypants

%post
%python_install_alternative smartypants

%postun
%python_uninstall_alternative smartypants

%check
%python_exec setup.py test

%files %{python_files}
%license COPYING
%doc README.rst docs/*.rst
%python_alternative %{_bindir}/smartypants
%{python_sitelib}/*

%changelog
