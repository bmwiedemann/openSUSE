#
# spec file for package caja-extensions
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


%define _version 1.23
Name:           caja-extensions
Version:        1.23.0
Release:        0
Summary:        Set of extensions for Caja, the MATE file manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE caja-extensions_use-xdgsu.patch sor.alexei@meowr.ru -- Use xdg-su instead of a direct gksu call in caja-gksu.
Patch0:         %{name}_use-xdgsu.patch
# PATCH-FIX-OPENSUSE enable-gupnp-1.2.patch -- reported upstream as https://github.com/mate-desktop/caja-extensions/issues/52
Patch1:         enable-gupnp-1.2.patch
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(gupnp-1.2)
%else
BuildRequires:  pkgconfig(gupnp-1.0)
%endif
BuildRequires:  pkgconfig(libcaja-extension) >= %{_version}
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}

%description
Set of extensions for Caja, the MATE file manager.

%package -n caja-extension-gksu
Summary:        Caja privilege granting plugin
Group:          System/GUI/Other
Requires:       ImageMagick
Requires:       caja >= %{_version}
# caja-gksu is last seen in openSUSE Leap 42.1.
Provides:       caja-gksu = %{version}
Obsoletes:      caja-gksu < %{version}

%description -n caja-extension-gksu
This extension allows you to open files with administration
privileges using the context menu when browsing your files with
Caja file manager.

%package -n caja-extension-image-converter
Summary:        Caja image converter
Group:          System/GUI/Other
Requires:       ImageMagick
Requires:       caja >= %{_version}
Recommends:     caja-extension-image-converter-lang
# mate-file-manager-image-converter is last seen in openSUSE 13.1.
Provides:       mate-file-manager-image-converter = %{version}
Obsoletes:      mate-file-manager-image-converter < %{version}
# caja-image-converter is last seen in openSUSE Leap 42.1.
Provides:       caja-image-converter = %{version}
Obsoletes:      caja-image-converter < %{version}

%description -n caja-extension-image-converter
ImageResizer adds a "Resize Images..." menu item to the context
menu of all images. This opens a dialog where you set the desired
image size and file name. A click on "Resize" finally resizes the
image(s) using ImageMagick's convert tool.

%package -n caja-extension-open-terminal
Summary:        Caja terminal plugin
Group:          System/GUI/Other
Requires:       caja >= %{_version}
Recommends:     caja-extension-open-terminal-lang
# mate-file-manager-open-terminal is last seen in openSUSE 13.1.
Provides:       mate-file-manager-open-terminal = %{version}
Obsoletes:      mate-file-manager-open-terminal < %{version}
# caja-open-terminal is last seen in openSUSE Leap 42.1.
Provides:       caja-open-terminal = %{version}
Obsoletes:      caja-open-terminal < %{version}

%description -n caja-extension-open-terminal
This extension allows to open a Terminal in arbitrary directories
through Caja file manager.

%package -n caja-extension-sendto
Summary:        A collection of 'sendto' plugins for Caja
Group:          System/GUI/Other
Requires:       caja >= %{_version}
Recommends:     caja-extension-sendto-lang
# mate-file-manager-sendto is last seen in openSUSE 13.1.
Provides:       mate-file-manager-sendto = %{version}
Obsoletes:      mate-file-manager-sendto < %{version}
# caja-sendto is last seen in openSUSE Leap 42.1.
Provides:       caja-sendto = %{version}
Obsoletes:      caja-sendto < %{version}

%description -n caja-extension-sendto
This package provides extra functionality to the Caja file manager.
The core package includes CD burner, archiving, email client links
and devices.

%if 0%{?is_opensuse}
%package -n  caja-extension-sendto-gajim
Summary:        Gajim integration for the Caja file manager
Group:          System/GUI/Other
Requires:       caja-extension-sendto = %{version}
Requires:       gajim
# caja-sendto-gajim is last seen in openSUSE Leap 42.1.
Provides:       caja-sendto-gajim = %{version}
Obsoletes:      caja-sendto-gajim < %{version}

