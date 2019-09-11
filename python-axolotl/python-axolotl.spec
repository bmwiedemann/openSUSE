#
# spec file for package python-axolotl
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
Name:           python-axolotl
Version:        0.2.3
Release:        0
Summary:        Python port of libaxolotl-android
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/tgalal/python-axolotl
Source:         https://github.com/tgalal/python-axolotl/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-axolotl-curve25519 >= 0.4.1
Requires:       python-cryptography
Requires:       python-protobuf >= 3.0.0.b2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module axolotl-curve25519 >= 0.4.1}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module protobuf >= 3.0.0.b2}
# /SECTION
%python_subpackages

%description
This is a Python port of libsignal-protocol-java, originally written by Moxie
Marlinspike.

%prep
%setup -q -n python-axolotl-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
