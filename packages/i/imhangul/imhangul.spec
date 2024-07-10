#
# spec file for package imhangul
#
# Copyright (c) 2023 SUSE LLC
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


Name:           imhangul
Version:        3.1.1+git20130112.a4c2796
Release:        0
Summary:        GTK+-3.0 Hangul Input Modules
License:        GPL-2.0-or-later
Group:          System/I18n/Korean
URL:            https://github.com/choehwanjin/imhangul
Source:         imhangul-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM marguerite@opensuse.org don't use gtk_alignment_set_padding
Patch0:         deprecated-gtkalignment-gtk3.14.patch
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libhangul-devel
BuildRequires:  libtool
Provides:       locale(gtk3:ko)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{gtk3_immodule_requires}

%description
GTK+-2.0 Hangul input modules.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
export CFLAGS="%{optflags}"
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--with-gtk-im-module-dir=%{_libdir}/gtk-3.0/3.0.0/immodules \
	%{_target_platform}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang im-hangul-3.0
find %{buildroot} -name "*.la" -delete

%post
%{gtk3_immodule_post}
/sbin/ldconfig

%postun
%{gtk3_immodule_postun}
/sbin/ldconfig

%files -f im-hangul-3.0.lang
%defattr(-,root,root)
%doc AUTHORS README COPYING ChangeLog.0 TODO NEWS
%{_libdir}/gtk-3.0/3.0.0/immodules/im-hangul.so

%changelog
