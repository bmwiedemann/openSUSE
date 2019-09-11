#
# spec file for package python-google-auth-oauthlib
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-google-auth-oauthlib
Version:        0.3.0
Release:        0
License:        Apache-2.0
Summary:        Google authentication library
Url:            https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/g/google-auth-oauthlib/google-auth-oauthlib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module google-auth}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-oauthlib >= 0.7.0}
BuildRequires:  %{python_module six}
BuildRequires:  python-futures
# /SECTION
Requires:       python-google-auth
Requires:       python-requests-oauthlib >= 0.7.0
Requires:       python-six
Recommends:     python-click
%ifpython2
Requires:       python-futures
%endif
BuildArch:      noarch

%python_subpackages

%description
This library provides oauthlib integration with google-auth.

%prep
%setup -q -n google-auth-oauthlib-%{version}
rm -rf tests/__pycache__/
rm -rf tests/*.pyc

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand pytest-%{$python_bin_suffix}

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/google-oauthlib-tool
%{python_sitelib}/*

%changelog
