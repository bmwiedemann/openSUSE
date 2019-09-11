#
# spec file for package cutecom
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           cutecom
Version:        0.51.0
Release:        0
Url:            https://gitlab.com/cutecom/cutecom
Summary:        A graphical serial terminal 
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtserialport-devel
Source:         %{name}-%{version}.tgz

%description
CuteCom is a graphical serial terminal, similar to minicom. It is
written using the Qt library.

It is aimed mainly at hardware developers or other people who need a
terminal to talk to their devices.

%prep
%setup

%build
cmake .
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -s -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/
gzip %{name}.1
install -m 644 %{name}.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/

install -d 755 $RPM_BUILD_ROOT%{_datadir}/applications
install -m 644 distribution/openSUSE/cutecom.desktop $RPM_BUILD_ROOT%{_datadir}/applications/
install -d 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 644 images/cutecom.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/cutecom.svg
%doc Changelog TODO CREDITS README.md
%license LICENSE

%changelog
