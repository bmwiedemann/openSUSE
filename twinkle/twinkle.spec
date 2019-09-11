#
# spec file for package twinkle
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           twinkle
Version:        1.10.2
Release:        0
Summary:        A SIP Soft Phone
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/SIP/Clients
Url:            https://twinkle.dolezel.info/
Source:         https://github.com/LubosD/%{name}/archive/v%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  flex
BuildRequires:  libgsm-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libzrtpcpp-devel >= 2.0.0
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-devel
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(commoncpp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%if 0%{?suse_version} <= 1320
BuildRequires:  boost-devel
%endif
%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?is_opensuse})
BuildRequires:  ilbc-devel
%else
BuildRequires:  ilbc
%endif

%description
Twinkle is a SIP-based soft phone for making telephone calls over IP
networks.


%prep
%setup -q

%build
%cmake \
  -DWITH_ZRTP=ON \
  -DWITH_SPEEX=ON \
  -DWITH_ILBC=ON \
  -DWITH_GSM=ON \
  -DWITH_ALSA=ON \
  -DWITH_QT5=ON
make %{?_smp_mflags}

%install
%cmake_install
install -d 755 %{buildroot}%{_datadir}/pixmaps
%suse_update_desktop_file -c twinkle Twinkle "SIP VoIP Phone" twinkle twinkle Network Telephony
%fdupes %{buildroot}%{_prefix}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-, root, root)
%doc AUTHORS README.md
%license COPYING
%{_bindir}/twinkle
%{_bindir}/twinkle-console
%{_datadir}/%{name}
%{_datadir}/pixmaps/twinkle.png
%{_datadir}/icons/hicolor
%{_datadir}/applications/twinkle.desktop
%{_mandir}/man1/twinkle.1.gz

%changelog
