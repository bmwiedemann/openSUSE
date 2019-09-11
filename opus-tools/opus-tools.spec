#
# spec file for package opus-tools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Bjørn Lie (zaitor@opensuse.org).
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


Name:           opus-tools
Version:        0.2
Release:        0
Summary:        A set of tools for the opus audio codec
License:        BSD-2-Clause AND GPL-2.0-only
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            http://www.opus-codec.org/
Source:         http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(flac) >= 1.1.3
BuildRequires:  pkgconfig(libopusenc) >= 0.2
BuildRequires:  pkgconfig(ogg) >= 1.3
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile) >= 0.5

%description
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

This is a set of tools for the opus codec.

%prep
%setup -q

%build
%configure \
  --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS
%{_bindir}/opusdec
%{_bindir}/opusenc
%{_bindir}/opusinfo
%{_mandir}/man1/opus*.1%{?ext_man}

%changelog
