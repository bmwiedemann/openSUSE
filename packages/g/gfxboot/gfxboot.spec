#
# spec file for package gfxboot
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gfxboot
Version:        4.5.86
Release:        0
Summary:        Graphical Boot Logo for GRUB, LILO and SYSLINUX
License:        GPL-2.0-or-later
Group:          System/Boot
URL:            http://en.opensuse.org/SDB:Gfxboot
Source:         %{name}-%{version}.tar.xz
Source1:        KDE.tar.xz
Source2:        SLED.tar.xz
Source3:        SLES.tar.xz
Source4:        examples.tar.xz
Source5:        openSUSE.tar.xz
Source6:        upstream.tar.xz
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  fribidi
BuildRequires:  libxslt
BuildRequires:  nasm
BuildRequires:  perl-HTML-Parser
BuildRequires:  sgml-skel
BuildRequires:  w3m
BuildRequires:  xmlto
Requires:       coreutils
Requires:       cpio
Requires:       dosfstools
Requires:       mktemp
Requires:       mtools
Requires:       perl-HTML-Parser
Requires:       syslinux
Recommends:     %{name}-theme >= 4
ExclusiveArch:  %ix86 x86_64
%perl_requires

%description
Tools to configure the graphics for your GRUB, LILO or SYSLINUX bootloader.

%package        devel
Summary:        Tools for creating a graphical boot logo
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Here you find the necessary programs to create your own graphical boot
logo. The logo can be used with GRUB, LILO or SYSLINUX.

%package        branding-upstream
Summary:        Graphical bootloader upstream theme
Group:          System/Boot
PreReq:         %{name} >= 4
Supplements:    packageand(%{name}:branding-upstream)
Provides:       %{name}-branding = %{version}
Provides:       %{name}-theme = %{version}
Conflicts:      otherproviders(%{name}-branding)

%description branding-upstream
upstream theme for gfxboot (bootloader graphics).

%package        branding-SLES
Summary:        Graphical bootloader SLES theme
Group:          System/Boot
PreReq:         %{name} >= 4
Supplements:    packageand(%{name}:branding-SLES)
Provides:       %{name}-branding = %{version}
Provides:       %{name}-theme = %{version}
Obsoletes:      bootloader-theme-SLES < %{version}
Provides:       bootloader-theme-SLES = %{version}
Conflicts:      otherproviders(%{name}-branding)

%description branding-SLES
SLES theme for gfxboot (bootloader graphics).

%package        branding-SLED
Summary:        Graphical bootloader SLED theme
Group:          System/Boot
PreReq:         %{name} >= 4
Supplements:    packageand(%{name}:branding-SLED)
Provides:       %{name}-branding = %{version}
Provides:       %{name}-theme = %{version}
Obsoletes:      bootloader-theme-NLD < %{version}
Provides:       bootloader-theme-NLD = %{version}
Conflicts:      otherproviders(%{name}-branding)

%description branding-SLED
SLED theme for gfxboot (bootloader graphics).

%package        branding-KDE
Summary:        Graphical bootloader KDE theme
Group:          System/Boot
PreReq:         %{name} >= 4
Supplements:    packageand(%{name}:branding-KDE)
Provides:       %{name}-branding = %{version}
Provides:       %{name}-theme = %{version}
Conflicts:      otherproviders(%{name}-branding)

%description branding-KDE
KDE theme for gfxboot (bootloader graphics).

%prep
%setup -q -a1 -a2 -a3 -a4 -a5 -a6

%build
# fix build
export SUSE_ASNEEDED=0
make X11LIBS=%{_prefix}/X11R6/%{_lib}
make doc
make themes

%install
%make_install
make DESTDIR=%{buildroot} installsrc
rm -rf %{buildroot}/etc/bootsplash/themes/openSUSE/
gzip -9c doc/%{name}.8 >%{name}.8.gz
install -d -m 755 %{buildroot}%{_mandir}/man8
install -m 644 %{name}.8.gz %{buildroot}%{_mandir}/man8
mkdir %{buildroot}/boot
touch %{buildroot}/boot/message

%post branding-upstream
%{name} --update-theme upstream

%post branding-SLES
%{name} --update-theme SLES

%post branding-SLED
%{name} --update-theme SLED

%post branding-KDE
%{name} --update-theme KDE

%files
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.gz
%dir %{_sysconfdir}/bootsplash
%dir %{_sysconfdir}/bootsplash/themes
%doc README.md
%license COPYING

%files devel
%{_sbindir}/%{name}-compile
%{_sbindir}/%{name}-font
%{_sbindir}/gfxtest
%doc doc/%{name}.html
%doc doc/%{name}.txt
%{_datadir}/%{name}

%files branding-upstream
%{_sysconfdir}/bootsplash/themes/upstream
%ghost /boot/message

%files branding-SLES
%{_sysconfdir}/bootsplash/themes/SLES
%ghost /boot/message

%files branding-SLED
%{_sysconfdir}/bootsplash/themes/SLED
%ghost /boot/message

%files branding-KDE
%{_sysconfdir}/bootsplash/themes/KDE
%ghost /boot/message

%changelog
