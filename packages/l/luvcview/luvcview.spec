#
# spec file for package luvcview
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



Name:           luvcview
BuildRequires:  SDL-devel SDL_image-devel
%if 0%{?suse_version} >= 1210
BuildRequires:  libv4l-devel >= 0.8.4
%endif
AutoReqProv:    on
Group:          Productivity/Multimedia/Video/Players
Summary:        Simple V4L2 application using sdl
Version:        20070512
Release:        15
Source:         %name-%version.src.tar.gz
Url:            http://mxhaard.free.fr/spca50x/Investigation/uvc/  
License:        GPL-2.0+
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch1:         luvcview-add-COPYING.patch
Patch2:         luvcview-memory-leaks.patch
Patch3:         luvcview-v4l-2.6.38.patch

%description
luvcview is a simple V4L2 application using sdl



Authors:
--------
    Laurent Pinchart  
    Michel Xhaard  

%prep
%setup -n luvcview-%version
%patch1 -p1
%patch2
%if 0%{?suse_version} >= 1210
%patch3 -p1
%endif

%build
make

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -s -m 755 luvcview %{buildroot}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/luvcview

%changelog
