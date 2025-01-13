#
# spec file for package nemo-extensions
#
# Copyright (c) 2025 SUSE LLC
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


%define         _version 6.0.0
Name:           nemo-extensions
Version:        6.4.0
Release:        0
Summary:        Set of extensions for Nemo, the Cinnamon file manager
License:        GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later
URL:            https://github.com/linuxmint/nemo-extensions
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-hwcaps.patch
Patch1:         gnome-installer-removal.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  meld
BuildRequires:  meson
BuildRequires:  mhash-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
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
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(libnemo-extension)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(mbedtls)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(xreader-document-1.5)
BuildRequires:  pkgconfig(xreader-view-1.5)

%description
Set of extensions for Nemo, the Cinnamon file manager.

%package -n python3-nemo
Summary:        Python bindings for the Nemo File manager
License:        GPL-2.0-only
Requires:       nemo >= %{_version}
# nemo-python was last used in openSUSE 13.2.
Provides:       nemo-python = %{version}
Obsoletes:      nemo-python < %{version}

Provides:       python3-nemo-devel = %{version}
Obsoletes:      python2-nemo-devel < %{version}
Provides:       python2-nemo = %{version}
Obsoletes:      python2-nemo < %{version}
# python-nemo was last used in openSUSE Leap 42.3.
Provides:       python-nemo = %{version}
Obsoletes:      python-nemo < %{version}

%description -n python3-nemo
Provides:       python-nemo-devel = %{version}
Includes Python bindings for the Nemo Filemanager.

%package -n nemo-extension-audio-tab
Summary:        Audio tag information for Nemo file manager
License:        GPL-3.0-or-later
Requires:       nemo >= %{_version}
BuildArch:      noarch
Requires:       python3-mutagen
Requires:       python3-nemo = %{version}

%description -n nemo-extension-audio-tab
View audio tag information from the file manager's properties tab.

%package -n nemo-extension-compare
Summary:        Context Menu comparison extension for Nemo file manager
License:        GPL-3.0-or-later
Requires:       meld
Requires:       nemo >= %{_version}
# nemo-compare was last used in openSUSE 13.2.
Provides:       nemo-compare = %{version}
Obsoletes:      nemo-compare < %{version}
BuildArch:      noarch
Requires:       python3-gobject
Requires:       python3-nemo = %{version}
Requires:       python3-pyxdg

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
Requires:       nemo >= %{_version}
# nemo-emblems was last used in openSUSE 13.2.
Provides:       nemo-emblems = %{version}
Obsoletes:      nemo-emblems < %{version}
BuildArch:      noarch
Requires:       python3-gobject
Requires:       python3-gobject-Gdk

%description -n nemo-extension-emblems
Change a directory or a file emblem in Nemo, the Cinnamon desktop
file manager.

%package -n nemo-extension-fileroller
Summary:        Fileroller support for the Nemo Filemanager
License:        GPL-3.0-or-later
Requires:       file-roller
Requires:       nemo >= %{_version}
Supplements:    (nemo and file-roller)
# nemo-fileroller was last used in openSUSE 13.2.
Provides:       nemo-fileroller = %{version}
Obsoletes:      nemo-fileroller < %{version}

%description -n nemo-extension-fileroller
Nemo-fileroller adds File-roller support to the Nemo file manager.

%package -n nemo-extension-image-converter
Summary:        Nemo extension to mass resize or rotate images
License:        GPL-2.0-or-later
Requires:       ImageMagick
Requires:       nemo >= %{_version}
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
Requires:       nemo >= %{_version}
# nemo-pastebin was last used in openSUSE 13.2.
Provides:       nemo-pastebin = %{version}
Obsoletes:      nemo-pastebin < %{version}
BuildArch:      noarch
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pyxdg

%description -n nemo-extension-pastebin
nemo-pastebin is an extension for the Nemo file manager, which
allows users to send files to pastebins just a right-click away.

%package -n nemo-extension-preview
Summary:        A quick previewer for Nemo file manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       gstreamer-plugins-good
Requires:       nemo >= %{_version}
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
Requires:       nemo >= %{_version}
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
Requires:       nautilus-extension-seahorse >= 3.0
Requires:       nemo >= %{_version}
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
Requires:       nemo >= %{_version}
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
Requires:       nemo >= %{_version}
# nemo-terminal was last used in openSUSE 13.2.
Provides:       nemo-terminal = %{version}
Obsoletes:      nemo-terminal < %{version}
BuildArch:      noarch
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-nemo = %{version}

%description -n nemo-extension-terminal
Nemo Terminal is an embedded terminal for Nemo, the Cinnamon file
manager. It embeds a terminal pane into Nemo that is accessible by
hotkey (default F4) and automatically follows the currently active
directory in Nemo.

%prep
%autosetup -p1

%build
pushd nemo-pastebin
export CFLAGS="%{optflags} -fcommon"
export CXXFLAGS="%{optflags} -fcommon"
%py3_build
popd

pushd nemo-fileroller
%meson
%meson_build
popd

pushd nemo-python
%meson
%meson_build
popd

pushd nemo-terminal
%py3_build
popd

pushd nemo-preview
%meson
%meson_build
popd

pushd nemo-emblems
%py3_build
popd

