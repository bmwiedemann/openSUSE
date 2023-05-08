#
# spec file for package python-CacheControl
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


%{?sle15_python_module_pythons}
Name:           python-CacheControl
Version:        0.12.11
Release:        0
Summary:        Caching library for Python requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ionrock/cachecontrol
Source:         https://github.com/ionrock/cachecontrol/archive/v%{version}.tar.gz#/CacheControl-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack >= 0.5.2
Requires:       python-requests
Provides:       python-cachecontrol = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-lockfile >= 0.9
Suggests:       python-redis >= 2.10.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module CherryPy}
BuildRequires:  %{python_module lockfile >= 0.9}
BuildRequires:  %{python_module msgpack >= 0.5.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis >= 2.10.5}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
CacheControl is a port of the caching algorithms in httplib2 for use with
requests session object.

%prep
%setup -q -n cachecontrol-%{version}
sed -i -e 's/^from mock/from unittest.mock/' -e 's/^import mock/from unittest import mock/' tests/*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/doesitcache
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_file_cache_recognizes_consumed_file_handle uses httpbin.org directly
%pytest -v -k 'not test_file_cache_recognizes_consumed_file_handle'

%post
%python_install_alternative doesitcache

%postun
%python_uninstall_alternative doesitcache

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/doesitcache
%{python_sitelib}/cachecontrol
%{python_sitelib}/CacheControl-%{version}*-info

%changelog
