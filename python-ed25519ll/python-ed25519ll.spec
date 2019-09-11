#
# spec file for package python-ed25519ll
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define modname ed25519ll
%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        0.6
Release:        0
Summary:        A low-level ctypes wrapper for Ed25519 digital signatures
License:        MIT
Group:          Development/Languages/Python
URL:            http://bitbucket.org/dholth/%{modname}/
Source:         https://files.pythonhosted.org/packages/source/e/ed25519ll/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
# Test requirements:
BuildRequires:  %{python_module nose}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Ed25519 is a public-key signature system with several attractive features
including:

* Fast single-signature verification.
* Very fast signing.
* Fast key generation.
* High security level.
* Small signatures. Signatures fit into 64 bytes.
* Small keys. Public keys consume only 32 bytes.

This text abridged from http://ed25519.cr.yp.to/.

%prep
%setup -q -n %{modname}-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.txt CHANGES.txt
%{python_sitearch}/*

%changelog
