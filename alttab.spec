#
# spec file for package alttab
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


Name:           alttab
Version:        1.4.0
Release:        0
Summary:        Task Switcher
License:        GPL-3.0-only
URL:            https://github.com/sagb/alttab
Source:         https://github.com/sagb/alttab/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libXft-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libpng-devel
BuildRequires:  uthash-devel
BuildRequires:  rubygem(ronn)

%description
alttab is a X11 window switcher designed for minimalistic window managers or standalone X11 session.

%prep
%setup -q

%build
./bootstrap.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc %{_datadir}/doc/alttab/
%{_bindir}/alttab
%{_mandir}/man1/alttab.1%{?ext_man}

%changelog
