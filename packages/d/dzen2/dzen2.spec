#
# spec file for package dzen2
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


%define _name dzen
Name:           dzen2
Version:        1379930259.488ab66
Release:        0
Summary:        A general purpose messaging and notification program
License:        MIT
Group:          System/GUI/Other
URL:            http://robm.github.io/dzen/
Source0:        %{name}-%{version}.tar.gz
### Manpages extracted from debian package and included here
### URL: http://ftp.us.debian.org/debian/pool/main/d/dzen2/dzen2_0.8.5-4_armel.deb
### *.deb Exctract: ar -x dzen2_0.8.5-4_armel.deb
Source1:        %{name}_man.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)

%description
Dezen is a general purpose messaging, notification and menuing program for X11. It was designed to be scriptable in any language and integrate well with window managers like dwm, wmii and xmonad though it will work with any windowmanger.

%prep
%setup -q

%build
sed -i '/^CFLAGS/ s/$/ %{optflags}/' config.mk
sed -i '/^CFLAGS/ s/$/ %{optflags}/' gadgets/config.mk
sed -i 's@strip@true@g' Makefile
sed -i 's@strip@true@g' gadgets/Makefile

make %{?_smp_mflags}
cd gadgets
make %{?_smp_mflags}
cd -

%install
%make_install PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_mandir}/man1
tar -jxf %{SOURCE1} -C %{buildroot}%{_mandir}/man1

cd gadgets
%make_install PREFIX=%{_prefix}

cd -
cd %{buildroot}%{_bindir}
for i in {dbar,gcpubar,gdbar,textwidth};
do
  mv ${i} %{name}-${i};
done

%files
%license LICENSE
%doc CREDITS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*gz
%{_bindir}/%{name}-dbar
%{_bindir}/%{name}-gcpubar
%{_bindir}/%{name}-gdbar
%{_bindir}/%{name}-textwidth

%changelog
