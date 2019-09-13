#
# spec file for package tamil-gtk2im
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           tamil-gtk2im
BuildRequires:  gtk2-devel libtool update-desktop-files
%define prefix /usr
%define sysconfdir /etc
License:        BSD-3-Clause
Group:          System/GUI/GNOME
Provides:       locale(gtk2:ta)
PreReq:         /usr/bin/touch
Requires:       gtk2
Version:        2.2
Release:        288
Url:            http://tamillinux.sourceforge.net/projects/project/gtk2tamilim/
Source0:        http://tamillinux.sourceforge.net/projects/project/gtk2tamilim/files/tamilgtk2im-src-2.2.tar.bz2
Source1:        License
Source2:        baselibs.conf
Patch:          tamilgtk2im-rpath.patch
Patch1:         tamilgtk2im-biarch.patch
Patch2:         tamilgtk2im-cflags.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Tamil99 Keyboard Input module for GTK2
%gtk2_immodule_requires

%description
Tamil99 Keyboard Input module for GTK2



Authors:
--------
    Dinesh Nadarajah <dinesh_list@sbcglobal.net>

%prep
%setup -q -n tamilgtk2im-src-%{version}
cp $RPM_SOURCE_DIR/License .
%patch
%if %_lib == lib64
%patch1
%endif
%patch2

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
./compile-gtk2im.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/%{_lib}/gtk-2.0/immodules
install -m 755 ./.libs/*.{la,so} $RPM_BUILD_ROOT%{prefix}/%{_lib}/gtk-2.0/immodules

%post
%gtk2_immodule_post
/sbin/ldconfig

%postun
%gtk2_immodule_postun
/sbin/ldconfig

%clean
#[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc README License
%{prefix}/%{_lib}/gtk-2.0/immodules

%changelog
