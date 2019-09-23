#
# spec file for package fastjet
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fastjet
Version:        3.2.1
Release:        0
Summary:        Package for jet finding in pp and e+e- collisions
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://fastjet.fr/
Source:         http://fastjet.fr/repo/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation. 

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

%package -n libfastjet0
Summary:        Shared libraries for fastjet core package
Group:          Development/Libraries/C and C++

%description -n libfastjet0
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation. 

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

This package provides the shared libraries for fastjet and its
plugins.


%package -n fastjet-devel
Summary:        Shared libraries for fastjet core package
Group:          Development/Libraries/C and C++
Requires:       libfastjet0 = %{version}

%description -n fastjet-devel
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation. 

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

This package provides the header files for development with fastjet.


%package -n fastjet-plugin-siscone
Summary:        SISCone plugin for fastjet
Group:          Development/Libraries/C and C++

%description -n fastjet-plugin-siscone
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation. 

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

This package provides shared libraries for SISCone plugin for
fastjet.


%package -n fastjet-plugin-siscone-devel
Summary:        SISCone plugin for fastjet
Group:          Development/Libraries/C and C++
Requires:       fastjet-devel = %{version}
Requires:       fastjet-plugin-siscone = %{version}

%description -n fastjet-plugin-siscone-devel
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation. 

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

This package provides the develoment files for SISCone plugin for
fastjet.

%prep
%setup -q

%build
%configure --disable-static --enable-allcxxplugins
make %{?_smp_mflags}

%install
%make_install

# REMOVE libtool ARCHIVES
rm %{buildroot}%{_libdir}/*.la

%post -n libfastjet0 -p /sbin/ldconfig

%postun -n libfastjet0 -p /sbin/ldconfig

%post -n fastjet-plugin-siscone -p /sbin/ldconfig

%postun -n fastjet-plugin-siscone -p /sbin/ldconfig

%files -n libfastjet0
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_libdir}/libfastjet.so.*
%{_libdir}/libfastjettools.so.*
%{_libdir}/libfastjetplugins.so.*

%files -n fastjet-devel
%defattr(-,root,root)
%{_bindir}/fastjet-config
%{_libdir}/libfastjet.so
%{_libdir}/libfastjettools.so
%{_libdir}/libfastjetplugins.so
%{_includedir}/fastjet/

%files -n fastjet-plugin-siscone
%defattr(-,root,root)
%{_libdir}/libsiscone*.so.*

%files -n fastjet-plugin-siscone-devel
%defattr(-,root,root)
%{_libdir}/libsiscone*.so
%{_includedir}/siscone/

%changelog
