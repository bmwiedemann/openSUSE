#
# spec file for package python
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global modname signedjson
Name:           python-%{modname}
Version:        1.0.0
Release:        0
Summary:        Python module to sign JSON with Ed25519 signatures
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/matrix-org/%{name}
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Features:

* More than one entity can sign the same object.
* Each entity can sign the object with more than one key making it easier to
  rotate keys
* ED25519 can be replaced with a different algorithm.
* Unprotected data can be added to the object under the "unsigned" key.

%prep
%setup -q

%build

%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{modname}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
