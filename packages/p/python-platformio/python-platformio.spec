#
# spec file for package python-platformio
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
Name:           python-platformio
Version:        4.3.4
Release:        0
Summary:        New Generation Ecosystem for Embedded Development
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://platformio.org
Source:         https://files.pythonhosted.org/packages/source/p/platformio/platformio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-bottle
Requires:       python-click >= 5
Requires:       python-colorama
Requires:       python-marshmallow >= 2
Requires:       python-pyelftools >= 0.25
Requires:       python-pyserial >= 3
Requires:       python-requests >= 2.4.0
Requires:       python-semantic_version >= 2.8.1
Requires:       python-tabulate >= 0.8.3
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
PlatformIO is a cross-platform, cross-architecture, multiple framework,
professional tool for embedded systems engineers and for software developers
who write applications for embedded products.

%prep
%setup -q -n platformio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/pio
%python_clone -a %{buildroot}%{_bindir}/piodebuggdb
%python_clone -a %{buildroot}%{_bindir}/platformio

%post
%{python_install_alternative pio piodebuggdb platformio}

%postun
%{python_uninstall_alternative pio piodebuggdb platformio}

%files %{python_files}
%python_alternative %{_bindir}/pio
%python_alternative %{_bindir}/piodebuggdb
%python_alternative %{_bindir}/platformio
%{python_sitelib}/*

%changelog