%description -n  caja-extension-sendto-gajim
This package provides Gajim integration to the Caja file manager.
%endif

%package -n  caja-extension-sendto-pidgin
Summary:        Pidgin integration for the Caja file manager
Group:          System/GUI/Other
Requires:       caja-extension-sendto = %{version}
Requires:       pidgin
# mate-file-manager-sendto-pidgin is last seen in openSUSE 13.1.
Provides:       mate-file-manager-sendto-pidgin = %{version}
Obsoletes:      mate-file-manager-sendto-pidgin < %{version}
# caja-sendto-pidgin is last seen in openSUSE Leap 42.1.
Provides:       caja-sendto-pidgin = %{version}
Obsoletes:      caja-sendto-pidgin < %{version}

%description -n  caja-extension-sendto-pidgin
This package provides Pidgin integration to the Caja file manager.

%package -n  caja-extension-sendto-upnp
Summary:        UPnP integration for the MATE Desktop file manager
Group:          System/GUI/Other
Requires:       caja-extension-sendto = %{version}
# mate-file-manager-sendto-upnp is last seen in openSUSE 13.1.
Provides:       mate-file-manager-sendto-upnp = %{version}
Obsoletes:      mate-file-manager-sendto-upnp < %{version}
# caja-sendto-upnp is last seen in openSUSE Leap 42.1.
Provides:       caja-sendto-upnp = %{version}
Obsoletes:      caja-sendto-upnp < %{version}

%description -n caja-extension-sendto-upnp
This package provides the functionality to the Caja file manager to
send files over e-mail or instant messaging protocols via Evolution,
Empathy and Pidgin.

%package -n caja-extension-sendto-devel
Summary:        Development files for caja-sendto
Group:          Development/Libraries/X11
Requires:       caja-extension-sendto = %{version}
Requires:       caja-extension-sendto-pidgin = %{version}
Requires:       caja-extension-sendto-upnp = %{version}
# mate-file-manager-sendto-devel is last seen in openSUSE 13.1.
Provides:       mate-file-manager-sendto-devel = %{version}
Obsoletes:      mate-file-manager-sendto-devel < %{version}
# caja-sendto-upnp-devel is last seen in openSUSE Leap 42.1.
Provides:       caja-sendto-devel = %{version}
Obsoletes:      caja-sendto-devel < %{version}

%description -n caja-extension-sendto-devel
This package provides the functionality to the caja file browser to
send files over e-mail or instant messaging protocols via Evolution,
Empathy and Pidgin.

%package -n caja-extension-share
Summary:        Share directory from caja via Samba
Group:          System/GUI/Other
Requires:       caja >= %{_version}
Requires:       mate-icon-theme
Requires:       samba >= 3.0.23
Recommends:     caja-extension-share-lang
# mate-file-manager-share is last seen in openSUSE 13.1.
Provides:       mate-file-manager-share = %{version}
Obsoletes:      mate-file-manager-share < %{version}
# caja-sendto-upnp-devel is last seen in openSUSE Leap 42.1.
Provides:       caja-share = %{version}
Obsoletes:      caja-share < %{version}

%description -n caja-extension-share
Caja-share allows you to quickly share a directory from the Caja
file manager without requiring root access. It uses Samba, so your
directories can be accessed by any operating system.

%package -n caja-extension-wallpaper
Summary:        Allows to quickly set desktop background
Group:          System/GUI/Other
Requires:       caja >= %{_version}
Recommends:     caja-extension-wallpaper-lang
# caja-wallpaper is last seen in openSUSE Leap 42.1.
Provides:       caja-wallpaper = %{version}
Obsoletes:      caja-wallpaper < %{version}

%description -n caja-extension-wallpaper
Caja-share allows you to quickly set desktop background wallpaper.

