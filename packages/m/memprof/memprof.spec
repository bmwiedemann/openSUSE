#
# spec file for package memprof
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


Name:           memprof
Version:        0.6.2
Release:        0
Summary:        A Memory Profiler with GNOME Interface
License:        GPL-2.0+
Group:          Development/Tools/Debuggers
Url:            http://www.gnome.org/projects/memprof/
Source:         https://download.gnome.org/sources/memprof/0.6/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM memprof-bfd-headers.patch bgo#688398 dmistar@opensuse.org -- Fix new binutils requirement to include config.h
Patch2:         memprof-bfd-headers.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch3:         memprof-0.5.1-desktop.patch
# PATCH-FIX-UPSTREAM memprof-arch-neutral.patch bgo#663253 rcoe@wi.rr.com -- Fix build on different archs than x86_64 and i586.
Patch4:         memprof-arch-neutral.patch
BuildRequires:  binutils-devel
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libglade2-devel
BuildRequires:  pkg-config
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Depend on x86 instruction set.
ExclusiveArch:  %ix86 x86_64

%description
With this application, profile applications for their memory
requirements and hunt for leaks very easily.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch3
%patch4 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing" CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
  --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
# Change sr@Latn to sr@latin
mv %{buildroot}%{_datadir}/locale/sr@Latn %{buildroot}%{_datadir}/locale/sr@latin
%find_lang memprof %{?no_lang_C}
%suse_update_desktop_file %{name} Development Profiling
%fdupes %{buildroot}

%post
/sbin/ldconfig
%if 0%{?suse_version} > 1130
%desktop_database_post
%endif

%postun
/sbin/ldconfig
%if 0%{?suse_version} > 1130
%desktop_database_postun
%endif

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%dir %{_libdir}/memprof
%{_libdir}/memprof/*.so
%{_datadir}/memprof/
%{_datadir}/pixmaps/*
%{_datadir}/applications/memprof.desktop

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
