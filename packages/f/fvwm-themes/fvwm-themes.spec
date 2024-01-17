#
# spec file for package fvwm-themes
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fvwm-themes
BuildRequires:  automake
BuildRequires:  fvwm2
Version:        0.7.0
Release:        0
PreReq:         /usr/bin/perl /usr/bin/mkfifo
Requires:       fvwm2 >= 2.5.8
Requires:       perl >= 5.002
Summary:        FVWM Configuration Framework
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            http://fvwm-themes.sourceforge.net/
Source0:        fvwm-themes-0.7.0.tar.bz2
#Patch0:         fvwm-themes-0.4.2-icon-names.patch
#Patch1:         fvwm-themes-0.4.2-menustyle-fontset.patch
#Patch2:         fvwm-themes-windowlook-fontset.patch
#Patch3:         fvwm-themes-modules-fontset.patch
#Patch5:         acdivert.patch
Patch1:         %{name}-head.patch
Patch2:         %{name}-configure.patch
Patch3:         %{name}-destdir.patch
# PATCH-FIX-UPSTREAM
Patch4:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
FVWM Themes is a powerful configuration framework for FVWM, designed to
be easily extendable and configurable.	It includes several prebuilt
themes and a pack of images and sounds.

%prep
%setup -q -n fvwm-themes-0.7.0
%patch1 -p1 -b .head
%patch2 -p1 -b .configure
%patch3 -p1
%patch4 -p1

%build
autoreconf --force --install
export CFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=%{_prefix} \
            --mandir=%{_mandir} \
            --disable-build-menus \
	    --without-gnome
make

%install
export HOST=openSUSE # override build hostname for fvwm-themes-config
make DESTDIR=$RPM_BUILD_ROOT install
for i in %{_prefix}/share/fvwm/themes/current/theme.cfg \
	 %{_prefix}/share/fvwm/themes-rc \
	 %{_prefix}/share/fvwm/themes-rc-2 \
 	 %{_prefix}/share/fvwm/themes-rc-3 ; do

rpmbuildroot2=${RPM_BUILD_ROOT/#\/home\/abuild/\$HOME}
sed -e "s@$RPM_BUILD_ROOT@@g; s@$rpmbuildroot2@@g" < $RPM_BUILD_ROOT/$i > xxtmp
mv xxtmp $RPM_BUILD_ROOT/$i
done

%post
[ -x usr/X11R6/bin/fvwm-themes-menuapp ] && usr/X11R6/bin/fvwm-themes-menuapp --site --build-menus --remove-popup || true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README TODO
%doc doc/FAQ doc/README.1st doc/colorsets doc/fvwm-themes.lsm
%{_prefix}/bin/*
%{_prefix}/share/fvwm/*
%{_mandir}/man?/*

%changelog
