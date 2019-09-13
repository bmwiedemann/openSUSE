#
# spec file for package madplay
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


Name:           madplay
Version:        0.15.2b
Release:        0
Summary:        MPEG audio decoder and player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://www.underbit.com/products/mad/
Source:         ftp://ftp.mars.org/pub/mpeg/madplay-%{version}.tar.gz
# PATCH-FIX-OPENSUSE madplay-switch-to-new-alsa-api.patch
Patch0:         madplay-switch-to-new-alsa-api.patch
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang

%description
madplay is a command-line MPEG audio decoder and player based on the MAD
library (libmad).

%lang_package

%package -n abxtest
Summary:        Double-blind ABX comparison testing script
Group:          Productivity/Multimedia/Sound/Utilities

%description -n abxtest
abxtest is a tool for conducting listening (or other subjective) tests to
determine whether a listener can discern a difference between two subjects
under test, denoted A and B.

%prep
%setup -q
%patch0 -p1

%build
%configure \
  --with-alsa \
  --enable-experimental
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install
rm -rf "%{buildroot}%{_datadir}/locale/no"
%find_lang %{name}

%files
%license COPYING COPYRIGHT
%doc CHANGES CREDITS README TODO
%{_bindir}/madplay
%{_mandir}/man1/madplay.1%{?ext_man}

%files lang -f %{name}.lang

%files -n abxtest
%{_bindir}/abxtest
%{_mandir}/man1/abxtest.1%{?ext_man}

%changelog
