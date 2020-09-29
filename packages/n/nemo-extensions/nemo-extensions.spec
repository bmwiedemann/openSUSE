#
# spec file for package nemo-extensions
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


# Disable build for nemo-extension-gtkhash for now, no clue why it cause nemo to segfault.
# Do not package nemo-extension-media-columns for now: slows Nemo down.
# nemo-extension-terminal 'requires' two versions, confusing typelib finder.
%define __requires_exclude typelib\\((Vte))\ =
%define _version 4.0.0
Name:           nemo-extensions
Version:        4.6.0
Release:        0
Summary:        Set of extensions for Nemo, the Cinnamon file manager
License:        GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/nemo-extensions
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE nemo-seahorse_no-nautilus-conflicts.patch sor.alexei@meowr.ru -- Strip conflicted with nautilus-extension-seahorse files.
Patch0:         nemo-seahorse_no-nautilus-conflicts.patch
# PATCH-FIX-OPENSUSE nemo-dropbox_no-dropbox-bin.patch sor.alexei@meowr.ru -- Strip dropbox binary installation from nemo-dropbox.
Patch1:         nemo-dropbox_no-dropbox-bin.patch
# PATCH-FIX-OPENSUSE nemo-gtkhash_openssl-1.1.patch sor.alexei@meowr.ru -- Add basic OpenSSL 1.1+ compatibility in nemo-gtkhash.
Patch3:         nemo-gtkhash_openssl-1.1.patch
# PATCH-FIX-UPSTREAM nemo-share-prevent-privilege-escalation.patch bsc#1084703 -- Prevent unprivileged users from adding other users to sambashare (commit a831e7b).
Patch4:         nemo-share-prevent-privilege-escalation.patch
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libtool
BuildRequires:  mbedtls-devel
BuildRequires:  meld
BuildRequires:  meson
BuildRequires:  mhash-devel
BuildRequires:  nemo-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(cjs-1.0)
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(cryptui-0.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(evince-view-3.0)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(xreader-document-1.5)
BuildRequires:  pkgconfig(xreader-view-1.5)
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
%else
BuildRequires:  python-devel
BuildRequires:  python-distutils-extra
BuildRequires:  python-docutils
BuildRequires:  python-setuptools
%endif

%description
Set of extensions for Nemo, the Cinnamon file manager.

%if 0%{?suse_version} >= 1500
%package -n python3-nemo
%else
%package -n python-nemo
%endif
Summary:        Python bindings for the Nemo File manager
License:        GPL-2.0-only
Group:          System/GUI/Other
Requires:       nemo >= %{_version}
# nemo-python was last used in openSUSE 13.2.
Provides:       nemo-python = %{version}
Obsoletes:      nemo-python < %{version}

%if 0%{?suse_version} >= 1500
Provides:       python3-nemo-devel = %{version}
Obsoletes:      python2-nemo-devel < %{version}
Provides:       python2-nemo = %{version}
Obsoletes:      python2-nemo < %{version}
# python-nemo was last used in openSUSE Leap 42.3.
Provides:       python-nemo = %{version}
Obsoletes:      python-nemo < %{version}

%description -n python3-nemo
%else
Provides:       python-nemo-devel = %{version}

%description -n python-nemo
%endif
Includes Python bindings for the Nemo Filemanager.

%package -n nemo-extension-audio-tab
Summary:        Audio tag information for Nemo file manager
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires:       python3-mutagen
Requires:       python3-nemo = %{version}
%else
Requires:       python-mutagen
Requires:       python-nemo = %{version}
%endif

%description -n nemo-extension-audio-tab
View audio tag information from the file manager's properties tab.

%package -n nemo-extension-compare
Summary:        Context Menu comparison extension for Nemo file manager
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Requires:       meld
Requires:       nemo >= %{_version}
Requires:       python-gtk
Recommends:     %{name}-lang
# nemo-compare was last used in openSUSE 13.2.
Provides:       nemo-compare = %{version}
Obsoletes:      nemo-compare < %{version}
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires:       python3-gobject
Requires:       python3-nemo = %{version}
Requires:       python3-pyxdg
%else
Requires:       python-gobject
Requires:       python-nemo = %{version}
Requires:       python-xdg
%endif

%description -n nemo-extension-compare
Simple context menu file comparison extension for Nemo, inspired by
the discontinued 'diff-ext' extension. By default it uses 'meld' to
do the comparison and provides "Compare", "Compare to ~/foo/bar" and
"Compare Later" in Nemo context menu. Using the configurator tool
you can choose your favourite compare tool for one-on-one,
three-way and multi-compare situations.

%package -n nemo-extension-dropbox
Summary:        DropBox support for the Nemo Filemanager
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Requires:       dropbox
Requires:       nemo >= %{_version}
Supplements:    (dropbox and nemo)
# nemo-dropbox was last used in openSUSE 13.2.
Provides:       nemo-dropbox = %{version}
Obsoletes:      nemo-dropbox < %{version}

%description -n nemo-extension-dropbox
Nemo-dropbox adds DropBox support to the Nemo filemanager.

%package -n nemo-extension-emblems
Summary:        Change a directory or file emblem in Nemo
License:        GPL-3.0-only
Group:          System/GUI/Other
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
# nemo-emblems was last used in openSUSE 13.2.
Provides:       nemo-emblems = %{version}
Obsoletes:      nemo-emblems < %{version}
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
%else
Requires:       python-gobject
Requires:       python-gobject-Gdk
%endif

%description -n nemo-extension-emblems
Change a directory or a file emblem in Nemo, the Cinnamon desktop
file manager.

%package -n nemo-extension-fileroller
Summary:        Fileroller support for the Nemo Filemanager
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Requires:       file-roller
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
Supplements:    (nemo and file-roller)
# nemo-fileroller was last used in openSUSE 13.2.
Provides:       nemo-fileroller = %{version}
Obsoletes:      nemo-fileroller < %{version}

%description -n nemo-extension-fileroller
Nemo-fileroller adds File-roller support to the Nemo file manager.

%package -n nemo-extension-gtkhash
Summary:        Nemo extension for computing checksums and more using gtkhash
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
# nemo-gtkhash was last used in openSUSE 13.2.
Obsoletes:      nemo-gtkhash < %{version}
Provides:       nemo-gtkhash = %{version}
%glib2_gsettings_schema_requires

%description -n nemo-extension-gtkhash
The GtkHash extension for nemo which allows users to compute
message digests or checksums using the mhash library.
Currently supported hash functions include MD5, MD6, SHA1, SHA256,
SHA512, RIPEMD, TIGER and WHIRLPOOL.

%package -n nemo-extension-image-converter
Summary:        Nemo extension to mass resize or rotate images
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       ImageMagick
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
# nemo-image-converter was last used in openSUSE 13.2.
Provides:       nemo-image-converter = %{version}
Obsoletes:      nemo-image-converter < %{version}

%description -n nemo-extension-image-converter
This package adds a "Resize Images..." menu item to the context
menu of all images. This opens a dialog where you set the desired
image size and file name. A click on "Resize" finally resizes the
image(s) using ImageMagick's convert tool.

%package -n nemo-extension-pastebin
Summary:        Pastebin extension for Nemo file manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
# nemo-pastebin was last used in openSUSE 13.2.
Provides:       nemo-pastebin = %{version}
Obsoletes:      nemo-pastebin < %{version}
BuildArch:      noarch
%glib2_gsettings_schema_requires
%if 0%{?suse_version} >= 1500
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pyxdg
%else
Requires:       python-gobject
Requires:       python-gobject-Gdk
Requires:       python-xdg
%endif

%description -n nemo-extension-pastebin
nemo-pastebin is an extension for the Nemo file manager, which
allows users to send files to pastebins just a right-click away.

%package -n nemo-extension-preview
Summary:        A quick previewer for Nemo file manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       gstreamer-plugins-good
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
# nemo-preview was last used in openSUSE 13.2.
Provides:       nemo-extension-preview-devel = %{version}
Provides:       nemo-preview = %{version}
Obsoletes:      nemo-preview < %{version}

%description -n nemo-extension-preview
This is NemoPreview, a quick previewer for Nemo, the Cinnamon
desktop file manager.

%package -n nemo-extension-repairer
Summary:        Nemo extension for filename encoding repair
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
# nemo-repairer was last used in openSUSE 13.2.
Provides:       nemo-repairer = %{version}
Obsoletes:      nemo-repairer < %{version}

%description -n nemo-extension-repairer
This is a Nemo extension which repairs filename which uses wrong
encoding in Nemo. This extension provides the context menu for any
file whose filename uses wrong encoding, so that you cannot read the
filename in Nemo.

You can find a candidate for filename in context menu or submenu.
This extension also provides a decoded name for URL encoded filename.

%package -n nemo-extension-seahorse
Summary:        OpenPGP encryption/decryption extension for Nemo file manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       nautilus-extension-seahorse >= 3.0
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
Supplements:    (nemo and seahorse)
# nemo-seahorse was last used in openSUSE 13.2.
Provides:       nemo-seahorse = %{version}
Obsoletes:      nemo-seahorse < %{version}

%description -n nemo-extension-seahorse
seahorse nemo is an extension for nemo which allows encryption
and decryption of OpenPGP files using GnuPG.

%package -n nemo-extension-share
Summary:        Samba share extension for Nemo file manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       nemo >= %{_version}
Recommends:     %{name}-lang
Recommends:     samba
Supplements:    (nemo and samba)
# nemo-share was last used in openSUSE 13.2.
Provides:       nemo-share = %{version}
Obsoletes:      nemo-share < %{version}

%description -n nemo-extension-share
Nemo Share allows you to quickly share a folder from the Cinnamon
Nemo file manager without requiring root access.

%package -n nemo-extension-terminal
Summary:        Nemo extension to enable an embedded terminal
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Requires:       nemo >= %{_version}
# nemo-terminal was last used in openSUSE 13.2.
Provides:       nemo-terminal = %{version}
Obsoletes:      nemo-terminal < %{version}
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-nemo = %{version}
%else
Requires:       python-gobject
Requires:       python-gobject-Gdk
Requires:       python-nemo = %{version}
%endif

%description -n nemo-extension-terminal
Nemo Terminal is an embedded terminal for Nemo, the Cinnamon file
manager. It embeds a terminal pane into Nemo that is accessible by
hotkey (default F4) and automatically follows the currently active
directory in Nemo.

%prep
%autosetup -p1

find -name COPYING.GPL3 -exec chmod -x '{}' \;

%build
pushd nemo-pastebin
export CFLAGS="%{optflags} -fcommon"
export CXXFLAGS="%{optflags} -fcommon"
%py3_build
popd

pushd nemo-fileroller
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build
popd

pushd nemo-python
%meson
%meson_build
popd

pushd nemo-terminal
%py3_build
popd

pushd nemo-preview
NOCONFIGURE=1 ./autogen.sh
intltoolize -f
%configure
%make_build
popd

pushd nemo-emblems
%py3_build
popd

pushd nemo-image-converter
NOCONFIGURE=1 gnome-autogen.sh
%configure
%make_build
popd

pushd nemo-compare
%py3_build
popd

pushd nemo-dropbox
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build
popd

pushd nemo-repairer
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build
popd

pushd nemo-seahorse
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build
popd

pushd nemo-share
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build
popd

# pushd nemo-gtkhash
# NOCONFIGURE=1 ./autogen.sh
# %%configure \
#             --with-gtk=3.0 \
#             --enable-linux-crypto \
#             --enable-gcrypt \
#             --enable-libcrypto \
#             --enable-mbedtls \
#             --enable-nettle \
#             --enable-nss \
#             --enable-mhash \
#             --enable-nemo
# 
# %%make_build
# popd

pushd nemo-audio-tab
%py3_build
popd

%install
pushd nemo-pastebin
%py3_install
popd

pushd nemo-fileroller
%make_install
popd

pushd nemo-python
%meson_install
popd

pushd nemo-terminal
%py3_install
popd

pushd nemo-preview
%make_install
popd

pushd nemo-emblems
%py3_install
popd

pushd nemo-image-converter
%make_install
popd

pushd nemo-compare
%py3_install
popd

pushd nemo-dropbox
%make_install
popd

pushd nemo-repairer
%make_install
popd

pushd nemo-seahorse
%make_install
popd

pushd nemo-share
%make_install
popd

# pushd nemo-gtkhash
# %%make_install
# popd

pushd nemo-audio-tab
%py3_install
popd

%find_lang nemo-preview
%find_lang nemo-share
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}/%{_prefix}

