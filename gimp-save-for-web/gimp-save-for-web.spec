#
# spec file for package gimp-save-for-web
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gimp-save-for-web
Version:        0.29.3
Release:        0
Summary:        Save for Web plug-in for The Gimp
License:        GPL-2.0+
Group:          Productivity/Graphics/Bitmap Editors
Url:            http://registry.gimp.org/node/33
Source:         http://registry.gimp.org/files/%{name}-%{version}.tar.bz2
BuildRequires:  automake
BuildRequires:  gimp-devel
BuildRequires:  intltool
BuildRequires:  libtool
%if %{?gimp_api_version:1}0
Requires:       gimp(abi) = %{gimp_abi_version}
Requires:       gimp(api) = %{gimp_api_version}
%else
%requires_eq gimp
%endif
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Save for Web allows to find compromise between minimal file size and
acceptable quality of image quickly. While adjusting various settings,
you may explore how image and file size change. Options to decrease
image file size include setting quality, number or colors, resizing,
cropping, Exif information removal, etc.

%lang_package
%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang gimp20-save-for-web

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/gimp/2.0/plug-ins/webexport
%{_datadir}/gimp-save-for-web/

%files lang -f gimp20-save-for-web.lang

%changelog
