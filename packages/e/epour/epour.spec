#
# spec file for package epour
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           epour
Version:        0.7.0
Release:        0
Summary:        BitTorrent client
License:        GPL-3.0
Group:          Productivity/Networking/File-Sharing 
Url:			https://phab.enlightenment.org/w/projects/epour/
Source0:        https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	python3-distutils-extra
BuildRequires:	intltool
buildroot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif

Requires:       python3-dbus-python
Requires:       python3-efl
Requires:       python3-libtorrent-rasterbar
Requires:       python3-xdg

Recommends:     %{name}-lang = %{version}

%lang_package

%description
EFL and libtorrent based BitTorrent client.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root "%{buildroot}"
%if 0%{?suse_version}
%fdupes %{buildroot}/%{_datadir}
%suse_update_desktop_file epour
%endif
rm -rf "%{buildroot}/%{_datadir}/doc"
%find_lang %{name}

%files
%defattr(-,root,root,-)
%doc README AUTHORS TODO
%{_bindir}/epour
%{python3_sitelib}/epour*
%{_datadir}/icons/*
%{_datadir}/applications/epour.desktop
%{_datadir}/%{name}/

%files lang -f %{name}.lang

%changelog
