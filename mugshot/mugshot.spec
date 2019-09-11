#
# spec file for package mugshot
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


Name:           mugshot
Version:        0.4.1
Release:        0
Summary:        User profile configuration utility
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://launchpad.net/%{name}
# PATCH-FIX-OPENSUSE disable_webcam.patch maurizio.galli@gmail.com -- remove webcam option from menu due to crashes
Patch0:         disable_webcam.patch
Source:         https://launchpad.net/%{name}/0.4/0.4.1/+download/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-dbus-python-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pexpect
BuildRequires:  update-desktop-files
Requires:       python3
Requires:       python3-base
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pexpect
# adds a list of avatars
Recommends:     gnome-control-center-user-faces
Recommends:     %{name}-lang
BuildArch:      noarch

%description
Mugshot is a lightweight user configuration utility that allows you to easily 
update personal user details and avatar.

%lang_package

%prep
%autosetup -p1

%build
%py3_build

%install
# Fix translations not found
install -dm 0755 %{buildroot}%{_datadir}/locale
cp -a build/mo/* %{buildroot}%{_datadir}/locale/

# Fix desktop file not found
install -Dm 0644 build/share/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%py3_install

# Remove unused doc directory
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Fix permissions of .py files
chmod a+x %{buildroot}%{python3_sitelib}/%{name}/*.py
chmod a+x %{buildroot}%{python3_sitelib}/%{name}_lib/*.py

# Fix python-bytecode-inconsistent-mtime.
pushd %{buildroot}%{python3_sitelib}/%{name}_lib
%py3_compile .
popd

# Fix duplicate files
%fdupes -s %{buildroot}%{python3_sitelib}/mugshot_lib/__pycache__/
%fdupes -s %{buildroot}%{_datadir}/icons/hicolor/

%find_lang %{name}

%files -f %{name}.lang

%files
%license COPYING
%doc AUTHORS README
%{python3_sitelib}/%{name}*
%{_datadir}/%{name}
%{_bindir}/%{name}*
%{_datadir}/metainfo/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/**/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/apps.mugshot.gschema.xml
%{_datadir}/man/man1/mugshot.1.gz

%changelog
