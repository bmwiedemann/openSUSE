#
# spec file for package libkkc
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


%define soname 2
Name:           libkkc
Version:        0.3.6~git20200818.e33e7fb
Release:        0
Summary:        Japanese Kana-string to Kana-Kanji-mixed-string converter
License:        GPL-3.0-only
Group:          System/I18n/Japanese
URL:            https://github.com/ueno/libkkc
Source:         %{name}-%{version}.tar.xz
Source1:        https://github.com/ueno/libkkc/releases/download/v0.3.5/libkkc-data-0.2.7.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - use correct shared library for typelib generation
Patch0:         libkkc-typelib-sharelib.patch
# PATCH-FIX-OPENSUSE marguerite@opensuse.org - lower gettext version
Patch1:         libkkc-gettext.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - public some classes to make vala 0.38 happy
Patch2:         libkkc-public.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# for autogen.sh
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
# json_generator_set_pretty is not available in version below.
BuildRequires:  json-glib-devel >= 0.14.0
BuildRequires:  libgee-devel >= 0.12.0
BuildRequires:  marisa-devel
BuildRequires:  pkg-config
BuildRequires:  vala >= 0.16.0
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libkkc provides a converter from Japanese Kana-string to Kana-Kanji-mixed-string.
It was named after kkc.el in GNU Emacs, a simple Kana Kanji converter,
while libkkc tries to convert sentences in a bit more complex way using N-gram
language models.

%package -n %{name}%{soname}
Summary:        Japanese Kana-string to Kana-Kanji-mixed-string convertion library
Group:          System/Libraries
Requires:       kkc-data
Requires:       skkdic
Requires:       skkdic-extra

%description -n %{name}%{soname}
libkkc provides a converter from Japanese Kana-string to Kana-Kanji-mixed-string.
It was named after kkc.el in GNU Emacs, a simple Kana Kanji converter,
while libkkc tries to convert sentences in a bit more complex way using N-gram
language models.

%package -n typelib-1_0-kkc-1_0
Summary:        Japanese Kana to Kana-Kanji converter -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-kkc-1_0
libkkc provides a converter from Japanese Kana-string to Kana-Kanji-mixed-string.

This package provides the GObject Introspection bindings for libkkc.

%package -n kkc-data
Summary:        Data files for %{name}
Group:          System/I18n/Japanese

%description -n kkc-data
libkkc provides a converter from Japanese Kana-string to Kana-Kanji-mixed-string.

This package provides the data files for libkkc.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description devel
libkkc provides a converter from Japanese Kana-string to Kana-Kanji-mixed-string.

This package contains its development headers and vala bindings.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
NOCONFIGURE=1 ./autogen.sh

%build
%configure --enable-introspection=yes \
	--enable-vala=yes \
	--enable-vapigen=yes
make %{?_smp_mflags}

# make data
cp -r %{SOURCE1} .
tar -xf %{name}-data-0.2.7.tar.xz
OLD=$(pwd)
pushd %{name}-data-0.2.7
cp -r ${OLD}/data/templates/libkkc-data/tools/genfilter.py tools/
cp -r ${OLD}/data/templates/libkkc-data/tools/sortlm.py tools/
%configure
# %{?_smp_mflags} cost too much memory
make
popd

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

find %{buildroot}%{_libdir} -name "*.la" -delete

# install data
pushd %{name}-data-0.2.7
make DESTDIR=%{buildroot} install %{?_smp_mflags}
popd

%fdupes %{buildroot}%{_datadir}/%{name}

%find_lang %{name}

%post -n %{name}%{soname} -p /sbin/ldconfig

%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname} -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/kkc
%{_libdir}/libkkc.so.%{soname}
%{_libdir}/libkkc.so.%{soname}.0.0
%{_datadir}/libkkc/

%files -n typelib-1_0-kkc-1_0
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Kkc-1.0.typelib

%files -n kkc-data
%defattr(-,root,root)
%{_libdir}/%{name}/

%files devel
%defattr(-,root,root)
%{_bindir}/kkc-package-data
%{_includedir}/libkkc/
%{_libdir}/libkkc.so
%{_libdir}/pkgconfig/kkc-1.0.pc
%{_datadir}/gir-1.0/Kkc-1.0.gir
%{_datadir}/vala/vapi/kkc-1.0.deps
%{_datadir}/vala/vapi/kkc-1.0.vapi

%changelog
