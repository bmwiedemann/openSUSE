#
# spec file for package vamp-plugin-sdk
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vamp-plugin-sdk
Version:        2.7.1
Release:        0
Summary:        An API for audio analysis and feature extraction plugins
License:        MIT
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://www.vamp-plugins.org/
Source0:        https://code.soundsoftware.ac.uk/attachments/download/2206/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sndfile)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Vamp is an API for C and C++ plugins that process sampled audio data
to produce descriptive output (measurements or semantic observations).

%package -n libvamp-hostsdk3
Summary:        Library for Vamp audio analysis plugin hosts
Group:          System/Libraries

%description -n libvamp-hostsdk3
Vamp is an API for C and C++ plugins that process sampled audio data
to produce descriptive output (measurements or semantic observations).

%package -n libvamp-sdk2
Summary:        Library for Vamp audio analysis plugins
Group:          System/Libraries

%description -n libvamp-sdk2
Vamp is an API for C and C++ plugins that process sampled audio data
to produce descriptive output (measurements or semantic observations).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       libvamp-hostsdk3 = %{version}-%{release}
Requires:       libvamp-sdk2 = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The vamp-plugin-sdk-devel package contains documentation examples and
header files for developing applications that use vamp-plugin-sdk.

%prep
%setup -q
sed -i 's|/lib/vamp|/%{_lib}/vamp|g' src/vamp-hostsdk/PluginHostAdapter.cpp
sed -i 's|/lib/|/%{_lib}/|g' src/vamp-hostsdk/PluginLoader.cpp
sed -i 's|$(INSTALL_PREFIX)/lib|@libdir@|g' Makefile.in

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC -Wall"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC -Wall"
%configure
make %{?_smp_mflags}

%install
# fix libdir
find . -name '*.pc.in' -exec sed -i 's|/lib|/%{_lib}|' {} ';'
# The #INSTALL_PREFIX
make DESTDIR=%{buildroot} install %{?_smp_mflags}
#INSTALL_PREFIX=%%{_prefix} LIB=/%%{_lib}
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name '*.a' -exec rm -f {} ';'
# Build api html docs
doxygen -u build/Doxyfile
doxygen build/Doxyfile
%fdupes -s doc/html
# Build refman.pdf
#pushd latex && make all
#popd

%if 0%{?suse_version} >= 1140
# Generate man pages with help2man
mkdir -p %{buildroot}%{_mandir}/man1
pushd %{buildroot}%{_mandir}/man1
cp -v %{buildroot}%{_bindir}/* ./
help2man -N --no-discard-stderr \
	-o vamp-rdf-template-generator.1 \
	./vamp-rdf-template-generator
help2man -N --no-discard-stderr \
	-o vamp-simple-host.1 \
	./vamp-simple-host
rm  vamp-simple-host vamp-rdf-template-generator
popd
%endif

# create Makefile for examples
cd examples
echo CXXFLAGS=%{optflags} -fpic >> Makefile
echo bundle: `ls *.o` >> Makefile
echo -e "\t"g++ \$\(CXXFLAGS\) -shared -Wl,-Bsymbolic \
     -o vamp-example-plugins.so \
     *.o \$\(pkg-config --libs vamp-sdk\) >> Makefile
echo `ls *.cpp`: >> Makefile
echo -e "\t"g++ \$\(CXXFLAGS\) -c $*.cpp >> Makefile
echo clean: >> Makefile
echo -e "\t"-rm *.o *.so >> Makefile
# clean directory up so we can package the sources
make clean

%post -n libvamp-hostsdk3 -p /sbin/ldconfig

%postun -n libvamp-hostsdk3 -p /sbin/ldconfig

%post -n libvamp-sdk2 -p /sbin/ldconfig

%postun -n libvamp-sdk2 -p /sbin/ldconfig

%files -n libvamp-hostsdk3
%defattr(-,root,root,-)
%{_libdir}/libvamp-hostsdk.so.3*

%files -n libvamp-sdk2
%defattr(-,root,root,-)
%{_libdir}/libvamp-sdk.so.2*

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/vamp-rdf-template-generator
%{_bindir}/vamp-simple-host
%if 0%{?suse_version} >= 1140
%{_mandir}/man1/vamp-rdf-template-generator.1.gz
%{_mandir}/man1/vamp-simple-host.1.gz
%endif
%dir %{_libdir}/vamp
%{_libdir}/vamp

%files devel
%defattr(-,root,root,-)
%doc rdf/doc doc/html examples
%dir %{_includedir}/vamp
%dir %{_includedir}/vamp-hostsdk
%dir %{_includedir}/vamp-sdk
%{_includedir}/vamp/*
%{_includedir}/vamp-hostsdk/*
%{_includedir}/vamp-sdk/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
