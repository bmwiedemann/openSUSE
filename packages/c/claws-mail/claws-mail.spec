#
# spec file for package claws-mail
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

%if 0%{?suse_version} > 1500
%bcond_with python_gtk
%else
%bcond_without python_gtk
%endif

%define gtk3_ready 0
%if !%{gtk3_ready}
%define favor_gtk2 1
%endif
%if 0%{?suse_version} >= 1330
%bcond_without vcalendar
%else
%bcond_with    vcalendar
%endif
%if 0%{?suse_version} >= 1550
%bcond_without litehtml
%else
%bcond_with    litehtml
%endif
%bcond_with    tnef
Name:           claws-mail
Version:        3.17.6
Release:        0
Summary:        A configurable email client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            https://www.claws-mail.org/
Source:         https://www.claws-mail.org/download.php?file=releases/%{name}-%{version}.tar.xz
Patch0:         libcanberra-gtk3.patch
BuildRequires:  compface-devel
BuildRequires:  db-devel
BuildRequires:  docbook-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  gpgme-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcanberra-devel >= 0.6
BuildRequires:  libcurl-devel
BuildRequires:  libetpan-devel >= 0.57
BuildRequires:  libexpat-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgdata-devel >= 0.17.2
BuildRequires:  libpoppler-glib-devel
BuildRequires:  librsvg-devel >= 2.40.5
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
%if %{with python_gtk}
BuildRequires:  python-gtk-devel
%endif
BuildRequires:  startup-notification-devel
BuildRequires:  texlive-dvips
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-latex
BuildRequires:  texlive-metafont-bin
BuildRequires:  texlive-wasy
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1) >= 0.60
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.60
## FIXME ## - On next version bump please replace with pkgconfig(enchant-2)
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(gnutls) >= 2.2
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sm)
Requires:       pinentry-gtk2
Recommends:     %{name}-lang
Provides:       sylpheed-claws = %{version}
Obsoletes:      sylpheed-claws < %{version}
# The extra-plugin package was merged with version 3.9.1
Obsoletes:      claws-mail-extra-plugins < %{version}
Provides:       claws-mail-extra-plugins = %{version}
# The extra-plugin package was merged with version 3.9.1, also merge the -lang package
Obsoletes:      claws-mail-extra-plugins-lang < %{version}
Provides:       claws-mail-extra-plugins-lang = %{version}
%{?libperl_requires}
%if 0%{?favor_gtk2}
BuildRequires:  gtk2-devel
BuildRequires:  libcanberra-gtk-devel >= 0.6
%else
BuildRequires:  gtk3-devel
BuildRequires:  libcanberra-gtk3-devel >= 0.6
%endif
%if %{with vcalendar}
BuildRequires:  libical-devel >= 2.0.0
%endif
%if 0%{?is_opensuse}
BuildRequires:  pilot-link-devel
%endif
%if %{with tnef}
BuildRequires:  libytnef-devel
%endif
# LiteHTML requires Gumbo which is currently shipped only with Tumbleweed
%if %{with litehtml}
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig(gumbo)
%endif
# libetpan 1.9.2 introduced function mailstream_ssl_set_server_name, which
# will be used by claws-mail if available
%if %{pkg_vcmp libetpan-devel >= 1.9.2}
Requires:       libetpan >= 1.9.2
%endif

%description
Claws Mail (previously known as Sylpheed-Claws) is a
configurable email client and news reader based on the GTK+ GUI
toolkit, and it runs on the X Window System.

When claws-mail is executed for the first time, a configuration "wizard"
(dialog) will appear prompting you for the minimum information necessary to
create a new account.

%package devel
Summary:        Development files for claws-mail
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       claws-mail = %{version}
Requires:       enchant-devel
Requires:       glib2-devel >= 2.28
Requires:       gnutls-devel
Requires:       gpgme-devel
Requires:       gtk2-devel >= 2.24
Requires:       libetpan-devel
Requires:       openldap2-devel
Provides:       claws-mail:%{_includedir}/claws-mail/main.h
# The extra-plugin package was merged with version 3.9.1; as such, also the -devel package merged
Obsoletes:      claws-mail-extra-plugins-devel < %{version}
Provides:       claws-mail-extra-plugins-devel = %{version}

%description devel
Claws Mail (previously known as Sylpheed-Claws) is a
configurable email client and news reader based on the GTK+ GUI
toolkit, and it runs on the X Window System.

This package contains header files for building plugins.

%lang_package

