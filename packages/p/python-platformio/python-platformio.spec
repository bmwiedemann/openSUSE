#
# spec file for package python-platformio
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-platformio
Version:        6.1.5
Release:        0
Summary:        New Generation Ecosystem for Embedded Development
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/platformio/platformio-core
Source0:        https://files.pythonhosted.org/packages/source/p/platformio/platformio-%{version}.tar.gz
Source99:       python-platformio.rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-aiofiles >= 0.8
Requires:       python-ajsonrpc >= 1
Requires:       python-bottle >= 0.12
Requires:       python-click >= 8.0.4
Requires:       python-colorama
Requires:       python-marshmallow >= 3
Requires:       python-pyelftools >= 0.27
Requires:       python-pyserial >= 3.5
Requires:       python-requests >= 2
Requires:       python-semantic_version >= 2.10
Requires:       python-starlette >= 0.20
Requires:       python-tabulate >= 0.8
# dropping requirement to 0.16 instead of 0.18, setup.py asks for 0.18 since python 3.7
Requires:       python-uvicorn >= 0.16
# dropping requirement to 1.0 instead of 1.1, setup.py asks for 1.1 since python 3.7
Requires:       python-wsproto >= 1.0
Requires:       python-zeroconf
Requires(post): update-alternatives
Requires(postun):update-alternatives

%python_subpackages

%description
PlatformIO is a cross-platform, cross-architecture, multiple framework,
professional tool for embedded systems engineers and for software developers
who write applications for embedded products.

%prep
%setup -q -n platformio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# mv because of gh#platformio/platformio-core#4458
%{python_expand mv %{buildroot}%{$python_sitelib}/scripts %{buildroot}%{$python_sitelib}/platformio
%fdupes %{buildroot}%{$python_sitelib}
}

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
%{python_sitelib}/platformio
%{python_sitelib}/platformio-%{version}*-info

%changelog
