#
# spec file for package python-pyp
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020-2021 LISA GmbH, Bingen, Germany
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
Name:           python-pyp
Version:        0.3.4
Release:        0
Summary:        Python at the shell
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/hauntsaninja/pyp
Source0:        https://github.com/hauntsaninja/pyp/archive/v%{version}.tar.gz#/pyp-%{version}.tar.gz
BuildRequires:  %{python_module astunparse}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# testing requirements
BuildRequires:  bc
BuildRequires:  jq
BuildRequires:  %{python_module pytest}
Requires:       python-astunparse
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Easily run Python at the shell! Magical, but never mysterious.

See README.md or https://github.com/hauntsaninja/pyp for examples.

%prep
%setup -q -n pyp-%{version}
sed -i '/^#!\//, 1d' pyp.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH=$(pwd):$PATH
%{python_expand ln -sf %{buildroot}%{_bindir}/pyp-%{$python_bin_suffix} pyp
PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -vv #k 'not test_tracebacks'
}

%post
%python_install_alternative pyp

%postun
%python_uninstall_alternative pyp

%files %{python_files}
%license LICENSE
%doc *.md
%{python_sitelib}/
%python_alternative %{_bindir}/pyp

%changelog