%if 0%{?suse_version} >= 1500
%post -n python3-nemo -p /sbin/ldconfig
%postun -n python3-nemo -p /sbin/ldconfig
%else
%post -n python-nemo -p /sbin/ldconfig
%postun -n python-nemo -p /sbin/ldconfig
%endif

%post -n nemo-extension-dropbox -p /sbin/ldconfig
%postun -n nemo-extension-dropbox -p /sbin/ldconfig
%post -n nemo-extension-fileroller -p /sbin/ldconfig
%postun -n nemo-extension-fileroller -p /sbin/ldconfig
%post -n nemo-extension-image-converter -p /sbin/ldconfig
%postun -n nemo-extension-image-converter -p /sbin/ldconfig
%post -n nemo-extension-preview -p /sbin/ldconfig
%postun -n nemo-extension-preview -p /sbin/ldconfig
%post -n nemo-extension-seahorse -p /sbin/ldconfig
%postun -n nemo-extension-seahorse -p /sbin/ldconfig
%post -n nemo-extension-repairer -p /sbin/ldconfig
%postun -n nemo-extension-repairer -p /sbin/ldconfig
%post -n nemo-extension-share -p /sbin/ldconfig
%postun -n nemo-extension-share -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post -n nemo-extension-gtkhash
/sbin/ldconfig
%glib2_gsettings_schema_post

