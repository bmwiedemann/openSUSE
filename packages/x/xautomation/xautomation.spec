#
# spec file for package xautomation
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xautomation
Version:        1.09
Release:        0
Summary:        Control X from the command line for scripts
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://hoopajoo.net/projects/xautomation.html
Source0:        http://hoopajoo.net/static/projects/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(xtst)
BuildRequires:  libpng-devel

%description
Control X from the command line for scripts, and do "visual scraping" to find
things on the screen. The conrol interface allows mouse movement, clicking,
button up/down, key up/down, etc, and uses the XTest extension so you don't
have the annoying problems that xse has when apps ignore sent events. The
visgrep program find images inside of images and reports the coordinates,
allowing programs to find buttons, etc, on the screen to click on.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/pat2ppm
%{_bindir}/patextract
%{_bindir}/png2pat
%{_bindir}/rgb2pat
%{_bindir}/visgrep
%{_bindir}/xmousepos
%{_bindir}/xte
%{_mandir}/man1/*.1%{ext_man}
%{_mandir}/man7/%{name}.7%{ext_man}

%changelog
