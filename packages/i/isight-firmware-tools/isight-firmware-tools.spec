#
# spec file for package isight-firmware-tools
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _udevdir %(pkg-config --variable=udevdir udev)
%define _udevrulesdir %{_udevdir}/rules.d
Name:           isight-firmware-tools
Version:        1.6
Release:        0
Summary:        Tools to manipulate firmware for Built-in iSight
License:        GPL-2.0
Group:          Amusements/Toys/Graphics
Url:            http://bersace03.free.fr/ift/
Source0:        https://launchpad.net/isight-firmware-tools/main/%{version}/+download/isight-firmware-tools-%{version}.tar.gz
Source1:        https://launchpad.net/isight-firmware-tools/main/%{version}/+download/isight-firmware-tools-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch0:         isight-firmware-tools-older_isight-1.6.0.diff
Patch1:         isight-ft-udev.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(udev)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
This project provide tools to manipulate firmware for Built-in iSight
found on Apple machine since iMac G5 iSight

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}

rm -f %{buildroot}%{_infodir}/dir

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/isight-firmware-tools %{buildroot}%{_docdir}/isight-firmware-tools

%post
%install_info --info-dir=%{_infodir} %{_infodir}/ift-extract.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ift-export.info.gz
%{udev_rules_update}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ift-extract.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ift-export.info.gz

%files -f %{name}.lang
%defattr(-,root,root)
%{_udevrulesdir}/isight.rules
%dir %{_docdir}/%{name}
%{_bindir}/ift-export
%{_bindir}/ift-extract
%{_udevdir}/ift-load
%doc %{_docdir}/%{name}/HOWTO
%{_infodir}/*
%{_mandir}/man1/*.1%{ext_man}

%changelog
