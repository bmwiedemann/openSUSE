#
# spec file for package PlayOnLinux
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


%define _sname    POL-POM-4
%define _sversion 4.4
%define _name     playonlinux
Name:           PlayOnLinux
Version:        4.4.0
Release:        0
Summary:        Play your Windows games on GNU/Linux
License:        GPL-3.0-only
Group:          Amusements/Games/Other
URL:            https://playonlinux.com
#Source:         http://repository.playonlinux.com/%%{name}/%%{version}/%%{name}_%%{version}.tar.gz
Source:         https://github.com/PlayOnLinux/POL-POM-4/archive/%{_sversion}/%{name}-%{version}.tar.gz
Source1:        playonlinux.sh
# PATCH-FIX-OPENSUSE PlayOnLinux-desktop.patch
Patch0:         %{name}-desktop.patch
# PATCH-FIX-OPENSUSE PlayOnLinux-fix_media_dir.patch: Fix variable MEDIA_DIR to correct location.
Patch9:         %{name}-fix_media_dir.patch
# PATCH-FIX-OPENSUSE PlayOnLinux-https.patch: Fix unencrypted connection to www.playonlinux.com
Patch10:        %{name}-https.patch
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
# Not need for build. Only to test if packages are exists.
BuildRequires:  python3
BuildRequires:  python3-natsort
BuildRequires:  python3-wxPython
Requires:       ImageMagick
%if 0%{?suse_version} <= 1500
Requires:       dbus-1-python
%endif
Requires:       gettext
Requires:       icoutils
Requires:       jq
Requires:       python3
Requires:       python3-natsort
Requires:       python3-wxPython
Requires:       unzip
Requires:       wget
Requires:       wine
Requires:       xterm
BuildArch:      noarch
# Remove when p7zip-full is in all products
%if 0%{?suse_version} >= 1500
Requires:       p7zip-full
%else
Requires:       p7zip
%endif

%description
PlayOnLinux is a piece of software which allows you to easily install and use
numerous games and apps designed to run with Microsoft Windows.
Few games are compatible with GNU/Linux at the moment and it certainly is
a factor preventing the migration to this system.
PlayOnLinux brings a cost-free, accessible and efficient solution to this problem.

%prep
%setup -q -n %{_sname}-%{_sversion}
%patch0 -p1
%patch9 -p1
%patch10 -p1
# rpmlint
find . -type f -exec sed -i -e 's|\/usr\/bin\/env python|\/usr\/bin\/python|g' {} \;
find . -type f -exec sed -i -e 's|\/usr\/bin\/env bash|\/bin\/bash|g' {} \;

%build
# Nothing to build.

%install
install -Dm 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{_name}

mkdir -p %{buildroot}%{_datadir}/%{_name}/
cp -rf * %{buildroot}%{_datadir}/%{_name}/

# Remove unneeded files.
rm -f %{buildroot}%{_datadir}/%{_name}/{CHANGELOG.md,README.md,LICENCE,TRANSLATORS,python/mainwindow.py.orig}
rm -rf %{buildroot}%{_datadir}/%{_name}/src

for f in bash/read_pc_cd bash/find_python bash/startup_after_server python/setupwindow/gui_server.py \
  tests/bash/test-versionlower tests/python/test_versionlower.py; do
    chmod +x "%{buildroot}%{_datadir}/%{_name}/$f"
done

install -Dm 0644 etc/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 %{buildroot}%{_datadir}/%{_name}%{_sysconfdir}/%{_name}.png %{buildroot}%{_datadir}/pixmaps/%{_name}.png
install -Dm 0644 %{buildroot}%{_datadir}/%{_name}%{_sysconfdir}/%{name}.directory %{buildroot}%{_datadir}/desktop-directories/%{name}.directory

%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}
%find_lang pol

%files -f pol.lang
%doc CHANGELOG.md README.md TRANSLATORS
%license LICENCE
%{_bindir}/%{_name}
%dir %{_datadir}/desktop-directories
%{_datadir}/playonlinux/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{_name}.png
%{_datadir}/desktop-directories/%{name}.directory

%changelog
