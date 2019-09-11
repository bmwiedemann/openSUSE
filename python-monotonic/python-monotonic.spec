#
# spec file for package python-monotonic
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
Name:           python-monotonic
Version:        1.5
Release:        0
Summary:        An implementation of time.monotonic() for Python 2 & < 33
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/atdt/monotonic
Source:         https://files.pythonhosted.org/packages/source/m/monotonic/monotonic-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif
%python_subpackages

%description
This module provides a ``monotonic()`` function which returns the
value (in fractional seconds) of a clock which never goes backwards.

%prep
%setup -q -n monotonic-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
