#
# spec file for package patterns-wsl
#
# Copyright (c) 2022 SUSE LLC
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


Name:           patterns-wsl
Version:        20220929
Release:        0
Summary:        Recommended packages for Windows Subsystem for Linux, WSL, WSLg
License:        MIT
Group:          Metapackages
URL:            https://github.com/sbradnick/patterns
BuildRequires:  patterns-rpm-macros
#BuildArch:      noarch

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

# ----

%package base
%pattern_development
Summary:        Base WSL packages
Group:          Metapackages
Provides:       pattern() = wsl_base
Provides:       pattern-icon() = wsl
Provides:       pattern-order() = 3420
Provides:       pattern-visible()
Requires:       bash
Recommends:     fish
Recommends:     zsh

%description base
This package contains the wsl_base pattern: recommended tools,libraries for using WSL.

%files base
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl_base.txt

# ----

%package gui
%pattern_development
Summary:        WSL GUI packages
Group:          Metapackages
Provides:       pattern() = wsl_gui
Provides:       pattern-icon() = wsl
Provides:       pattern-order() = 3420
Provides:       pattern-visible()
Requires:       lato-fonts
Requires:       xeyes
Recommends:     adwaita-icon-theme
Recommends:     gnome-icon-theme
Recommends:     noto-sans-fonts
Recommends:     powerline-fonts

%description gui
This package contains the wsl_gui pattern: recommended tools,libraries for using WSLg.

%files gui
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl_gui.txt

# ----

%package systemd
%pattern_development
Summary:        WSL systemd setup
Group:          Metapackages
Provides:       pattern() = wsl_systemd
Provides:       pattern-icon() = wsl
Provides:       pattern-order() = 3420
Provides:       pattern-visible()

%description systemd
This package contains the wsl_systemd pattern: provides /etc/wsl.conf and /sbin/init symlink where required.

#%%if 0%%{?suse_version} == 1500
#%%endif
%post systemd
if [[ ! -L /sbin/init ]];
then
  %{_bindir}/echo "ADDING /sbin/init -> /usr/lib/systemd/systemd SYMLINK."
  %{_bindir}/ln -s %{_systemd_util_dir}/systemd /sbin/init
  if [[ -e /etc/wsl.conf ]];
  then
    cp /etc/wsl.conf /etc/wsl.conf.$(date +%s)
  fi
  %{_bindir}/echo "ADDING /etc/wsl.conf ..."
  %{_bindir}/echo -e "# added by wsl_systemd pattern\n[boot]\nsystemd=true\n# END: wsl_systemd pattern edit" > %{_sysconfdir}/wsl.conf
fi

%files systemd
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl_systemd.txt

# ----

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl_base to be installed.' > %{buildroot}/usr/share/doc/packages/patterns/wsl_base.txt
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl_gui to be installed.' > %{buildroot}/usr/share/doc/packages/patterns/wsl_gui.txt
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl_systemd to be installed.' > %{buildroot}/usr/share/doc/packages/patterns/wsl_systemd.txt

%changelog
