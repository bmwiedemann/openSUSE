#
# spec file for package sound-theme-freedesktop
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           sound-theme-freedesktop
Version:        0.8
Release:        0
# For details on the licenses used, see CREDITS.
Summary:        freedesktop.org sound theme
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            http://0pointer.de/public/sound-theme-freedesktop.tar.gz
Source0:        http://people.freedesktop.org/~mccann/dist/%{name}-%{version}.tar.bz2
# COPYING in the tarball is a 0-byte file
Source1:        gpl-2.0.txt
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  intltool
Requires(post): /bin/touch
Requires(postun): /bin/touch
BuildArch:      noarch

%description
The default freedesktop.org sound theme following the XDG theming
specification.	(http://0pointer.de/public/sound-theme-spec.html).

%prep
%setup -q
if [ ! -s COPYING ]; then
  cp %{SOURCE1} COPYING
fi

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}%{_datadir}

%post
/bin/touch --no-create %{_datadir}/sounds/freedesktop

%postun
/bin/touch --no-create %{_datadir}/sounds/freedesktop

%files
%doc README
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.oga

%changelog
