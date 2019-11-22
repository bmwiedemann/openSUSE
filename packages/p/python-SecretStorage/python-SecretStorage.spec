#
# spec file for package python-SecretStorage
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
Name:           python-SecretStorage
Version:        2.3.1
Release:        0
Summary:        Python bindings to FreeDesktoporg Secret Service API
License:        BSD-3-Clause
URL:            https://github.com/mitya57/secretstorage
Source:         https://files.pythonhosted.org/packages/source/S/SecretStorage/SecretStorage-%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dbus-1-x11
BuildRequires:  fdupes
BuildRequires:  gnome-keyring
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Requires:       python-dbus-python
BuildArch:      noarch
%python_subpackages

%description
This module provides a way for securely storing passwords and other secrets.

It uses D-Bus `Secret Service`_ API that is supported by GNOME Keyring
(since version 2.30) and KSecretsService.

The main classes provided are ``secretstorage.Item``, representing a secret
item (that has a *label*, a *secret* and some *attributes*) and
``secretstorage.Collection``, a place items are stored in.

SecretStorage supports most of the functions provided by Secret Service,
including creating and deleting items and collections, editing items,
locking and unlocking collections (asynchronous unlocking is also supported).

The documentation can be found on `pythonhosted.org`_.

.. _`Secret Service`: https://specifications.freedesktop.org/secret-service/
.. _`pythonhosted.org`: https://pythonhosted.org/SecretStorage/

%prep
%setup -q -n SecretStorage-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gnome-keyring "forgets" to create this directory under certain conditions
mkdir -p $HOME/.cache
%python_expand dbus-run-session -- $python -m unittest discover -s tests

%files %{python_files}
%license LICENSE
%doc changelog README.rst
%{python_sitelib}/*

%changelog