%package -n caja-extension-xattr-tags
Summary:        See tags stored on xattrs
Group:          System/GUI/Other
Requires:       caja >= %{_version}
Recommends:     caja-extension-xattr-tags-lang

%description -n caja-extension-xattr-tags
Caja-xattr-tags allows one to see tags stored on xattrs.

%package common-lang
Summary:        Languages for Caja extensions
Group:          System/Localization
Provides:       caja-extension-image-converter-lang = %{version}
Provides:       caja-extension-open-terminal-lang = %{version}
Provides:       caja-extension-sendto-lang = %{version}
Provides:       caja-extension-share-lang = %{version}
Provides:       caja-extension-wallpaper-lang = %{version}
Provides:       caja-extension-xattr-tags-lang = %{version}
BuildArch:      noarch

%description common-lang
Provides common translations shared by Caja file manager extensions.

%prep
%setup -q
%patch0 -p1
%if 0%{?suse_version} >= 1550
%patch1
%endif

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static       \
  --enable-shared        \
  --enable-gksu          \
  --enable-image-convert \
  --enable-open-terminal \
  --enable-share         \
  --enable-sendto        \
  --enable-xattr-tags
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%if !0%{?is_opensuse}
rm %{buildroot}%{_libdir}/caja-sendto/plugins/libnstgajim.so
%endif

%if 0%{?suse_version} < 1500
%post -n caja-extension-open-terminal
%glib2_gsettings_schema_post

%postun -n caja-extension-open-terminal
%glib2_gsettings_schema_postun

%post -n caja-extension-sendto
%glib2_gsettings_schema_post

%postun -n caja-extension-sendto
%glib2_gsettings_schema_postun
%endif

%files -n caja-extension-gksu
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/caja/extensions-2.0/libcaja-gksu.so
%{_datadir}/caja/extensions/libcaja-gksu.caja-extension

%files -n caja-extension-image-converter
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-extensions/caja-image-resize.ui
%{_datadir}/caja-extensions/caja-image-rotate.ui
%{_datadir}/caja/extensions/libcaja-image-converter.caja-extension

%files -n caja-extension-open-terminal
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/caja/extensions/libcaja-open-terminal.caja-extension
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml

%files -n caja-extension-sendto
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/caja-sendto
%{_datadir}/caja-extensions/caja-sendto.ui
%{_datadir}/caja/extensions/libcaja-sendto.caja-extension
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%dir %{_libdir}/caja-sendto/
%dir %{_libdir}/caja-sendto/plugins/
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_mandir}/man?/caja-sendto.?%{?ext_man}

%if 0%{?is_opensuse}
%files -n caja-extension-sendto-gajim
%{_libdir}/caja-sendto/plugins/libnstgajim.so
%endif

%files -n caja-extension-sendto-pidgin
%{_libdir}/caja-sendto/plugins/libnstpidgin.so

%files -n caja-extension-sendto-upnp
%{_libdir}/caja-sendto/plugins/libnstupnp.so

%files -n caja-extension-sendto-devel
%{_includedir}/caja-sendto/
%{_libdir}/pkgconfig/caja-sendto.pc
%{_datadir}/gtk-doc/html/caja-sendto/

%files -n caja-extension-share
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/caja/extensions/libcaja-share.caja-extension
%{_datadir}/caja-extensions/share-dialog.ui
%{_libdir}/caja/extensions-2.0/libcaja-share.so

%files -n caja-extension-wallpaper
%license COPYING
%doc AUTHORS ChangeLog README
%{_datadir}/caja/extensions/libcaja-wallpaper.caja-extension
%{_libdir}/caja/extensions-2.0/libcaja-wallpaper.so

%files -n caja-extension-xattr-tags
%{_datadir}/caja/extensions/libcaja-xattr-tags.caja-extension
%{_libdir}/caja/extensions-2.0/libcaja-xattr-tags.so

%files common-lang -f %{name}.lang

%changelog