%postun -n nemo-extension-gtkhash
/sbin/ldconfig
%glib2_gsettings_schema_postun

%post -n nemo-extension-pastebin
%glib2_gsettings_schema_post

%postun -n nemo-extension-pastebin
%glib2_gsettings_schema_postun

%post -n nemo-extension-terminal
%glib2_gsettings_schema_post

%postun -n nemo-extension-terminal
%glib2_gsettings_schema_postun
%endif

%if 0%{?suse_version} >= 1500
%files -n python3-nemo
%else
%files -n python-nemo
%endif
%license nemo-python/COPYING
%doc nemo-python/AUTHORS nemo-python/debian/changelog
%{_libdir}/nemo/extensions-3.0/libnemo-python.so
%{_libdir}/pkgconfig/nemo-python.pc
%dir %{_datadir}/nemo-python/
%dir %{_datadir}/nemo-python/extensions/

%files -n nemo-extension-audio-tab
%license nemo-audio-tab/COPYING*
%doc nemo-audio-tab/debian/changelog
%{_datadir}/nemo-python/extensions/nemo-audio-tab.py*
%dir %{_datadir}/nemo-audio-tab
%{_datadir}/nemo-audio-tab/nemo-audio-tab.glade
%{python3_sitelib}/nemo_audio_tab-%{version}-py?.?.egg-info

