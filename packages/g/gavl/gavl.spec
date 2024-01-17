#
# spec file for package gavl
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


%define soname 1
%define rev    4256

Name:           gavl
Version:        1.4.0rsvn%{rev}
Release:        0
Summary:        Library which provides basic support for uncompressed multimedia data
License:        GPL-3.0+
Group:          System/Libraries
Url:            http://gmerlin.sourceforge.net/
#svn checkout http://svn.code.sf.net/p/gmerlin/code/trunk/gavl/
Source0:        gavl-%{rev}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Gavl is short for Gmerlin Audio Video Library. It is a low level library, upon
which multimedia APIs can be built. Gavl handles all the details of audio and
video formats like colorspaces, samplerates, multichannel configurations etc. It
provides standardized definitions for those formats as well as container
structures for carrying audio samples or video images inside an application.

In addition, it handles the sometimes ugly task to convert between all these
formats and provides some elementary operations (copying, scaling, alpha
blending etc).

%package -n libgavl%{soname}
Summary:        Library which provides basic support for uncompressed multimedia data
Group:          System/Libraries

%description -n libgavl%{soname}
Gavl is short for Gmerlin Audio Video Library. It is a low level library, upon
which multimedia APIs can be built. Gavl handles all the details of audio and
video formats like colorspaces, samplerates, multichannel configurations etc. It
provides standardized definitions for those formats as well as container
structures for carrying audio samples or video images inside an application.

In addition, it handles the sometimes ugly task to convert between all these
formats and provides some elementary operations (copying, scaling, alpha

%package -n libgavl-devel
Summary:        Library which provides basic support for uncompressed multimedia data
Group:          Development/Libraries/C and C++
Requires:       libgavl%{soname} = %{version}

%description -n libgavl-devel
Gavl is short for Gmerlin Audio Video Library. It is a low level library, upon
which multimedia APIs can be built. Gavl handles all the details of audio and
video formats like colorspaces, samplerates, multichannel configurations etc. It
provides standardized definitions for those formats as well as container
structures for carrying audio samples or video images inside an application.

In addition, it handles the sometimes ugly task to convert between all these
formats and provides some elementary operations (copying, scaling, alpha
blending etc).

%prep
%setup -q -n %{name}

#Do not compile in DATE and TIME
echo 'HTML_TIMESTAMP = NO' >> doc/Doxyfile.in

%build
./autogen.sh
%configure --docdir=%{_docdir}/lib%{name} --without-cpuflags
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post -n libgavl%{soname} -p /sbin/ldconfig

%postun -n libgavl%{soname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README TODO
%{_bindir}/gavfdump

%files -n libgavl%{soname}
%defattr(0644, root, root, 0755)
%{_libdir}/libgavl.so.%{soname}*

%files -n libgavl-devel
%defattr(0644, root, root, 0755)
%{_docdir}/lib%{name}
%{_libdir}/libgavl.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
