#
# spec file for package python-CacheControl
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.14.1
Release:        0
Summary:        Caching library for Python requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/psf/cachecontrol
Source:         https://github.com/psf/cachecontrol/archive/v%{version}.tar.gz#/cachecontrol-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack >= 0.5.2
Requires:       python-requests >= 2.16.0
Provides:       python-cachecontrol = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-filelock >= 3.8.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module CherryPy}
BuildRequires:  %{python_module filelock >= 3.8.0}
BuildRequires:  %{python_module msgpack >= 0.5.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.16.0}
# /SECTION
%python_subpackages

%description
CacheControl is a port of the caching algorithms in httplib2 for use with
requests session object.

%prep
%autosetup -p1 -n cachecontrol-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# do not pack tests
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

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
%{python_sitelib}/cachecontrol-%{version}*-info

%changelog
