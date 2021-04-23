#
# spec file for package ephoto
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ephoto
Version:        1.5
Release:        0
Summary:        EFL image viewer/editor/manipulator/slideshow creator
License:        BSD-3-Clause
Group:          Productivity/Graphics/Viewers
Url:            http://enlightenment.org
Source:         http://www.smhouston.us/stuff/%{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(ecore) >= 1.20.0
BuildRequires:  pkgconfig(ecore-evas)
BuildRequires:  pkgconfig(ecore-file)
BuildRequires:  pkgconfig(ecore-imf)
BuildRequires:  pkgconfig(ecore-imf-evas)
BuildRequires:  pkgconfig(ecore-input)
BuildRequires:  pkgconfig(ecore-ipc)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(eet)
BuildRequires:  pkgconfig(efreet)
BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(elementary) >= 1.13.0
BuildRequires:  pkgconfig(emotion)  >= 1.13.0
BuildRequires:  pkgconfig(ethumb_client)
BuildRequires:  pkgconfig(evas)
Requires:       efl
Requires:       elementary >= 1.13.0
Requires:       evas-generic-loaders >= 1.13.0

%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif

Recommends: %{name}-lang = %{version}

%description
Ephoto is an image viewer and editor.

Images can be viewed one at a time, in thumbnail groups, or as a slideshow.
In terms of editing, images can be rotated/mirrored, cropped, colors be
adjusted and artistic filters be applied.

%lang_package

%prep
%setup -q

%build
./autogen.sh
%configure --disable-silent-rules --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}%{_datadir}/%{name}/AUTHORS
rm %{buildroot}%{_datadir}/%{name}/COPYING
%if 0%{?suse_version}
%fdupes %{buildroot}/%{_datadir}
%suse_update_desktop_file ephoto -r "Graphics;Viewer;"
%endif
%find_lang %{name}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png

%files lang -f %{name}.lang

%changelog
