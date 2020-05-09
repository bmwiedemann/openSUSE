#
# spec file for package solfege
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


#
%if 0%{?suse_version} > 1320 || 0%{?is_opensuse} == 1
%define usemyprovides 0
%else
%define usemyprovides 1
%endif

Name:           solfege
Summary:        An ear training program
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Version:        3.23.4
Release:        0
URL:            https://www.gnu.org/software/solfege/
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  libxslt
BuildRequires:  python3-gobject-devel
BuildRequires:  swig
BuildRequires:  texinfo
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(python3)
%if 0%{?suse_version} > 1320 || 0%{?is_opensuse} == 1
BuildRequires:  txt2man
%endif

%if 0%{?usemyprovides} == 1
%define _use_internal_dependency_generator 0
%define my_provides /tmp/my-provides
%endif

Source0:        ftp://alpha.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        lessonfile_editor.1
Source2:        ftp://alpha.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Patch0:         solfege-configure-fix.dif
Patch1:         solfege-python-fixcompile.patch
Patch2:         solfege-nogenreadmeetc.patch
# PATCH-FIX-UPSTREAM - sent by mail to tca@gnu - is upstream orphaned?
Patch3:         reproducible.patch
Requires:       lilypond-fonts-common >= 2.20
Requires:       python3-gobject-Gdk
Requires:       timidity

%description
Solfege is an eartraining program for X written in python, using
the GTK+ and GNOME libraries. To use this software you need some
basic knowledge about music theory. Using solfege you can learn
to recognise melodic and harmonic intervals, compare interval
sizes, sing the intervals the computer asks for, identify chords,
sing chords, scales, dictation and remember rhythmic patterns.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3 -p1

for i in `grep -rl "/usr/bin/env python "`;do $(chmod 0755 ${i} ; sed -i '1s/^#!.*/#!\/usr\/bin\/python3 /' ${i}) ;done
#for i in `grep -rl "!/usr/bin/python "`;do $(chmod 0755 ${i} ; sed -i '1s/^#!.*/#!\/usr\/bin\/python3 /' ${i}) ;done

%build
autoreconf -fi

%configure \
    --enable-docbook-stylesheet=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/html/chunker.xsl \
    --disable-oss-sound
make %{?jobs:-j%jobs} all

%install
%makeinstall

%if 0%{?usemyprovides} == 1
# exclude plugins from the provide-list
cat << EOF > %{my_provides}
grep -v %{buildroot}%{_libdir}/%{name} | %{__find_provides}
EOF
chmod 755 %{my_provides}
%define __find_provides %{my_provides}
%endif

%suse_update_desktop_file solfege Education X-SuSE-Music

# This line caused bnc#664826
#rm -f %%{buildroot}/%%{_datadir}/%%{name}/%%{name}/_version.*
%find_lang %{name}
%fdupes -s %{buildroot}
# Fix any .py files with shebangs and wrong permissions.
chmod 0755 %{buildroot}/usr/share/solfege/solfege/_version.py
chmod 0755 %{buildroot}/usr/share/solfege/solfege/parsetree.py
chmod 0755 %{buildroot}/usr/share/solfege/solfege/presetup.py
chmod 0644 %{buildroot}/usr/share/solfege/solfege/_version.py
find %{buildroot}/usr/share/solfege/ -name "*~" -print -delete

%post
#/sbin/ldconfig
if test -e /dev/music;
then break;
else mknod /dev/music u 14 8 > /dev/null;
fi

#%%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root)
%doc changelog
%license COPYING
%{_bindir}/*
%{_datadir}/solfege
#%%{_libdir}/solfege
%{_mandir}/man1/*.1.gz
%config %{_sysconfdir}/solfege*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
