#
# spec file for package scim-bridge
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


Name:           scim-bridge
Version:        0.4.17
Release:        0
Summary:        Yet another IM client of SCIM
License:        LGPL-2.1-or-later
Group:          System/I18n/Japanese
URL:            https://github.com/scim-im
Source:         https://github.com/scim-im/scim-bridge/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        xim.d-%{name}
Source99:       baselibs.conf
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
BuildRequires:  libqt4-devel
%endif
BuildRequires:  libtool
BuildRequires:  scim-devel
Recommends:     scim-bridge-gtk2 = %{version}
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
Recommends:     scim-bridge-qt4 = %{version}
%endif
Provides:       scim-bridge-agent

%description
Yet another IM client of SCIM. The immodules of scim-bridge
communicates with SCIM via socket.

scim-bridge has two parts: agent and client. scim-bridge (agent)
stands between SCIM and its clients (immodules), so the clients
only need to communicate with scim-bridge, because scim-bridge
was writen in C, it will solve some C++ ABI problems.

%package gtk2
Summary:        Scim-bridge immodule for GTK+ 2.0
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}
Supplements:    (scim-bridge and gtk2)
Provides:       scim-bridge-client-gtk
Provides:       scim-bridge-gtk = %{version}
Obsoletes:      scim-bridge-gtk <= %{version}
%{scim_gtk2_immodule_requires}

%description gtk2
Scim-bridge-gtk2 is the gtk+-2.0 client of scim-bridge, it provides
another gtk-immodule for SCIM.

%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
%package qt4
Summary:        Scim-bridge immodule for Qt4
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}
Supplements:    (scim-bridge and libqt4)
Provides:       scim-bridge-client-qt4
Provides:       scim-bridge-qt = %{version}
Obsoletes:      scim-bridge-qt <= %{version}

%description qt4
Scim-bridge-qt4 is the qt4 client of scim-bridge, it provides
another qt-immodule for SCIM.
%endif

%prep
%setup -q
./bootstrap

%build
export CFLAGS="%{optflags}"
%configure \
    --disable-static \
    --with-pic \
    --enable-agent \
    --enable-gtk2-immodule \
    --disable-qt3-immodule \
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
    --enable-qt4-immodule \
%else
    --disable-qt4-immodule \
%endif
    --enable-documents \
    --enable-debug

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_sysconfdir}/X11/xim.d/
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xim.d/%{name}
# install symlinks in /etc/X11/xim.d/$lang for all languages
# where scim-bridge might be useful:
PRIORITY=49
pushd %{buildroot}%{_sysconfdir}/X11/xim.d/
    for lang in am ar as bn el fa gu he hi hr ja ka kk kn ko lo ml my \
		pa ru sk vi zh_TW zh_CN zh_HK zh_SG \
		de fr it es nl cs pl da nn nb fi en sv
    do
        mkdir $lang
	pushd $lang
            ln -s ../%{name} $PRIORITY-%{name}
	popd
    done
popd

# fix path
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
mkdir -p %{buildroot}%{_libdir}/qt4/plugins/inputmethods
mv %{buildroot}%{_libdir}/plugins/inputmethods/*.so %{buildroot}%{_libdir}/qt4/plugins/inputmethods/
rm -rf %{buildroot}%{_libdir}/plugins
%endif
mkdir -p %{buildroot}%{_libdir}/gtk-2.0/2.10.0/immodules
mv %{buildroot}%{_libdir}/gtk-2.0/immodules/*.so %{buildroot}%{_libdir}/gtk-2.0/2.10.0/immodules/
rm -rf %{buildroot}%{_libdir}/gtk-2.0/immodules

# install manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

rm doc/Makefile*

%post gtk2
/sbin/ldconfig
%{scim_gtk2_immodule_post}

%postun gtk2
/sbin/ldconfig
%{scim_gtk2_immodule_postun}

%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
%post qt4 -p /sbin/ldconfig
%postun qt4 -p /sbin/ldconfig
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog doc
%dir %{_sysconfdir}/X11/xim.d/
%config %{_sysconfdir}/X11/xim.d/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files gtk2
%{_libdir}/gtk-2.0/2.10.0/immodules/im-%{name}.so

%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
%files qt4
%{_libdir}/qt4/plugins/inputmethods/im-%{name}.so
%endif

%changelog
