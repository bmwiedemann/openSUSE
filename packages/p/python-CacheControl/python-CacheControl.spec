#
# spec file for package python-CacheControl
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-CacheControl
Version:        0.12.6
Release:        0
Summary:        Caching library for Python requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ionrock/cachecontrol
Source:         https://github.com/ionrock/cachecontrol/archive/v%{version}.tar.gz#/CacheControl-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-lockfile >= 0.9
Suggests:       python-redis >= 2.10.5
BuildArch:      noarch
# SECTION test requirements
## cherrypy is python3 only from 18.x series
BuildRequires:  python3-CherryPy
BuildRequires:  python3-lockfile >= 0.9
BuildRequires:  python3-mock
BuildRequires:  python3-msgpack
BuildRequires:  python3-pytest
BuildRequires:  python3-redis >= 2.10.5
BuildRequires:  python3-requests
# /SECTION
%python_subpackages

%description
CacheControl is a port of the caching algorithms in httplib2 for use with
requests session object.

%prep
%setup -q -n cachecontrol-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/doesitcache
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_file_cache_recognizes_consumed_file_handle uses httpbin.org directly
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_bin_suffix} -v -k 'not test_file_cache_recognizes_consumed_file_handle'

%post
%python_install_alternative doesitcache

%postun
%python_uninstall_alternative doesitcache

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/doesitcache
%{python_sitelib}/*

%changelog
