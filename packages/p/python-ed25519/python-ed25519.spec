#
# spec file for package python-ed25519
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
Name:           python-ed25519
Version:        1.5
Release:        0
Summary:        Python bindings to the Ed25519 public-key signature system
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/warner/python-ed25519
Source:         https://files.pythonhosted.org/packages/source/e/ed25519/ed25519-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Python bindings to the Ed25519 public-key signature system.

%prep
%setup -q -n ed25519-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/edsig
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%post
%python_install_alternative edsig

%postun
%python_uninstall_alternative edsig

%files %{python_files}
%doc NEWS README.md
%license LICENSE
%python_alternative %{_bindir}/edsig
%{python_sitearch}/*

%changelog
