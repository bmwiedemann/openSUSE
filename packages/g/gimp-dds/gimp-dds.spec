#
# spec file for package gimp-dds
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           gimp-dds
Version:        3.0.1
Release:        0
Summary:        Plugin for GIMP providing support for the DDS format
License:        GPL-2.0+
Group:          Productivity/Graphics/Bitmap Editors
Url:            http://code.google.com/p/gimp-dds/
Source0:        http://gimp-dds.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:  gimp-devel >= 2.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This GIMP plugin allows to load and save images in the Direct Draw
Surface (DDS) format.

%package -n gimp-plugin-dds
Summary:        Plugin for GIMP providing support for the DDS format
Group:          Productivity/Graphics/Bitmap Editors
Requires:       gimp >= 2.6

%description -n gimp-plugin-dds
This GIMP plugin allows to load and save images in the Direct Draw
Surface (DDS) format.

%package -n gimp-plugin-dds-doc
Summary:        Plugin for GIMP providing support for the DDS format -- Documentation
Group:          Documentation/Other
Requires:       gimp-plugin-dds = %{version}

%description -n gimp-plugin-dds-doc
This GIMP plugin allows to load and save images in the Direct Draw
Surface (DDS) format.

This package contains documentation for the following features of the
DDS plugin:

 + Saving general images
 + Saving cube map images
 + Saving volume map images

%prep
%setup -q

%build
# The Makefile correct expands CFLAGS
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -D -m 0755 dds %{buildroot}%{_libdir}/gimp/2.0/plug-ins/dds

%files -n gimp-plugin-dds
%defattr(-,root,root,-)
%doc COPYING LICENSE README README.dxt TODO
%{_libdir}/gimp/2.0/plug-ins/dds

%files -n gimp-plugin-dds-doc
%defattr(-,root,root,-)
%doc doc/*

%changelog
