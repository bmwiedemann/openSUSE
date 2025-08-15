#
# spec file for package koan
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if "%{_vendor}" == "debbuild"
%global develsuffix dev
%else
%global develsuffix devel
%endif

%global __python %{__python3}

%if 0%{?suse_version} && 0%{?suse_version} < 1600
%{!?python3_pkgversion: %global python3_pkgversion 311}
%global python3_pkgversion 311
%global pythons python311
%else
%{!?python3_pkgversion: %global python3_pkgversion 3}
%global python3_pkgversion %{python3_pkgversion}
%endif
%if 0%{?suse_version}
%{?single_pythons_311plus}
%endif

%define next_tag 3.0.2
Name:           koan
Version:        3.0.1+git68
Release:        0%{?dist}
Summary:        Kickstart over a network

%if "%{_vendor}" == "debbuild"
Group:          admin
%else
Group:          Development/Libraries
%endif

License:        GPL-2.0-or-later
URL:            https://github.com/cobbler/koan
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-%{develsuffix}
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
%if "%{_vendor}" != "debbuild"
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%endif
%if 0%{?rhel}
# We need these to build this properly, and OBS doesn't pull them in by default for EPEL
BuildRequires:  epel-rpm-macros
%endif
Requires:       python%{python3_pkgversion}-distro
Requires:       python%{python3_pkgversion}-netifaces
%if 0%{?suse_version}
# SUSE distributions have messed up naming of this module
Requires:       python%{python3_pkgversion}-libvirt-python
%else
Requires:       python%{python3_pkgversion}-libvirt
%endif
%if "%{_vendor}" == "debbuild"
Recommends:     virtinst
%else
Recommends:     virt-install
%endif

%description
Koan stands for kickstart-over-a-network and allows for both network
installation of new virtualized guests and reinstallation of an existing
system. For use with a boot-server configured with Cobbler.

%prep
%autosetup -p1

%if 0%{?fedora}%{?rhel}
pathfix.py -pni "%{__python} %{py_shbang_opts}" bin
%endif

%build
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version}
%pyproject_wheel
%else
python3 -m pip wheel --verbose --progress-bar off --disable-pip-version-check --use-pep517 --no-build-isolation --no-deps --wheel-dir ./dist .
%endif

%install
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version}
%pyproject_install
%else
python3 -m pip install --verbose --progress-bar off --disable-pip-version-check --root %{buildroot} --no-compile --ignore-installed --no-deps --no-index .
%endif

%if "%{_vendor}" == "debbuild"
%post
# Do late-stage bytecompilation, per debian policy
py%{python3_pkgversion}compile -p %{name}

%preun
# Ensure all __pycache__ files are deleted, per debian policy
py%{python3_pkgversion}clean -p %{name}
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/koan
%{_bindir}/cobbler-register
%{python_sitelib}/koan
%{python_sitelib}/koan-%{next_tag}.dist-info

%changelog
