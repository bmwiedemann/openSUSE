#
# spec file for package iwscanner
#
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           iwscanner
Version:        0.2.4
Release:        0
Summary:        Wireless scanner for linux with an easy to use graphic interface
License:        LGPL-2.1+
Group:          System/Monitoring
Url:            http://kuthulu.com/iwscanner/
Source0:        http://kuthulu.com/%{name}/%{name}-%{version}.tgz
Source1:        %{name}.sh
Source2:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  python-devel
Requires:       python-gtk
Requires:       wireless-tools
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
iwScanner is a python/glade wireless scanning utility.

Features:
- Information about detected wireless networks (AP, MAC, Channel, Encryption, etc)
- Chart with signal strenght for every wireless network
- iwScanner GUI is much like the well known application NetStumbler
- Adjustable scanning speed
- Can open and save netdetect (.ndd) and netstumbler (.ns1) file formats

%prep
%setup -q

# Fix typo
sed -i 's|networs|networks|' iwscanner.py

%build

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install files
mkdir -p %{buildroot}%{_datadir}/%{name}
install -Dm 0555 %{name}.py %{buildroot}%{_datadir}/%{name}
for f in SimpleGladeApp.py *.glade ; do
    install -Dm 0644 "$f" %{buildroot}%{_datadir}/%{name}
done

# install icon
install -Dm 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install .desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
