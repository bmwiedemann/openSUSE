#
# spec file for package openttd-opengfx
#
# Copyright (c) 2021 SUSE LLC
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


Name:           openttd-opengfx
Version:        0.6.1
Release:        0
Summary:        Default baseset graphics for OpenTTD
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://github.com/OpenTTD/OpenGFX
Source:         %{URL}/archive/refs/tags/%{version}.tar.gz#/OpenGFX-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  grfcodec
BuildRequires:  nml >= 0.5
BuildRequires:  openttd-data
BuildRequires:  python3-base
BuildRequires:  xz
Requires:       openttd-data >= 1.5
Provides:       opengfx = %{version}
BuildArch:      noarch
%if 0%{?with_gimp}
BuildRequires:  gimp >= 2.4
%if 0%{?suse_version} < 1550
BuildRequires:  gimp-plugins-python
%endif
%endif

%description
OpenGFX is an open source graphics base set designed to be used by OpenTTD.

OpenGFX provides a set of free and open source base graphics, and aims to
ensure the best possible out-of-the-box experience with OpenTTD.

%prep
%setup -q -n OpenGFX-%{version}
%if 0%{?with_gimp}
make clean-gfx
%endif

%build
# set $UNIX2DOS to null, fixes http://dev.openttdcoop.org/issues/7669
%make_build UNIX2DOS= grf PYTHON=%{_bindir}/python3 REPO_VERSION=%{version} _V=

%install
# we need to define version on the install target, else it could conflict with
# possible same named opengfx in $HOME
%define ogfxdir %{_datadir}/openttd/baseset/opengfx-%{version}
make install INSTALL_DIR=%{buildroot}%{ogfxdir} PYTHON=%{_bindir}/python3 REPO_VERSION=%{version} _V=

%check
%make_build opengfx-%{version}.check.md5 check PYTHON=%{_bindir}/python3 REPO_VERSION=%{version} _V=

%files
%license %{ogfxdir}/license.txt
%doc %{ogfxdir}/changelog.txt
%doc %{ogfxdir}/readme.txt
%dir %{ogfxdir}
%{ogfxdir}/opengfx.obg
%{ogfxdir}/*.grf
%{ogfxdir}/*.txt

%changelog
