#
# spec file for package python-google-auth-oauthlib
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-google-auth-oauthlib
Version:        1.2.4
Release:        0
Summary:        Google authentication library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-auth-library-python-oauthlib
Source:         https://files.pythonhosted.org/packages/source/g/google_auth_oauthlib/google_auth_oauthlib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 2.14.0
Requires:       python-requests-oauthlib >= 0.7.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-click
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 6.0.0}
BuildRequires:  %{python_module google-auth >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-oauthlib >= 0.7.0}
# /SECTION
%python_subpackages

%description
This library provides oauthlib integration with google-auth.

%prep
%autosetup -p1 -n google_auth_oauthlib-%{version}
rm -rf docs
rm -rf tests/__pycache__/
rm -rf tests/*.pyc

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/google_auth_oauthlib
%{python_sitelib}/google_auth_oauthlib-%{version}.dist-info

%changelog
