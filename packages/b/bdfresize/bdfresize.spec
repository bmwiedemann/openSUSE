#
# spec file for package bdfresize
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bdfresize
Version:        1.5
Release:        0
Summary:        A Tool for Resizing BDF Format Fonts
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://openlab.ring.gr.jp/efont/dist/tools/bdfresize/
Source0:        http://openlab.ring.gr.jp/efont/dist/tools/bdfresize/bdfresize-%{version}.tar.bz2
Patch0:         bdfresize-gcc4.patch
Patch1:         020_minus-sign.patch

%description
bdfresize is a command for magnifying or shrinking fonts described in the
standard BDF format.

%prep
%setup -q
%patch0
%patch1 -p1

%build
rm -f config.cache
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/bdfresize
%{_mandir}/man1/bdfresize.1%{ext_man}

%changelog
