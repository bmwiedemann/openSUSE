#
# spec file for package instlux
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


%if 0%{?suse_version} >= 1500 && !0%{?skelcd_compat}
%define skelcdpath /usr/lib/skelcd
%endif

Name:           instlux
Summary:        Windows openSUSE installer
License:        GPL-2.0-or-later
Group:          Metapackages
URL:            http://en.opensuse.org/Instlux
Version:        15.6.2
Release:        0
AutoReqProv:    off
BuildRequires:  dos2unix
Source1:        openSUSE_installer.exe
Source2:        %name-README.BUILD
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64

%description
Find your place in the Linux world by upgrading your windows to a Linux
system the easiest possible way: running an installer on your Windows.

This package as meta package contains the instlux CD content.

%prep

%build

%install
# create a short README for the pseudo main package
mkdir -p %buildroot%_defaultdocdir/%name/
cat > %buildroot%_defaultdocdir/%name/README << EOF
Instlux allows a windows user start installing openSUSE from Windows, without
configuring the BIOS.
Instlux was based on Marc Herberts web page[1] and was started as a
sourceforge.net[2] project on October 2005.
Currently maintained at github[3] and OBS project[4].
Instlux is included in openSUSE since 10.3.
[1]: http://marc.herbert.free.fr/linux/win2linstall.html
[2]: http://instlux.svn.sourceforge.net/
[3]: https://github.com/belphegor-belbel/instlux/
[4]: https://build.opensuse.org/project/show/home:belphegor_belbel:instlux
Have a lot of fun!
EOF
install -m644 %{S:2} %buildroot%_defaultdocdir/%name/README.BUILD
mkdir -p %buildroot%{?skelcdpath}/CD1
install -m644 %{S:1} %buildroot%{?skelcdpath}/CD1/openSUSE_installer.exe

echo "[autorun]" > %buildroot%{?skelcdpath}/CD1/autorun.inf
echo "label = openSUSE installer" >> %buildroot%{?skelcdpath}/CD1/autorun.inf
echo "icon  = susego.ico" >> %buildroot%{?skelcdpath}/CD1/autorun.inf
echo "open  = openSUSE_installer.exe" >> %buildroot%{?skelcdpath}/CD1/autorun.inf
unix2dos %buildroot%{?skelcdpath}/CD1/autorun.inf

%files
%defattr(-, root, root)
%dir %_defaultdocdir/%name
%doc %_defaultdocdir/%name/*
%if %{defined skelcdpath}
%dir %{skelcdpath}
%endif
%{?skelcdpath}/CD1

%changelog
