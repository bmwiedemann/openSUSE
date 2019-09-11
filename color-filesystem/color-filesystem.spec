#
# spec file for package color-filesystem
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           color-filesystem
Version:        1
Release:        1
Summary:        Color filesystem layout

Url:            http://www.freedesktop.org/wiki/OpenIcc
Group:          System/Base
License:        SUSE-Public-Domain
BuildArch:      noarch

Requires:       filesystem
Requires:       rpm       
Provides:       icc-dirs = 1.3
Obsoletes:      icc-dirs = 1.2

%description
This package provides directories and rpm macros that are required/used to store color management data for many applications.

%prep
# Nothing to prep

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/color/icc
mkdir -p %{buildroot}%{_datadir}/color/cmms
mkdir -p %{buildroot}%{_datadir}/color/settings
mkdir -p %{buildroot}%{_datadir}/color/target
mkdir -p %{buildroot}%{_localstatedir}/lib/color/icc

# rpm macros
mkdir -p %{buildroot}/usr/lib/rpm/
cat >%{buildroot}/usr/lib/rpm/macros.color<<EOF
%%_colordir %%_datadir/color
%%_syscolordir %%_colordir
%%_icccolordir %%_colordir/icc
%%_cmmscolordir %%_colordir/cmms
%%_settingscolordir %%_colordir/settings
%%_targetcolordir %%_colordir/target
EOF

%files
%defattr(-,root,root,-)
%dir %{_datadir}/color
%dir %{_datadir}/color/icc
%dir %{_datadir}/color/cmms
%dir %{_datadir}/color/settings
%dir %{_datadir}/color/target
%dir %{_localstatedir}/lib/color
%dir %{_localstatedir}/lib/color/icc
/usr/lib/rpm/macros.color

%changelog
