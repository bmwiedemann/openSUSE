#
# spec file for package tkxcd
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


Name:           tkxcd
Version:        1.1.0
Release:        0
Summary:        Graphical frontend for diff
License:        GPL-2.0+
Group:          Productivity/Text/Utilities
Source:         tkxcd_1.1.0.tar.gz
Patch:          tkxcd-wish.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       tkxcd_1.1.0
Requires:       tk

%description
This is a diff front-end with a look and feel based on Atria Clearcase
xcleardiff. Both files are displayed in a window each and the
differences are marked in different colors.



Authors:
--------
    John C. Quillan <quillan@doitnow.com>

%prep
%setup -q -n tkxcd_1.1.0
%patch

%build

%install
install -d -m 755 %buildroot%_bindir %buildroot%_mandir/man1
install -m 755 tkxcd %buildroot%_bindir
install -m 644 tkxcd.man %buildroot%_mandir/man1/tkxcd.1

%files
%defattr(-,root,root)
%doc HISTORY README sample.tkxcdrc LICENSE TODO 
%doc %_mandir/*/*
%_bindir/*

%changelog
