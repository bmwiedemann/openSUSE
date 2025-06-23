#
# spec file for package python-ethtool
#
# Copyright (c) 2025 SUSE LLC
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


%global pypi_name ethtool
Name:           python-%{pypi_name}
Version:        0.15
Release:        0
Summary:        Ethernet settings Python bindings
License:        GPL-2.0-only
URL:            https://github.com/fedora-python/%{name}
Source:         https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libnl3-devel
# needs ifconfig for tests (to check feature parity)
BuildRequires:  net-tools-deprecated
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Python bindings for the ethtool kernel interface that allows querying and
changing of Ethernet interface settings, such as speed, port, autonegotiation, and
PCI locations.

%prep
%setup -q -n %{pypi_name}-%{version}
# No module imp in python 3.12+
rm tests/test_scripts.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}{%{_bindir},%{_sbindir}}/pifconfig
mv %{buildroot}{%{_bindir},%{_sbindir}}/pethtool
%python_clone -a %{buildroot}%{_sbindir}/pifconfig
%python_clone -a %{buildroot}%{_sbindir}/pethtool

%check
%pyunittest_arch -v

%post
# %%python_install_alternative for %{_sbindir} binaries
%{python_expand \
  %{_sbindir}/update-alternatives --quiet --install %{_sbindir}/pifconfig  pifconfig \
     %{_sbindir}/pifconfig-%{$python_version}  %{$python_version_nodots}
  %{_sbindir}/update-alternatives --quiet --install %{_sbindir}/pethtool  pethtool \
     %{_sbindir}/pethtool-%{$python_version}  %{$python_version_nodots}
}

%postun
%python_uninstall_alternative pifconfig
%python_uninstall_alternative pethtool

%files %{python_files}
%license COPYING
%doc README.rst CHANGES.rst
%{python_sitearch}/ethtool.cpython-*-linux-gnu.so
%{python_sitearch}/ethtool-%{version}.dist-info
%python_alternative %{_sbindir}/pethtool
%python_alternative %{_sbindir}/pifconfig

%changelog
