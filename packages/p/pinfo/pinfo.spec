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
Version:        0.6.13
Release:        0
Summary:        Lynx-style Info Browser
License:        GPL-2.0-only
Group:          Productivity/Publishing/Texinfo
URL:            https://github.com/baszoetekouw/pinfo
Source:         https://github.com/baszoetekouw/pinfo/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         https://github.com/baszoetekouw/pinfo/commit/16dba5978146b6d3a540ac7c8f415eda49280847.patch
Patch2:         https://github.com/baszoetekouw/pinfo/commit/23c169877fda839f0634b2d193eaf26de290f141.patch
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
%autosetup -p 1

%build
autoreconf -fiv
export CPPFLAGS="-Wno-error=unused-parameter"
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
%doc NEWS
%{_mandir}/man1/pinfo.1%{?ext_man}
%{_infodir}/pinfo.info%{?ext_info}
%config %{_sysconfdir}/pinforc
%{_bindir}/pinfo

%changelog
