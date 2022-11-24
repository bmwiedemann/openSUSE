#
# spec file
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define name_suffix %{nil}
%else
%define name_suffix -%{flavor}
%endif
Name:           rpmlint%{name_suffix}
Version:        2.4.0+git20221122.a31cc76
Release:        0
Summary:        RPM file correctness checker
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/rpmlint
Source0:        rpmlint-%{version}.tar.xz
Patch0:         disable-flake-and-cov.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildArch:      noarch
%if "%{flavor}" == "test"
BuildRequires:  appstream-glib
BuildRequires:  binutils
BuildRequires:  checkbashisms
BuildRequires:  dash
BuildRequires:  desktop-file-utils
BuildRequires:  myspell-cs_CZ
BuildRequires:  myspell-en_US
BuildRequires:  python3-magic
BuildRequires:  python3-pybeam
BuildRequires:  python3-pyenchant
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-pyxdg
BuildRequires:  python3-rpm
%if 0%{?python3_version_nodots < 311}
BuildRequires:  python3-tomli
%endif
BuildRequires:  python3-tomli-w
BuildRequires:  python3-zstandard
BuildRequires:  xz
%ifarch x86_64
BuildRequires:  glibc-32bit
%endif
%endif
%if "%{flavor}" == ""
Requires:       appstream-glib
Requires:       bash
Requires:       binutils
Requires:       checkbashisms
Requires:       cpio
Requires:       dash
Requires:       desktop-file-utils
Requires:       file
Requires:       findutils
Requires:       myspell-en_US
Requires:       python3-magic
Requires:       python3-pybeam
Requires:       python3-pyenchant
Requires:       python3-pyxdg
Requires:       python3-rpm
%if 0%{?python3_version_nodots < 311}
Requires:       python3-tomli
%endif
Requires:       python3-tomli-w
Requires:       python3-zstandard
Requires:       rpm-build
%endif

%description
rpmlint is a tool to check common errors on RPM packages. Binary and
source packages can be checked.

%prep
%autosetup -p1 -n rpmlint-%{version}

%build
%if "%{flavor}" != "strict"
%python3_build
%endif

%install
%if "%{flavor}" != "test"
mkdir -p %{buildroot}%{_sysconfdir}/xdg/rpmlint
install -m644 configs/openSUSE/scoring-strict.override.toml %{buildroot}%{_sysconfdir}/xdg/rpmlint
%endif

%if "%{flavor}" == ""
%python3_install
fdupes %{buildroot}%{python3_sitelib}
install -m644 configs/openSUSE/* %{buildroot}%{_sysconfdir}/xdg/rpmlint
rm %{buildroot}%{_sysconfdir}/xdg/rpmlint/scoring-strict.override.toml
%endif

%if "%{flavor}" == "test"
%check
python3 -m pytest
%endif

%files
%if "%{flavor}" == ""
%license COPYING
%doc README*
%{_bindir}/rpmlint
%{_bindir}/rpmdiff
%{python3_sitelib}/rpmlint*
%dir %{_sysconfdir}/xdg/rpmlint
%config %{_sysconfdir}/xdg/rpmlint/*

%else
%if "%{flavor}" == "strict"
%dir %{_sysconfdir}/xdg/rpmlint
%config %{_sysconfdir}/xdg/rpmlint/scoring-strict.override.toml
%endif
%endif

%changelog
