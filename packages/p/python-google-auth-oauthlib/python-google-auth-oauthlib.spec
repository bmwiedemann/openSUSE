#
# spec file for package python-google-auth-oauthlib
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
%bcond_without python2
Name:           python-google-auth-oauthlib
Version:        0.8.0
Release:        0
Summary:        Google authentication library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-auth-library-python-oauthlib
Source:         https://files.pythonhosted.org/packages/source/g/google-auth-oauthlib/google-auth-oauthlib-%{version}.tar.gz
# https://github.com/googleapis/google-auth-library-python-oauthlib/issues/207
Patch0:         python-google-auth-oauthlib-no-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 2.14.0
Requires:       python-requests-oauthlib >= 0.7.0
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-click
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 6.0.0}
BuildRequires:  %{python_module google-auth >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-oauthlib >= 0.7.0}
BuildRequires:  %{python_module six}
%if %{with python2}
BuildRequires:  python-futures
%endif
# /SECTION
%ifpython2
Requires:       python-futures
%endif
%python_subpackages

%description
This library provides oauthlib integration with google-auth.

%prep
%setup -q -n google-auth-oauthlib-%{version}
%patch0 -p1
rm -rf tests/__pycache__/
rm -rf tests/*.pyc

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/google-oauthlib-tool
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative google-oauthlib-tool

%postun
%python_uninstall_alternative google-oauthlib-tool

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/google-oauthlib-tool
%{python_sitelib}/*

%changelog
