#
# spec file for package python-kiwi_crossprepare_plugin
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020 SUSE Software Solutions Germany GmbH, Nuernberg, Germany.
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

Name:           python-kiwi_crossprepare_plugin
Version:        0.1.6
Release:        0
URL:            https://github.com/OSInside/kiwi-crossprepare-plugin
Summary:        KIWI - Cross Image Arch Prepare Plugin
License:        GPL-3.0-or-later
%if "%{_vendor}" == "debbuild"
# Needed to set Maintainer in output debs
%endif
Group:          %{pygroup}
Source:         kiwi-crossprepare-plugin-%version.tar.xz
Source1:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  python%{python3_pkgversion}-%{develsuffix}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildArch:      noarch

%description
Prepare an image root tree for a cross architecture build process.

# python3-kiwi_crossprepare_plugin

%package -n python%{python3_pkgversion}-kiwi_crossprepare_plugin
Summary:        KIWI - Cross Image Arch Prepare Plugin
Group:          Development/Languages/Python
Requires:       python%{python3_pkgversion}-docopt
Requires:       python%{python3_pkgversion}-kiwi >= 9.21.21
Requires:       python%{python3_pkgversion}-setuptools
%if 0%{?ubuntu} || 0%{?debian}
Requires:       python%{python3_pkgversion}-yaml
%else
Requires:       python%{python3_pkgversion}-PyYAML
%endif
Requires:       qemu-linux-user

%description -n python%{python3_pkgversion}-kiwi_crossprepare_plugin
Prepare an image root tree for a cross architecture build process.

%prep
%setup -q -n kiwi-crossprepare-plugin-%{version}

%build
# Build Python 3 version
python3 setup.py build

%install
# Install Python 3 version
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot} %{?is_deb:--install-layout=deb}

# Install man pages and package documentation
#make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ install

%files -n python%{python3_pkgversion}-kiwi_crossprepare_plugin
#%dir %{_defaultdocdir}/python-kiwi_crossprepare_plugin
%{python3_sitelib}/kiwi_crossprepare_plugin*
#%{_defaultdocdir}/python-kiwi_crossprepare_plugin/LICENSE
#%{_defaultdocdir}/python-kiwi_crossprepare_plugin/README
#%doc %{_mandir}/man8/*

%changelog
