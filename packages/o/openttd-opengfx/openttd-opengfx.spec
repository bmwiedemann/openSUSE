#
# spec file for package openttd-opengfx
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


Name:           openttd-opengfx
Version:        0.5.5
Release:        0
Summary:        Default baseset graphics for OpenTTD
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Other
URL:            http://dev.openttdcoop.org/projects/opengfx
Source:         http://bundles.openttdcoop.org/opengfx/releases/%{version}/opengfx-%{version}-source.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  dos2unix
BuildRequires:  nml >= 0.4.1
%if !0%{?without_gimp}
BuildRequires:  gimp
%if 0%{?suse_version} < 1550
BuildRequires:  gimp-plugins-python
%endif
%endif
BuildRequires:  grfcodec
BuildRequires:  python-base
BuildRequires:  python-xml
BuildRequires:  python3-base
BuildRequires:  xz
Requires:       openttd-data >= 1.5
Provides:       opengfx = %{version}

%description
OpenGFX is an open source graphics base set designed to be used by OpenTTD.

OpenGFX provides a set of free and open source base graphics, and aims to
ensure the best possible out-of-the-box experience with OpenTTD.

%prep
%setup -qn opengfx-%{version}-source
%if !0%{?without_gimp}
make clean-gfx
%endif

%build
# set $UNIX2DOS to null, fixes http://dev.openttdcoop.org/issues/7669
make UNIX2DOS=

%install
# we need to define version on the install target, else it could conflict with
# possible same named opengfx in $HOME
%define ogfxdir %{_datadir}/openttd/baseset/opengfx-%{version}
make install INSTALL_DIR=%{buildroot}%{ogfxdir}

%files
%defattr(-,root,root,-)
%dir %{_datadir}/openttd
%dir %{_datadir}/openttd/baseset
%dir %{ogfxdir}
%doc %{ogfxdir}/changelog.txt
%doc %{ogfxdir}/license.txt
%doc %{ogfxdir}/readme.txt
%{ogfxdir}/ogfx1_base.grf
%{ogfxdir}/ogfxc_arctic.grf
%{ogfxdir}/ogfxe_extra.grf
%{ogfxdir}/ogfxh_tropical.grf
%{ogfxdir}/ogfxi_logos.grf
%{ogfxdir}/ogfxt_toyland.grf
%{ogfxdir}/opengfx.obg

%changelog