%prep
%setup -q
%if ! 0%{?favor_gtk2}
%patch0 -p1
%endif
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python/' tools/*.py
sed -i 's/#!\/usr\/bin\/env bash/#!\/bin\/bash/' tools/*.sh
sed -i 's/#!\/usr\/bin\/env bash/#!\/bin\/bash/' tools/kdeservicemenu/install.sh

%build
%configure \
        --docdir=%{_datadir}/claws-mail \
        --disable-static \
%if !(0%{?favor_gtk2})
        --enable-gtk3 \
%endif
        --enable-ldap \
        --enable-ipv6 \
%if 0%{?is_opensuse}
        --enable-jpilot \
%else
        --disable-jpilot \
%endif
        --enable-acpi_notifier-plugin \
        --enable-address_keeper-plugin \
        --enable-archive-plugin \
        --enable-att_remover-plugin \
        --enable-attachwarner-plugin \
        --enable-bogofilter-plugin \
        --enable-bsfilter-plugin \
        --enable-clamd-plugin \
        --disable-fancy-plugin \
        --enable-fetchinfo-plugin \
        --enable-mailmbox-plugin \
        --enable-newmail-plugin \
        --enable-notification-plugin \
        --enable-pdf_viewer-plugin \
        --enable-perl-plugin \
        %if %{with python_gtk}
        --enable-python-plugin \
        %endif
        --enable-pgpcore-plugin \
        --enable-pgpmime-plugin \
        --enable-pgpinline-plugin \
        --enable-rssyl-plugin \
        --enable-smime-plugin \
        --enable-spamassassin-plugin \
        --enable-spam_report-plugin \
        %if %{with tnef}
        --enable-tnef_parse-plugin \
        %else
        --disable-tnef_parse-plugin \
        %endif
        %if %{with vcalendar}
        --enable-vcalendar-plugin \
        %else
        --disable-vcalendar-plugin \
        %endif
        --disable-demo-plugin \
        --enable-crash-dialog \
        --enable-startup-notification \
        --enable-compface \
        --enable-libetpan
%make_build

%install
%make_install
# Clean up
find %{buildroot} -type f -name "*.la" -delete -print
# install desktop file
%suse_update_desktop_file claws-mail
# we want to have the icon installed in /usr/share/pixmaps
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp claws-mail-64x64.png %{buildroot}%{_datadir}/pixmaps/
# Tools
cp -r tools %{buildroot}%{_datadir}/%{name}
rm %{buildroot}%{_datadir}/claws-mail/tools/Makefile*
# The ca-certificates are meant for windows. On Linux, it is not used and should not be distributed.
rm %{buildroot}%{_datadir}/claws-mail/tools/ca-certificates.crt
mv %{buildroot}%{_datadir}/claws-mail/tools/README ./README.tools
# fixing permissions
chmod 755 %{buildroot}%{_datadir}/claws-mail/tools/*
chmod 644 %{buildroot}%{_datadir}/claws-mail/tools/multiwebsearch.conf
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_libdir}/%{name}/plugins/
install -d %{buildroot}%{_sysconfdir}/skel/.claws-mail/
cat <<EOF > %{buildroot}%{_sysconfdir}/skel/.claws-mail/clawsrc
[Plugins_GTK2]
%{_libdir}/claws-mail/plugins/pgpcore.so
%{_libdir}/claws-mail/plugins/pgpinline.so
%{_libdir}/claws-mail/plugins/pgpmime.so
%{_libdir}/claws-mail/plugins/smime.so
EOF

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.tools TODO
%{_bindir}/claws-mail
%dir %{_libdir}/claws-mail
%dir %{_libdir}/claws-mail/plugins
%{_libdir}/claws-mail/plugins/*.so
%{_libdir}/claws-mail/plugins/*.deps
%{_datadir}/applications/claws-mail.desktop
%{_datadir}/icons/hicolor/*/apps/claws-mail.png
%{_datadir}/pixmaps/claws-mail-64x64.png
%dir %{_datadir}/claws-mail
%doc %{_datadir}/claws-mail/RELEASE_NOTES
%doc %{_datadir}/claws-mail/manual/
%dir %{_datadir}/claws-mail/tools
%{_datadir}/claws-mail/tools/*.sh
%{_datadir}/claws-mail/tools/*.pl
%{_datadir}/claws-mail/tools/*.py
%{_datadir}/claws-mail/tools/*.conf
%{_datadir}/claws-mail/tools/tb2claws-mail
%{_datadir}/claws-mail/tools/u*
%{_datadir}/claws-mail/tools/kdeservicemenu/
%{_mandir}/man1/claws-mail.1%{?ext_man}
%config(noreplace) %{_sysconfdir}/skel/.claws-mail/

%files devel
%{_includedir}/claws-mail/
%{_libdir}/pkgconfig/claws-mail.pc

%files lang -f %{name}.lang

%changelog
