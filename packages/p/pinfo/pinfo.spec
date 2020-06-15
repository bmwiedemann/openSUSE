#
# spec file for package pinfo
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pinfo
Version:        0.6.10
Release:        0
Summary:        Lynx-style Info Browser
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/Texinfo
URL:            https://alioth.debian.org/projects/pinfo/
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

%description
Pinfo is a curses based, Lynx-style info browser.

%prep
%setup -q
%patch1
%patch2
%patch3 -p1

%build
export CFLAGS="%{optflags} -fcommon"
autoreconf -fiv
%configure \
	--with-curses=%{_prefix}
%make_build

%install
%make_install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_mandir}/man1/pinfo.1%{?ext_man}
%{_infodir}/pinfo.info%{?ext_info}
%config %{_sysconfdir}/pinforc
%{_bindir}/pinfo

%changelog
