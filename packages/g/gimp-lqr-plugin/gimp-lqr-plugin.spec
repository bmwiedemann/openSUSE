#
# spec file for package gimp-lqr-plugin
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


Name:           gimp-lqr-plugin
Version:        0.7.2
Release:        0
Summary:        Content-aware resizing plug-in for GIMP
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://liquidrescale.wikidot.com/
Source0:        https://github.com/carlobaldassi/gimp-lqr-plugin/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/carlobaldassi/gimp-lqr-plugin/commit/22a274942434ae841b0b51a183979ddb560996f9
Patch0:         upstream-Fix-compilation-errors.patch
BuildRequires:  gimp-devel >= 2.8.0
BuildRequires:  intltool
BuildRequires:  liblqr-devel >= 0.4.0
Requires:       gimp >= 2.8.0

%description
This GIMP plug-in implements the content-aware resizing algorithm
described in the paper "Seam Carving for Content-Aware Image Resizing"
by Shai Avidan and Ariel Shamir.

%package -n gimp-plugin-lqr
Summary:        Content-aware resizing plug-in for GIMP
Group:          Productivity/Graphics/Bitmap Editors
Recommends:     gimp-plugin-lqr-lang
Provides:       %{name} = %{version}

%description -n gimp-plugin-lqr
This GIMP plug-in implements the content-aware resizing algorithm
described in the paper "Seam Carving for Content-Aware Image Resizing"
by Shai Avidan and Ariel Shamir.

%lang_package -n gimp-plugin-lqr

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
# ro_RO locale should simply be ro
test ! -e %{buildroot}%{_datadir}/locale/ro
mv %{buildroot}%{_datadir}/locale/ro_RO %{buildroot}%{_datadir}/locale/ro

%find_lang gimp20-lqr-plugin

%files -n gimp-plugin-lqr
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_libdir}/gimp/2.0/plug-ins/gimp-lqr-plugin
%{_libdir}/gimp/2.0/plug-ins/plug_in_lqr_iter
%{_datadir}/gimp-lqr-plugin/
%dir %{_datadir}/gimp/2.0/scripts/
%{_datadir}/gimp/2.0/scripts/batch-gimp-lqr.scm

%files -n gimp-plugin-lqr-lang -f gimp20-lqr-plugin.lang

%changelog
