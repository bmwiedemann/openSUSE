#
# spec file for package flnews
#
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


Name:           flnews
Version:        0.18
Release:        0
Summary:        Graphical USENET newsreader
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            http://micha.freeshell.org/flnews/
Source:         http://micha.freeshell.org/flnews/src/%{name}-%{version}.tar.bz2
# TODO: upstream
Patch0:         reproducible.patch
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libopenssl-devel
BuildRequires:  zlib-devel
Requires:       xdg-utils

%description
flnews is a FLTK-based client with graphical user interface to read
USENET newsgroups.

%prep
%setup -q
%patch0 -p1
sed -i 's|CFG_XDG_DISABLE=1|CFG_XDG_DISABLE=0|g' CONFIG
sed -i 's|CFG_NLS_PATH="$CFG_PREFIX/lib/$CFG_NAME/nls"|CFG_NLS_PATH="$CFG_PREFIX/share/$CFG_NAME/nls"|g' CONFIG
sed -i 's|CFG_REPRODUCIBLE=0|CFG_REPRODUCIBLE=1|g' CONFIG

%build
export CFLAGS="%{optflags} -fPIE"
export CXXFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
make PREFIX=%{_prefix} %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc CHANGELOG README
%{_bindir}/flnews
%dir %{_datadir}/flnews/
%{_datadir}/flnews/license.txt
%dir %{_datadir}/flnews/nls
%{_datadir}/flnews/nls/de_DE.cat
%{_mandir}/man1/flnews.1%{?ext_man}
%{_datadir}/applications/flnews.desktop
%{_datadir}/icons/hicolor/*/apps/flnews.png

%changelog
