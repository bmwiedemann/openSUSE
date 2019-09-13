#
# spec file for package nautilus-image-converter
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2007-2010 Dominique Leuenberger, Amsterdam, The Netherlands.
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


#
%define nautilus_extdir %(pkg-config --variable=extensiondir libnautilus-extension)

Name:           nautilus-image-converter
Summary:        Nautilus Image Converter
License:        GPL-2.0+
Group:          Productivity/Graphics/Convertors
Version:        0.3.0
Release:        0
Url:            http://www.bitron.ch/software/nautilus-image-converter.php
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM nautilus-image-converter-git.patch vuntz@opensuse.org -- Update to code from git, as of 2011-04-16
Patch0:         nautilus-image-converter-git.patch
# needed for patch0
BuildRequires:  gnome-common
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  nautilus-devel
Recommends:     ImageMagick
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Nautilus-Image-Converter extension allows you to resize/rotate images
from Nautilus.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
# needed for patch0
NOCONFIGURE=1 gnome-autogen.sh
%configure --with-pic
%__make %{?jobs:-j%jobs}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS
%{nautilus_extdir}/libnautilus-image-converter.so
%{_datadir}/nautilus-image-converter

%files lang -f %{name}.lang

%changelog
