#
# spec file for package python-expiringdict
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-expiringdict
Version:        1.2.2
Release:        0
Summary:        Dictionary with auto-expiring values for caching purposes
License:        Apache-2.0
URL:            https://www.mailgun.com/
Source:         https://github.com/mailgun/expiringdict/archive/refs/tags/v%{version}.tar.gz#/expiringdict-%{version}.tar.gz
Patch0:         remove-nose.patch
BuildRequires:  %{python_module dill}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dill
Requires:       python-typing
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The core of the library is ExpiringDict class which is an ordered
dictionary with auto-expiring values for caching purposes.
Expiration happens on any access, object is locked during cleanup
from expired values. ExpiringDict can not store more than
max_len elements - the oldest will be deleted.

%prep
%setup -q -n expiringdict-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/expiringdict*

%changelog
