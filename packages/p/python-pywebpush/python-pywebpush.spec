#
# spec file for package python-pywebpush
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
Name:           python-pywebpush
Version:        1.11.0
Release:        0
Summary:        WebPush publication library
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/web-push-libs/pywebpush
Source:         https://files.pythonhosted.org/packages/source/p/pywebpush/pywebpush-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 2.6.1
Requires:       python-http-ece >= 1.1.0
Requires:       python-py-vapid >= 1.5.0
Requires:       python-requests >= 2.21.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography >= 2.6.1}
BuildRequires:  %{python_module http-ece >= 1.1.0}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module nose >= 1.3.7}
BuildRequires:  %{python_module py-vapid >= 1.5.0}
BuildRequires:  %{python_module requests >= 2.21.0}
# /SECTION
%python_subpackages

%description
WebPush publication library.

%prep
%setup -q -n pywebpush-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pywebpush
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose

%post
%python_install_alternative pywebpush

%postun
%python_uninstall_alternative pywebpush

%files %{python_files}
%doc CHANGELOG.md README.md README.rst
%license LICENSE
%python_alternative %{_bindir}/pywebpush
%{python_sitelib}/*

%changelog