%files -n nemo-extension-compare
%license nemo-compare/nemo-compare/COPYING*
%doc nemo-compare/debian/changelog
%{_bindir}/nemo-compare-preferences
%{_datadir}/nemo-compare/
%{python3_sitelib}/nemo_compare-%{version}-py?.?.egg-info
%{_datadir}/nemo-python/extensions/nemo-compare.py

%files -n nemo-extension-dropbox
%license nemo-dropbox/COPYING
%doc nemo-dropbox/AUTHORS nemo-dropbox/debian/changelog
%exclude %{_libdir}/nemo/extensions-3.0/libnemo-dropbox.a
%{_libdir}/nemo/extensions-3.0/libnemo-dropbox.so
%{_datadir}/nemo-dropbox/

%files -n nemo-extension-emblems
%license nemo-emblems/COPYING*
%doc nemo-emblems/debian/changelog
%{_datadir}/nemo-python/extensions/nemo-emblems.py*
%{python3_sitelib}/nemo_emblems-%{version}-py?.?.egg-info

%files -n nemo-extension-fileroller
%license nemo-fileroller/COPYING
%doc nemo-fileroller/debian/changelog
%exclude %{_libdir}/nemo/extensions-3.0/libnemo-fileroller.a
%{_libdir}/nemo/extensions-3.0/libnemo-fileroller.so

