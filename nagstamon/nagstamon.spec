#
# spec file for package nagstamon
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Lars Vogdt
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


Name:           nagstamon
Version:        2.0.1
Release:        0
Summary:        Nagios status monitor for the desktop
License:        GPL-2.0
Group:          System/Monitoring
Url:            http://nagstamon.ifw-dresden.de/
Source:         Nagstamon-%{version}.tar.bz2
Source1:        %{name}.desktop
BuildRequires:  python3-devel
#
# Fedora dependencies
#
%if 0%{?fedora_version}
BuildRequires:  desktop-file-utils
BuildRequires:  python3-qt5
Requires:       python3
Requires:       python3-SecretStorage
Requires:       python3-beautifulsoup4
Requires:       python3-crypto
Requires:       python3-psutil
Requires:       python3-qt5
Requires:       python3-requests
Requires:       qt5-qtsvg
%endif
#
# openSUSE dependencies
#
%if 0%{?suse_version}
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  python-SecretStorage
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-psutil
BuildRequires:  python3-pycrypto
BuildRequires:  python3-qt5
BuildRequires:  python3-qt5
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       python-SecretStorage
Requires:       python3-beautifulsoup4
Requires:       python3-psutil
Requires:       python3-pycrypto
Requires:       python3-qt5
Requires:       python3-requests
Recommends:     gnome-terminal
Recommends:     rdesktop
Recommends:     sox
Recommends:     tightvnc
%py_requires
%endif
#
# Mandriva dependencies
#
%if 0%{?mandriva_version}
BuildRequires:  desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{!?python3_sitelib: %global python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%description
Nagstamon is a Nagios status monitor which takes place in systray or on desktop
(GNOME, KDE, Windows) as floating statusbar to inform you in realtime about the
status of your Nagios and derivatives monitored network. It allows to connect
to multiple Nagios, Icinga, Opsview, Op5, Check_MK/Multisite and Centreon
servers.

%prep
%setup -q -n Nagstamon
# currently we use our own desktop file
test -f Nagstamon/resources/nagstamon.desktop && rm Nagstamon/resources/nagstamon.desktop
install -Dm644 %{SOURCE1} Nagstamon/resources/nagstamon.desktop

%build
python3 setup.py build

%install
python3 setup.py install \
				--single-version-externally-managed \
				-O1 \
 				--root=%{buildroot} \
				--install-lib=%{python3_sitelib} \
				--prefix=%{_prefix}
mv %{buildroot}/%{_bindir}/nagstamon.py %{buildroot}/%{_bindir}/nagstamon
if [ -d %buildroot/Nagstamon ]; then
    mkdir -p %{buildroot}/%{python3_sitelib}
	my Nagstamon %{buildroot}/%{python3_sitelib}/
fi
# desktop stuff
chmod -x %{buildroot}%{_datadir}/pixmaps/nagstamon.svg
chmod -x %{buildroot}%{python3_sitelib}/Nagstamon/resources/*.svg
for file in $(grep -wlr bin/env %{buildroot}%{python3_sitelib}/Nagstamon/*); do
	chmod +x $file
done
# openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -i %{buildroot}/%{_datadir}/applications/nagstamon.desktop
%endif
# Fedora
%if 0%{?fedora_version}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    --vendor OBS \
    --delete-original \
    %{buildroot}/%{_datadir}/applications/nagstamon.desktop
%endif
# Mandriva
%if 0%{?mandriva_version}
desktop-file-install --vendor="OBS" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/nagstamon.desktop

%post
%{update_menus}

%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog COPYRIGHT LICENSE
%{_datadir}/pixmaps/nagstamon*
%{_datadir}/applications/*nagstamon.desktop
%{python3_sitelib}/Nagstamon/
%{_bindir}/nagstamon
%{_mandir}/man1/nagstamon.1*
%{python3_sitelib}/%{name}*.egg-info

%changelog
