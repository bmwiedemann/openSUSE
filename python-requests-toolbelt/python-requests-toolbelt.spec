#
# spec file for package python-requests-toolbelt
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
Name:           python-requests-toolbelt
Version:        0.9.1
Release:        0
Summary:        A utility belt for advanced users of python3-requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/requests/toolbelt
Source:         https://files.pythonhosted.org/packages/source/r/requests-toolbelt/requests-toolbelt-%{version}.tar.gz
Patch0:         fix-tests.patch
BuildRequires:  %{python_module requests >= 2.12.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.12.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module betamax >= 0.5.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is just a collection of utilities for `python-requests`_, but don't
really belong in ``requests`` proper. The minimum tested requests version is
``2.1.0``. In reality, the toolbelt should work with ``2.0.1`` as well, but
some idiosyncracies prevent effective or sane testing on that version.

%prep
%setup -q -n requests-toolbelt-%{version}
%patch0 -p1
rm -rf requests_toolbelt.egg-info
# requires network access
rm -v tests/test_multipart_encoder.py

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
%{python_sitelib}/*

%changelog
