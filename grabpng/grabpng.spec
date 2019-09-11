#
# spec file for package grabpng
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define version_unconverted 20160630

Name:           grabpng
Version:        20160630
Release:        0
Summary:        Sprite position adjuster for PNG files
License:        GPL-3.0 and BSD-3-Clause
Group:          Productivity/Graphics/Other
#Url:            http://code.google.com/p/grabpng/ # defunct
Url:            https://sourceforge.net/p/zdoom/grabpng/ci/master/tree/

Source:         %name-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  xz
%if !0%{?without_fltk}
BuildRequires:  fltk-devel
%endif

%description
grabpng allows to change the PNG "GRAB" and "ALPH" chunks used by
ZDoom.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%_bindir/*
%doc COPYING CREDITS

%changelog
