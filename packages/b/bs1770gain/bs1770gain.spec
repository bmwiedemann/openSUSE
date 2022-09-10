#
# spec file for package bs1770gain
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           bs1770gain
Version:        0.8.4.1
Release:        0
Summary:        A loudness scanner compliant with ITU-R BS.1770
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://pbelkner.de/projects/web/bs1770gain
Source0:        http://pbelkner.de/count/download.php?path=projects/files/%{name}/%{name}/%{version}&file=%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         remove-inappropriate-text.patch

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)

%description
The command line tool bs1770gain is a loudness scanner compliant with
ITU-R BS.1770 and its flavors EBU R128, ATSC A/85, and ReplayGain 2.0.
It helps normalizing the loudness of audio and video files to the same
level.

%prep
%autosetup -p1

%build
export CPPFLAGS="$CPPFLAGS $(pkg-config --cflags libavutil)"
%configure \
	--with-ffmpeg=%{_prefix} \
	%{nil}
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/bs1770gain

%changelog
