#
# spec file for package eduvpn-common
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


%define skip_python2 1
%define _name eduvpn_common
Name:           eduvpn-common
Version:        4.0.0
Release:        0
Summary:        Shared library for eduVPN
License:        MIT
Group:          System/Libraries
URL:            https://www.eduvpn.org/
Source0:        https://codeberg.org/eduVPN/eduvpn-common/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://codeberg.org/eduVPN/eduvpn-common/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
                # https://app.eduvpn.org/linux/v4/deb/app+linux@eduvpn.org.asc and inside package dir 'keys'
Source2:        %{name}.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  go1.23
BuildRequires:  golang-packaging
BuildRequires:  python-rpm-macros
Recommends:     python3-%{name}
%define python_subpackage_only 1
%python_subpackages

%description
Shared library written in Go with functions that all eduVPN clients can use.

%package -n lib%{_name}-4_0_0
Summary:        Shared library for eduVPN
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n lib%{_name}-4_0_0
Shared library written in Go with functions that all eduVPN clients can use.

%package -n python-%{name}
Summary:        Python wrapper for eduVPN shared library
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
BuildArch:      noarch

%description -n python-%{name}
The python wrapper for the eduVPN common Go shared library.

%prep
%autosetup

%build
# Build shared library

# Prob. future way:
#
# export EDUVPN_COMMON_BUILD_SO=1
# (but, 'soname' is missing and python >= 3.7 seems needed here)

export CGO_ENABLED=1
go build -o lib/lib%{_name}-%{version}.so \
  -buildmode=c-shared -ldflags "-s -w -extldflags -Wl,-soname,lib%{_name}-%{version}.so" \
  -tags=release \
  ./exports

# Build Python wrapper
pushd wrappers/python
%pyproject_wheel
popd

%install
install -m 0755 -D -p lib/lib%{_name}-%{version}.so \
  %{buildroot}%{_libdir}/lib%{_name}-%{version}.so

pushd wrappers/python
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
pushd wrappers/python
%pytest tests.py
popd

%post -n lib%{_name}-4_0_0 -p /sbin/ldconfig
%postun -n lib%{_name}-4_0_0 -p /sbin/ldconfig

%files -n lib%{_name}-4_0_0
%license LICENSE
%doc CHANGES.md README.md
%{_libdir}/lib%{_name}-%{version}.so

%files %{python_files %{name}}
%license LICENSE
%doc CHANGES.md README.md
%dir %{python_sitelib}/%{_name}
%{python_sitelib}/%{_name}/
%{python_sitelib}/%{_name}-%{version}*

%changelog
