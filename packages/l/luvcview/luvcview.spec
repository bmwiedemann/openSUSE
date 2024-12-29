#
# spec file for package luvcview
#
# Copyright (c) 2024 SUSE LLC
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


Name:           luvcview
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  libv4l-devel >= 0.8.4
Group:          Productivity/Multimedia/Video/Players
Summary:        Simple V4L2 application using sdl
Version:        20070512
Release:        0
Source:         %name-%version.src.tar.gz
URL:            http://mxhaard.free.fr/spca50x/Investigation/uvc/
License:        GPL-2.0-or-later
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch1:         luvcview-add-COPYING.patch
Patch2:         luvcview-memory-leaks.patch
Patch3:         luvcview-v4l-2.6.38.patch
Patch4:         luvcview-fix-implicit.patch

%description
luvcview is a simple V4L2 application using sdl



Authors:
--------
    Laurent Pinchart
    Michel Xhaard

%prep
%setup -n luvcview-%version
%patch -P 1 -p1
%patch -P 2
%patch -P 3 -p1
%patch -P 4 -p1

%build
make

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -s -m 755 luvcview %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%{_bindir}/luvcview

%changelog