pushd nemo-image-converter
%meson
%meson_build
popd

pushd nemo-compare
%py3_build
popd

pushd nemo-dropbox
%meson
%meson_build
popd

pushd nemo-repairer
%meson
%meson_build
popd

pushd nemo-seahorse
%meson
%meson_build
popd

pushd nemo-share
%meson
%meson_build
popd

pushd nemo-audio-tab
%py3_build
popd

%install
pushd nemo-pastebin
%py3_install
popd

pushd nemo-fileroller
%meson_install
popd

pushd nemo-python
%meson_install
popd

pushd nemo-terminal
%py3_install
popd

pushd nemo-preview
%meson_install
popd

pushd nemo-emblems
%py3_install
popd

pushd nemo-image-converter
%meson_install
popd

pushd nemo-compare
%py3_install
popd

pushd nemo-dropbox
%meson_install
popd

pushd nemo-repairer
%meson_install
popd

pushd nemo-seahorse
%meson_install
popd

pushd nemo-share
%meson_install
popd

pushd nemo-audio-tab
%py3_install
popd

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete -print

%fdupes %{buildroot}
chmod 744 %{buildroot}%{_datadir}/nemo-compare/utils.py
chmod 744 %{buildroot}%{_datadir}/nemo-python/extensions/nemo-audio-tab.py
chmod 744 %{buildroot}%{_datadir}/nemo-python/extensions/nemo-compare.py

# Manually let install samba from our package manager.
rm -r %{buildroot}%{_datadir}/nemo-share/install-samba

# Already included.
rm -r %{buildroot}%{_datadir}/licenses/nemo-dropbox/COPYING

%python_compileall

%ldconfig_scriptlets -n python3-nemo

%ldconfig_scriptlets -n nemo-extension-dropbox

%ldconfig_scriptlets -n nemo-extension-fileroller

%ldconfig_scriptlets -n nemo-extension-image-converter

%ldconfig_scriptlets -n nemo-extension-preview

%ldconfig_scriptlets -n nemo-extension-seahorse

%ldconfig_scriptlets -n nemo-extension-repairer

%ldconfig_scriptlets -n nemo-extension-share

%files -n python3-nemo
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
%{python3_sitelib}/nemo_audio_tab-%{version}-py?.*.egg-info

%files -n nemo-extension-compare
%license nemo-compare/nemo-compare/COPYING*
%doc nemo-compare/debian/changelog
%{_bindir}/nemo-compare-preferences
%{_datadir}/nemo-compare/
%{python3_sitelib}/nemo_compare-%{version}-py?.*.egg-info
%{_datadir}/nemo-python/extensions/nemo-compare.py

%files -n nemo-extension-dropbox
%license nemo-dropbox/COPYING
%doc nemo-dropbox/AUTHORS nemo-dropbox/debian/changelog
%{_libdir}/nemo/extensions-3.0/libnemo-dropbox.so
%{_datadir}/nemo-dropbox/
%{_datadir}/icons/hicolor/symbolic/apps/nemo-dropbox-symbolic.svg

%files -n nemo-extension-emblems
%license nemo-emblems/COPYING*
%doc nemo-emblems/debian/changelog
%{_datadir}/nemo-python/extensions/nemo-emblems.py*
%{python3_sitelib}/nemo_emblems-%{version}-py?.*.egg-info

%files -n nemo-extension-fileroller
%license nemo-fileroller/COPYING
%doc nemo-fileroller/debian/changelog
%{_libdir}/nemo/extensions-3.0/libnemo-fileroller.so

%files -n nemo-extension-image-converter
%license nemo-image-converter/COPYING
%doc nemo-image-converter/AUTHORS nemo-image-converter/debian/changelog
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
%{python3_sitelib}/nemo_pastebin-%{version}-py?.*.egg-info

%files -n nemo-extension-preview
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
%{_bindir}/nemo-seahorse-tool
%{_libdir}/nemo/extensions-3.0/libnemo-seahorse.so
%{_libdir}/nemo/extensions-3.0/libnemo-image-converter.so
#%%{_datadir}/applications/nemo-seahorse-pgp-*.desktop
%{_datadir}/glib-2.0/schemas/org.nemo.plugins.seahorse.*.xml
%{_mandir}/man?/nemo-seahorse-tool.?%{?ext_man}
%dir %{_datadir}/nemo-seahorse
%{_datadir}/nemo-seahorse/ui

%files -n nemo-extension-share
%license nemo-share/COPYING
%doc nemo-share/AUTHORS nemo-share/debian/changelog
%{_libdir}/nemo/extensions-3.0/libnemo-share.so
%{_datadir}/nemo-share/
%{_datadir}/polkit-1/actions/org.nemo.share.samba_install.policy

%files -n nemo-extension-terminal
%license nemo-terminal/COPYING
%doc nemo-terminal/AUTHORS nemo-terminal/debian/changelog
%{_bindir}/nemo-terminal-prefs
%{_datadir}/nemo-terminal/
%{_datadir}/nemo-python/extensions/nemo_terminal.py
%{_datadir}/glib-2.0/schemas/org.nemo.extensions.nemo-terminal.gschema.xml
%{python3_sitelib}/nemo_terminal-%{version}-py?.*.egg-info

%changelog
