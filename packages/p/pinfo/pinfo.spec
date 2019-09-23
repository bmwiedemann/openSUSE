#
# spec file for package pinfo
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pinfo
Version:        0.6.10
Release:        0
Summary:        Lynx-style Info Browser
License:        GPL-2.0+
Group:          Productivity/Publishing/Texinfo
Url:            https://alioth.debian.org/projects/pinfo/
Source:         https://alioth.debian.org/frs/download.php/file/3351/%{name}-%{version}.tar.bz2
Patch1:         pinfo-0.6.9-nul-strings.patch
Patch2:         pinfo-0.6.10-tinfo.patch
Patch3:         pinfo-curses-detection.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pinfo is a curses based, Lynx-style info browser.

%prep
%setup -q
%patch1
%patch2
%patch3 -p1

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
autoreconf -fiv
%configure \
	--with-curses=%{_prefix}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot}/ install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_mandir}/man1/pinfo.1%{ext_man}
%{_infodir}/pinfo.info%{ext_info}
%config %{_sysconfdir}/pinforc
%{_bindir}/pinfo

%changelog
