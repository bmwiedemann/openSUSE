#
# spec file for package gtypist
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gtypist
Version:        2.9.5
Release:        0
Summary:        Universal typing tutor
License:        GPL-3.0
Group:          Amusements/Teaching/Other
Url:            http://gnu.org/software/gtypist/

Source:         http://ftp.gnu.org/gnu/gtypist/%name-%version.tar.xz
Source2:        http://ftp.gnu.org/gnu/gtypist/%name-%version.tar.xz.sig
Source3:        %name.keyring
Patch1:         escdelay.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  ncurses-devel
BuildRequires:  xz
PreReq:         %install_info_prereq

%description
GNU Typist (typist) is a universal typing tutor. You can learn
correct typing and improve your skills by practising its exercises on
a regular basis. Its main features are:

* It comes with several typing tutorials: in Czech, English (Qwerty,
  Dvorak and Colemak keyboards), Russian and Spanish, as well as
  simpler exercises in German, French and Norwegian.

* It interprets a simple and intuitive scripting language that
  describes typing tutorials. You can easily modify existing
  tutorials or create new ones according to your needs.

* Users can navigate through lessons through an easy to use arrow key
  based menu interface. 'vi' up, down, left and right keys can be
  used too!

%package lang
Summary:        Language files for package gtypist
Group:          System/Localization
Requires:       gtypist = %{version}

%description lang
GNU Typist (typist) is a universal typing tutor. You can learn
correct typing and improve your skills by practising its exercises on
a regular basis.

This subpackage contain the translations for the package gtypist.

%prep
%setup -q 
%patch -P 1 -p1

%build 
%configure
make %{?_smp_mflags}

%install
b="%buildroot";
make install DESTDIR="$b"
%find_lang %name

%post
for i in "%_infodir"/gtypist*.gz; do
	%install_info --info-dir="%_infodir" "$i"
done;

%preun
for i in "%_infodir"/gtypist*.gz; do
	%install_info_delete --info-dir="%_infodir" "$i"
done;

%files
%defattr(-,root,root)
%_bindir/gtypist
%_bindir/typefortune
%_datadir/gtypist/
%_infodir/gtypist*.gz
%_datadir/man/man1/gtypist.1*
%_datadir/man/man1/typefortune.1*

%files lang -f %name.lang
%defattr(-,root,root)

%changelog
