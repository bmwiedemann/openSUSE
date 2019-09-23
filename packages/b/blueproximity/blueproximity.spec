#
# spec file for package blueproximity
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           blueproximity
Version:        1.2.5
Release:        3
License:        GPL-2.0
Summary:        Utility to lock/unlock the screen based on the presence of bluetooth devices
Url:            http://blueproximity.sourceforge.net/
Group:          Hardware/Mobile
Source0:        http://downloads.sourceforge.net/blueproximity/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM blueproximity-suseization.diff rdb@ccb.ac.uk-- Patches for openSUSE
Patch0:         blueproximity-suseization.diff
# PATCH-FIX-UPSTREAM blueproximity-fix-bash-script.diff ncorrare@redhat.com -- Fixes app launch when running from bash scripts
Patch1:         blueproximity-fix-bash-script.diff
# PATCH-FIX-UPSTREAM blueproximity-python-ConfigObj.patch rjsteffan@fedoraproject.org -- Patch for python ConfigObj changes
Patch2:         blueproximity-python-ConfigObj.patch
BuildRequires:  update-desktop-files
# Required due to Patch2
Requires:       python-configobj >= 4.7.0
Requires:       python-gtk >= 2.17
Requires:       python-pybluez
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
BlueProximity adds security to your desktop by automatically locking and
unlocking the screen when you and your phone leave/enter the desk. Think
of a proximity detector for your mobile phone via bluetooth.

%lang_package
%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build

%install

# Create Directory Structure
install -d %{buildroot}%{_datadir}/%{name}/
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/pixmaps/
install -d %{buildroot}%{_datadir}/%{name}/pixmaps/
install -d %{buildroot}%{_mandir}/man1/

# Install Files
install -p -m 0755 start_proximity.sh %{buildroot}%{_bindir}/%{name}
install -p -m 0755 proximity.py %{buildroot}%{_datadir}/%{name}/
install -p -m 0644 proximity.glade %{buildroot}%{_datadir}/%{name}/
install -p -m 0644 doc/blueproximity.1 %{buildroot}%{_mandir}/man1/

# Install Languages
for i in $(ls LANG/); do
install -d %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES/
install -p -m 0644 LANG/$i/LC_MESSAGES/* %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES/
done

# Install Images
for i in $(ls *.svg); do
install -p -m 0644 $i %{buildroot}%{_datadir}/%{name}/pixmaps/
done

# Link in SVG
pushd %{buildroot}%{_datadir}
ln -s ../%{name}/pixmaps/%{name}_base.svg pixmaps/
popd

# Install Menu Item
install -D -m 0644 addons/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
%suse_update_desktop_file -i -r -G "Bluetooth Security Lock" %{name} GNOME GTK Settings HardwareSettings

# Find Languages
%find_lang %{name} %{?no_lang_C}

%if 0%{?suse_version} > 1130

%post
%desktop_database_post
%endif

%if 0%{?suse_version} > 1130

%postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README doc/manual*
%{_bindir}/%{name}
%{_mandir}/man1/blueproximity*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_base.svg
%{_datadir}/pixmaps/blueproximity.xpm

%files lang -f %{name}.lang

%changelog
