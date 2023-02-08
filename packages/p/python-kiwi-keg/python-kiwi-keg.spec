#
# spec file for package python-kiwi-keg
#
# Copyright (c) 2022 SUSE Software Solutions Germany GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via:
#
#       https://github.com/SUSE-Enceladus/keg/issues
#

# If they aren't provided by a system installed macro, define them
%{!?_defaultdocdir: %global _defaultdocdir %{_datadir}/doc}
%{!?__python3: %global __python3 /usr/bin/python3}

%if %{undefined python3_sitelib}
%global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%endif

%if 0%{?el7}
%global python3_pkgversion 36
%else
%{!?python3_pkgversion:%global python3_pkgversion 3}
%endif

%if 0%{?debian} || 0%{?ubuntu}
%global is_deb 1
%global pygroup python
%global sysgroup admin
%global develsuffix dev
%else
%global pygroup Development/Languages/Python
%global sysgroup System/Management
%global develsuffix devel
%endif

Name:           python-kiwi-keg
Version:        2.0.2
Release:        0
Url:            https://github.com/SUSE-Enceladus/keg
Summary:        KEG - Image Composition Tool
License:        GPL-3.0-or-later
%if "%{_vendor}" == "debbuild"
# Needed to set Maintainer in output debs
Packager:       Public Cloud Team <public-cloud-dev@susecloud.net>
%endif
Group:          %{pygroup}
Source:         kiwi-keg-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python%{python3_pkgversion}-%{develsuffix}
BuildRequires:  python%{python3_pkgversion}-Jinja2
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-Sphinx
BuildRequires:  fdupes
BuildArch:      noarch

%description
KEG is an image composition tool for KIWI image descriptions

# python3-kiwi-keg
%package -n python%{python3_pkgversion}-kiwi-keg
Summary:        KEG - Image Composition Tool
Group:          Development/Languages/Python
Requires:       python%{python3_pkgversion}-docopt
Requires:       python%{python3_pkgversion}-kiwi >= 9.21.21
Requires:       python%{python3_pkgversion}-Jinja2
Requires:       python%{python3_pkgversion}-schema
Requires:       python%{python3_pkgversion}-setuptools
%if 0%{?ubuntu} || 0%{?debian}
Requires:       python%{python3_pkgversion}-yaml
%else
Requires:       python%{python3_pkgversion}-PyYAML
%endif
%if 0%{?suse_version}
Requires:       python%{python3_pkgversion}-Cerberus
%else
Requires:       python%{python3_pkgversion}-cerberus
%endif

%description -n python%{python3_pkgversion}-kiwi-keg
KEG is an image composition tool for KIWI image descriptions

%package -n obs-service-compose_kiwi_description
Summary:        An OBS service: generate KIWI description using KEG
Group:          Development/Tools/Building
Requires:       python%{python3_pkgversion}-kiwi-keg
Requires:       git

%description -n obs-service-compose_kiwi_description
This is a source service for openSUSE Build Service.

The source service produces a KIWI image description through KEG from one or
more given git repositories that contain keg-recipes source tree. It supports
auto-generation of change log files from commit history.

%prep
%setup -q -n kiwi-keg-%{version}

%build
# Build Python 3 version
python3 setup.py build

# Build man pages
make -C doc man

%install
# Install Python 3 version
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot} %{?is_deb:--install-layout=deb}

# Install man pages
make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ install

# Install LICENSE and README
make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ install_package_docs

%files -n python%{python3_pkgversion}-kiwi-keg
%dir %{_defaultdocdir}/python-kiwi-keg
%dir %{_usr}/lib/obs
%{_bindir}/generate_recipes_changelog
%{_bindir}/keg
%{python3_sitelib}/kiwi_keg*
%{_defaultdocdir}/python-kiwi-keg/LICENSE
%{_defaultdocdir}/python-kiwi-keg/README
%doc %{_mandir}/man1/*

%files -n obs-service-compose_kiwi_description
%{_usr}/lib/obs/service

%changelog
