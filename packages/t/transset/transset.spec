#
# spec file for package transset
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           transset
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)
Url:            http://www.kde.me.uk/index.php?page=x-6.8-xcomposite-howto
Version:        20040120
Release:        0
Summary:        Simple program to make windows transparent
License:        MIT
Group:          System/X11/Utilities
Source:         transset-%{version}.tar.bz2
Patch:          transset-%{version}.diff
Patch2:         transset-df-5.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
transset manipulates the _NET_WM_WINDOW_OPACITY property to make
windows transparent.

%prep
%setup -n transset
%patch
%patch2

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 transset $RPM_BUILD_ROOT/usr/bin
cat >> README.SUSE <<EOF
Details: 
    http://gentoo-wiki.com/TIP_Xorg_X11_and_Tranparency
    http://www.kde.me.uk/index.php?page=x-6.8-xcomposite-howto
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.SUSE README ChangeLog
/usr/bin/transset

%changelog
