#
# spec file for package gimp-lqr-plugin
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Peter Linnell
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


Name:           gimp-lqr-plugin
Version:        0.7.2
Release:        0
Summary:        Content-aware resizing plug-in for GIMP
License:        GPL-2.0+
Group:          Productivity/Graphics/Bitmap Editors
Url:            http://liquidrescale.wikidot.com/
Source0:        http://liquidrescale.wdfiles.com/local--files/en:download-page-sources/%{name}-%{version}.tar.bz2
BuildRequires:  gimp-devel >= 2.8.0
BuildRequires:  intltool
BuildRequires:  liblqr-devel >= 0.4.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This GIMP plug-in implements the content-aware resizing algorithm
described in the paper "Seam Carving for Content-Aware Image Resizing"
by Shai Avidan and Ariel Shamir.

%package -n gimp-plugin-lqr
Summary:        Content-aware resizing plug-in for GIMP
Group:          Productivity/Graphics/Bitmap Editors
Provides:       %{name} = %{version}
Recommends:     gimp-plugin-lqr-lang

%description -n gimp-plugin-lqr
This GIMP plug-in implements the content-aware resizing algorithm
described in the paper "Seam Carving for Content-Aware Image Resizing"
by Shai Avidan and Ariel Shamir.

%lang_package -n gimp-plugin-lqr
%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%makeinstall
# ro_RO locale should simply be ro
test ! -e %{buildroot}%{_datadir}/locale/ro
mv %{buildroot}%{_datadir}/locale/ro_RO %{buildroot}%{_datadir}/locale/ro
%find_lang gimp20-lqr-plugin

%clean
rm -rf %{buildroot}

%files -n gimp-plugin-lqr
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%dir %{_libdir}/gimp/
%dir %{_libdir}/gimp/2.0/
%dir %{_libdir}/gimp/2.0/plug-ins/
%{_libdir}/gimp/2.0/plug-ins/gimp-lqr-plugin
%{_libdir}/gimp/2.0/plug-ins/plug_in_lqr_iter
%dir %{_datadir}/gimp/
%dir %{_datadir}/gimp/2.0/
%dir %{_datadir}/gimp/2.0/scripts/
%{_datadir}/gimp-lqr-plugin/
%{_datadir}/gimp/2.0/scripts/batch-gimp-lqr.scm

%files -n gimp-plugin-lqr-lang -f gimp20-lqr-plugin.lang

%changelog
