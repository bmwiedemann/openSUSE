#
# spec file for package kalpa-themes
#
# Copyright (c) 2026 Shawn W Dunn <sfalken@kalpadesktop.org>
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


Name:           kalpa-themes
Version:        1.0
Release:        0
Summary:        Default desktop theme for the Kalpa Desktop
License:        GPL-2.0 and MIT and CC-BY-SA-4.0
URL:            https://kalpadesktop.org
Source:         %{name}-%{version}.tar.zst
BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  kf6-filesystem
BuildRequires:  update-bootloader-rpm-macros
BuildRequires:  zstd

%description
Default plasma desktop theme for the Kalpa Desktop

%package chefs-recommendation
Summary:        Alternate Theme for Kalpa Desktop
Requires:       %{name} = %{version}-%{release}

%description chefs-recommendation
This package offers "The Chef's Recommendation" light and dark
themes for the Kalpa Desktop.

They are rather opinionated in their layout but offer an
alternative take from the more default upstream-like experience
of the Kalpa Light/Dark themes

%package sddm
Summary:        SDDM Light/Dark themes for Kalpa
Requires:       %{name} = %{version}-%{release}
Conflicts:      sddm-theme-openSUSE
Conflicts:      plasma6-sddm-theme-openSUSE
Provides:       sddm-theme-openSUSE

%description sddm
Kalpa Desktop Light and Dark sddm themes

%package -n grub2-branding-kalpa
Summary:        Kalpa branding for GRUB2
License:        CC-BY-SA-3.0
Requires:       (grub2 or grub2-common)
Supplements:    (grub2 and branding-kalpa)
Conflicts:      grub2-branding
Provides:       grub2-branding = %{version}-%{release}
BuildArch:      noarch
%if 0%{?update_bootloader_requires:1}
%{update_bootloader_requires}
%endif

%description -n grub2-branding-kalpa
Kalpa Desktop branding for the GRUB2 graphical console

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/boot/grub2/themes

%fdupes %{buildroot}%{_datadir}

%post -n grub2-branding-kalpa
%{_datadir}/grub2/themes/kalpa/activate-theme
%if 0%{?update_bootloader_check_type_refresh_post:1}
%{update_bootloader_check_type_refresh_post grub2 grub2-efi}
%else
if test -e /boot/grub2/grub.cfg ; then
  %{_sbindir}/grub2-mkconfig -o /boot/grub2/grub.cfg || true
fi
%endif

%posttrans -n grub2-branding-kalpa
%{?update_bootloader_posttrans}

%postun -n grub2-branding-kalpa
if [ $1 = 0 ] ; then
  rm -rf /boot/grub2/themes/kalpa
fi

%files
%license LICENSE wallpapers/*/LICENSE aurorae/themes/CatppuccinLatte-Classic/LICENSE aurorae/themes/CatppuccinMocha-Classic/LICENSE
%dir %{_datadir}/aurorae
%dir %{_datadir}/aurorae/themes
%dir %{_datadir}/plasma/desktoptheme
%dir %{_datadir}/plasma/look-and-feel
%exclude %{_datadir}/aurorae/themes/CatppuccinLatte-Classic/LICENSE
%exclude %{_datadir}/aurorae/themes/CatppuccinMocha-Classic/LICENSE
%{_datadir}/aurorae/themes/CatppuccinLatte-Classic/
%{_datadir}/aurorae/themes/CatppuccinMocha-Classic/
%{_datadir}/color-schemes/
%{_datadir}/plasma/desktoptheme/kalpa-dark/
%{_datadir}/plasma/desktoptheme/kalpa-light/
%{_datadir}/plasma/look-and-feel/org.kalpadesktop.dark/
%{_datadir}/plasma/look-and-feel/org.kalpadesktop.light/
%{_datadir}/wallpapers/KalpaDesktopDark/
%{_datadir}/wallpapers/KalpaDesktopLight/

%files chefs-recommendation
%{_datadir}/plasma/look-and-feel/org.kalpadesktop.chefrecommends/
%{_datadir}/plasma/look-and-feel/org.kalpadesktop.chefrecommendsdark/

%files sddm
%dir %{_datadir}/sddm
%dir %{_datadir}/sddm/themes
%{_datadir}/sddm/themes/kalpa-light/
%{_datadir}/sddm/themes/kalpa-dark/

%files -n grub2-branding-kalpa
%dir /boot/grub2
%dir /boot/grub2/themes
%{_datadir}/grub2
%ghost %attr(0644,root,root) /boot/grub2/themes/kalpa

%changelog

