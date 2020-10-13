#
# spec file for package python-uvicorn
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
%define skip_python2 1
Name:           python-uvicorn
Version:        0.12.1
Release:        0
Summary:        The lightning-fast ASGI server
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/encode/uvicorn
Source:         https://github.com/encode/uvicorn/archive/%{version}.tar.gz#/uvicorn-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 7.0
Requires:       python-h11 >= 0.8.0
Requires:       python-httptools >= 0.0.13
Requires:       python-typing_extensions
Requires:       python-websockets >= 8.0
Recommends:     python-PyYAML
Suggests:       python-uvloop >= 0.14.0
Suggests:       python-watchgod
Suggests:       python-wsproto
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module h11 >= 0.8.0}
BuildRequires:  %{python_module httptools >= 0.0.13}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module uvloop >= 0.14.0}
BuildRequires:  %{python_module watchgod >= 0.6}
BuildRequires:  %{python_module websockets >= 8.0}
BuildRequires:  %{python_module wsproto >= 0.13.0}
# /SECTION
%python_subpackages

%description
The lightning-fast ASGI server.

%prep
%setup -q -n uvicorn-%{version}
rm setup.cfg

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/uvicorn
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative uvicorn

%postun
%python_uninstall_alternative uvicorn

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/uvicorn
%{python_sitelib}/*

%changelog
