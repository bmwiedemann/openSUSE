#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-SecretStorage%{psuffix}
Version:        3.3.3
Release:        0
Summary:        Python bindings to FreeDesktoporg Secret Service API
License:        BSD-3-Clause
URL:            https://github.com/mitya57/secretstorage
Source:         https://files.pythonhosted.org/packages/source/S/SecretStorage/SecretStorage-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Requires:       python-jeepney >= 0.6
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module SecretStorage = %{version}}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module jeepney >= 0.6}
%if %{?suse_version} >= 1550
BuildRequires:  dbus-1-daemon
%endif
BuildRequires:  gnome-keyring
%endif
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
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# gnome-keyring "forgets" to create this directory under certain conditions
mkdir -p $HOME/.cache
%python_expand dbus-run-session -- $python -m unittest discover -s tests
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc changelog README.rst
%{python_sitelib}/*
%endif

%changelog
