#
# spec file for package python-gpgme
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Neal Gompa <ngompa13@gmail.com>.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-gpgme
Version:        0.3
Release:        0
Summary:        A Python module for working with OpenPGP messages
License:        LGPL-2.1+
Group:          Development/Libraries/Python
Url:            http://pypi.python.org/pypi/pygpgme
Source:         pygpgme-%{version}.tar.gz
# Upstream is dead, but Fedora maintains a fork
# All patches tracked at: https://pagure.io/pygpgme
# Patches for working with gnupg >= 2.1
Patch0001:      0001-reflect-2.1-reporting-for-key-imports.patch
Patch0002:      0002-passphrase_cb-is-deprecated.patch
Patch0003:      0003-handle-generic-error-when-no-passphrase-callback-pre.patch
Patch0004:      0004-add-pubkey_algo-and-hash_algo-attributes-to-signatur.patch
Patch0005:      0005-add-ENCRYPT_NO_ENCRYPT_TO-constant.patch
Patch0006:      0006-ignore-STATUS_KEY_CONSIDERED-when-editing.patch
BuildRequires:  %{python_module devel}
BuildRequires:  gpgme-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and
decrypt messages using the OpenPGP format.

It is built on top of the GNU Privacy Guard and the GPGME library.

%prep
%setup -q -n pygpgme-%{version}
%if 0%{?suse_version} >= 1330
%autopatch -p1
%endif

%build
%python_build

%install
%python_install

%files %{python_files}
%doc README examples tests
%{python_sitearch}/*

%changelog
