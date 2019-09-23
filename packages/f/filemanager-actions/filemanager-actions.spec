#
# spec file for package filemanager-actions
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   fma
Name:           filemanager-actions
Version:        3.4
Release:        0
Summary:        File manager extensions to launch arbitrary applications on files
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          System/GUI/Other
Url:            https://git.gnome.org/browse/filemanager-actions
Source:         https://download.gnome.org/sources/filemanager-actions/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE filemanager-actions-fix-build.patch -- Fix building.
Patch0:         filemanager-actions-fix-build.patch
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libcaja-extension) >= 1.18
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnautilus-extension)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(uuid)
Recommends:     %{name}-lang
Obsoletes:      caja-extension-actions-lang < %{version}
%if 0%{?suse_version} >= 1500 || (0%{?sle_version} >= 120300 && 0%{?is_opensuse})
BuildRequires:  pkgconfig(libnemo-extension)
%endif

%description
These extensions provide a way to configure applications to
be launched on files selected in file manager interfaces.

%lang_package

%package devel
Summary:        Development files of filemanager-actions
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
# caja-extension-actions-devel was last used in openSUSE Leap 42.3.
Provides:       caja-extension-actions-devel = %{version}
Obsoletes:      caja-extension-actions-devel < %{version}
# caja-extension-actions-doc was last used in openSUSE Leap 42.3.
Provides:       caja-extension-actions-doc = %{version}
Obsoletes:      caja-extension-actions-doc < %{version}
# nautilus-actions-devel was last used in openSUSE Leap 42.3.
Provides:       nautilus-actions-devel = %{version}
Obsoletes:      nautilus-actions-devel < %{version}

%description devel
The filemanager-actions development package includes the header
files, libraries necessary for development with
filemanager-actions.

%package -n caja-extension-actions
Summary:        Caja context menu customisation extension
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Requires:       caja
Supplements:    packageand(%{name}:caja)

%description -n caja-extension-actions
This extension provides a way to configure applications to be
launched on files selected in the Caja interface.

%package -n nautilus-extension-actions
Summary:        Nautilus context menu customisation extension
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       nautilus
Supplements:    packageand(%{name}:nautilus)
# nautilus-actions was last used in openSUSE Leap 42.3.
Provides:       nautilus-actions = %{version}
Obsoletes:      nautilus-actions < %{version}

%description -n nautilus-extension-actions
This extension provides a way to configure applications to be
launched on files selected in the Nautilus interface.

%if 0%{?suse_version} >= 1500 || (0%{?sle_version} >= 120300 && 0%{?is_opensuse})
%package -n nemo-extension-actions
Summary:        Nemo context menu customisation extension
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Requires:       nemo
Supplements:    packageand(%{name}:nemo)

%description -n nemo-extension-actions
This extension provides a way to configure applications to be
launched on files selected in the Nemo interface.
%endif

%prep
%setup -q
%patch0 -p1
sed -i 's|^\(Icon=\).*$|\1%{name}|' src/ui/fma-config-tool.desktop.in

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
  --disable-static       \
  --enable-deprecated    \
  --disable-scrollkeeper \
  --enable-gtk-doc
make %{?_smp_mflags} V=1

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/
mv -f %{buildroot}%{_datadir}/doc/%{name}-%{version}/ \
  %{buildroot}%{_docdir}/%{name}-devel/
rm %{buildroot}%{_docdir}/%{name}-devel/{AUTHORS,INSTALL,NEWS,README}

%suse_update_desktop_file -G "FileManager-Actions Configuration Tool" fma-config-tool
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}/
%find_lang %{name}

%if 0%{?suse_version} < 1500
%post -n caja-extension-actions
%desktop_database_post
%icon_theme_cache_post

%postun -n caja-extension-actions
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%if 0%{?suse_version} >= 1500
%license COPYING*
%else
%doc COPYING*
%endif
%doc AUTHORS NEWS README
%{_bindir}/%{_name}-*
%{_libdir}/%{name}/
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/%{_name}-*/
%{_datadir}/applications/%{_name}-*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/omf/
%{_datadir}/omf/%{_name}-*/

%files -n %{name}-lang -f %{name}.lang

%files -n caja-extension-actions
%{_libdir}/caja/extensions-2.0/lib%{_name}-caja-*.so

%files -n nautilus-extension-actions
%{_libdir}/nautilus/extensions-3.0/lib%{_name}-nautilus-*.so

%if 0%{?suse_version} >= 1500 || (0%{?sle_version} >= 120300 && 0%{?is_opensuse})
%files -n nemo-extension-actions
%{_libdir}/nemo/extensions-3.0/lib%{_name}-nemo-*.so
%endif

%files devel
%doc %{_docdir}/%{name}-devel/
%doc %{_datadir}/gnome/help/%{_name}-config-tool/
%{_includedir}/%{name}/
%{_datadir}/gtk-doc/*/%{name}*/

%changelog
