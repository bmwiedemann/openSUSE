#
# spec file for package python-livereload
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-livereload
Version:        2.6.3
Release:        0
Summary:        Livereload server in python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://livereload.readthedocs.io/en/latest/
Source:         https://github.com/lepture/python-livereload/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       python-tornado
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Reload webpages on changes, without hitting refresh in your browser.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/livereload

%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
# https://github.com/lepture/python-livereload/issues/200
%pytest -k 'not test_watch_multiple_dirs'

%post
%python_install_alternative livereload

%postun
%python_uninstall_alternative livereload

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/livereload
%{python_sitelib}/livereload/
%{python_sitelib}/livereload-%{version}-py%{python_version}.egg-info

%changelog