%files -n nemo-extension-gtkhash
%license nemo-gtkhash/COPYING
%doc nemo-gtkhash/AUTHORS nemo-gtkhash/debian/changelog
# %%{_bindir}/gtkhash
# %%{_datadir}/glib-2.0/schemas/app.gtkhash.gschema.xml
# %%dir %%{_datadir}/nemo-gtkhash
# %%{_datadir}/nemo-gtkhash/gtkhash.xml.gz
# %%{_libdir}/nemo/extensions-3.0/libgtkhash-properties.so
# %%{_datadir}/glib-2.0/schemas/org.nemo.extensions.gtkhash.gschema.xml
# %%dir %%{_datadir}/nemo-gtkhash/nautilus
# %%{_datadir}/nemo-gtkhash/nautilus/gtkhash-properties.xml.gz

%files -n nemo-extension-image-converter
%license nemo-image-converter/COPYING
%doc nemo-image-converter/AUTHORS nemo-image-converter/debian/changelog
%{_libdir}/nemo/extensions-3.0/libnemo-image-converter.so
%{_datadir}/nemo-image-converter/

%files -n nemo-extension-pastebin
%license nemo-pastebin/COPYING
%doc nemo-pastebin/debian/changelog
%{_bindir}/nemo-pastebin-configurator
%{_datadir}/nemo-pastebin/
%{_datadir}/nemo-python/extensions/nemo-pastebin.py
%{_datadir}/icons/hicolor/*/apps/nemo-pastebin.png
%{_datadir}/icons/hicolor/scalable/apps/nemo-pastebin.svg
%{_datadir}/glib-2.0/schemas/nemo-pastebin.gschema.xml
%{python3_sitelib}/nemo_pastebin-%{version}-py?.?.egg-info

%files -n nemo-extension-preview -f nemo-preview.lang
%license nemo-preview/COPYING
%doc nemo-preview/AUTHORS nemo-preview/debian/changelog
%{_bindir}/nemo-preview
%{_libexecdir}/nemo-preview-start
%{_libdir}/nemo-preview/
%{_datadir}/nemo-preview/
%{_datadir}/dbus-1/services/org.nemo.Preview.service

%files -n nemo-extension-repairer
%license nemo-repairer/COPYING
%doc nemo-repairer/AUTHORS nemo-repairer/README
%{_libdir}/nemo/extensions-3.0/libnemo-filename-repairer.so
%{_bindir}/nemo-filename-repairer
%{_datadir}/nemo-filename-repairer/

%files -n nemo-extension-seahorse
%license nemo-seahorse/COPYING
%doc nemo-seahorse/debian/changelog
%{_libdir}/nemo/extensions-3.0/libnemo-seahorse.so

%files -n nemo-extension-share -f nemo-share.lang
%license nemo-share/COPYING
%doc nemo-share/AUTHORS nemo-share/debian/changelog
%{_libdir}/nemo/extensions-3.0/libnemo-share.so
%exclude %{_libdir}/nemo/extensions-3.0/libnemo-share.a
%{_datadir}/nemo-share/
%{_datadir}/polkit-1/actions/org.nemo.share.samba_install.policy

%files -n nemo-extension-terminal
%license nemo-terminal/COPYING
%doc nemo-terminal/AUTHORS nemo-terminal/debian/changelog
%{_bindir}/nemo-terminal-prefs
%{_datadir}/nemo-terminal/
%{_datadir}/nemo-python/extensions/nemo_terminal.py
%{_datadir}/glib-2.0/schemas/org.nemo.extensions.nemo-terminal.gschema.xml
%{python3_sitelib}/nemo_terminal-%{version}-py?.?.egg-info

%changelog
