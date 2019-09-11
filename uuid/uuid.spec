#
# spec file for package uuid
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           uuid
Version:        1.6.2
Release:        0
Summary:        OSSP's Universally Unique Identifier generator
License:        MIT
Group:          Development/Libraries/C and C++
%define with_perl 1
Url:            http://www.ossp.org/pkg/lib/uuid/

#Source:        ftp://ftp.ossp.org/pkg/lib/%{name}/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.bz2
Patch0:         uuid-1.5.0_perl_vendor_install.patch
Patch1:         uuid-1.6.0_php.patch
Patch3:         0001-Change-library-name.patch
Patch4:         0002-uuid-preserve-m-option-status-in-v-option-handling.patch
Patch5:         0003-Fix-whatis-entries.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
OSSP uuid is a ISO C99 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE 1.1,
ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique Identifier (UUID).
It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3
(name based, MD5), version 4 (random number based) and version 5 (name based,
SHA-1). Additional API bindings are provided for the languages ISO-C++98,
Perl 5 and PHP 4/5. Optional backward compatibility exists for the ISO C
DCE-1.1 and Perl Data::UUID APIs.

UUIDs are 128-bit numbers which are intended to have a high likelihood of
uniqueness over space and time and are computationally difficult to guess. They
are globally unique identifiers which can be locally generated without
contacting a global registration authority. UUIDs are intended as unique
identifiers for both mass tagging objects with an extremely short lifetime and
to reliably identifying very persistent objects across a network.

%package -n ossp-uuid
Provides:       %{name} = %{version}-%{release}
#
Summary:        OSSP's Universally Unique Identifier generator
Group:          Development/Libraries/C and C++

%description -n ossp-uuid
OSSP uuid is a ISO C99 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE 1.1,
ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique Identifier (UUID).
It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3
(name based, MD5), version 4 (random number based) and version 5 (name based,
SHA-1). Additional API bindings are provided for the languages ISO C++98,
Perl 5 and PHP 4/5. Optional backward compatibility exists for the ISO C
DCE-1.1 and Perl Data::UUID APIs.

UUIDs are 128-bit numbers which are intended to have a high likelihood of
uniqueness over space and time and are computationally difficult to guess. They
are globally unique identifiers which can be locally generated without
contacting a global registration authority. UUIDs are intended as unique
identifiers for both mass tagging objects with an extremely short lifetime and
to reliably identifying very persistent objects across a network.

%define pkg_libname libossp-uuid16

%package -n %{pkg_libname}
Summary:        OSSP's Universally Unique Identifier generator library
Group:          System/Libraries

%description -n %{pkg_libname}
OSSP uuid is a ISO C99 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE 1.1,
ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique Identifier (UUID).
It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3
(name based, MD5), version 4 (random number based) and version 5 (name based,
SHA-1). Additional API bindings are provided for the languages ISO C++98,
Perl 5 and PHP 4/5. Optional backward compatibility exists for the ISO C
DCE-1.1 and Perl Data::UUID APIs.

UUIDs are 128-bit numbers which are intended to have a high likelihood of
uniqueness over space and time and are computationally difficult to guess. They
are globally unique identifiers which can be locally generated without
contacting a global registration authority. UUIDs are intended as unique
identifiers for both mass tagging objects with an extremely short lifetime and
to reliably identifying very persistent objects across a network.


This package contains the shared library of OSSP uuid.

%define pkg_cxx_libname libossp-uuid++16

%package -n %{pkg_cxx_libname}
Summary:        OSSP's Universally Unique Identifier generator library
Group:          System/Libraries

%description -n %{pkg_cxx_libname}
OSSP uuid is a ISO C99 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE 1.1,
ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique Identifier (UUID).
It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3
(name based, MD5), version 4 (random number based) and version 5 (name based,
SHA-1). Additional API bindings are provided for the languages ISO C++98,
Perl 5 and PHP 4/5. Optional backward compatibility exists for the ISO-C
DCE-1.1 and Perl Data::UUID APIs.

UUIDs are 128-bit numbers which are intended to have a high likelihood of
uniqueness over space and time and are computationally difficult to guess. They
are globally unique identifiers which can be locally generated without
contacting a global registration authority. UUIDs are intended as unique
identifiers for both mass tagging objects with an extremely short lifetime and
to reliably identifying very persistent objects across a network.


This package contains the shared C++ library of OSSP uuid.

%define pkg_dce_libname libossp-uuid_dce16

%package -n %{pkg_dce_libname}
Summary:        OSSP's Universally Unique Identifier generator library
Group:          System/Libraries

%description -n %{pkg_dce_libname}
OSSP uuid is a ISO C99 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE 1.1,
ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique Identifier (UUID).
It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3
(name based, MD5), version 4 (random number based) and version 5 (name based,
SHA-1). Additional API bindings are provided for the languages ISO C++98,
Perl 5 and PHP 4/5. Optional backward compatibility exists for the ISO-C
DCE-1.1 and Perl Data::UUID APIs.

UUIDs are 128-bit numbers which are intended to have a high likelihood of
uniqueness over space and time and are computationally difficult to guess. They
are globally unique identifiers which can be locally generated without
contacting a global registration authority. UUIDs are intended as unique
identifiers for both mass tagging objects with an extremely short lifetime and
to reliably identifying very persistent objects across a network.


This package contains the shared library of OSSP uuid with DCE compatibility.

%package devel
Requires:       %{pkg_cxx_libname} = %{version}
Requires:       %{pkg_dce_libname} = %{version}
Requires:       %{pkg_libname} = %{version}
Summary:        Development files for OSSP uuid
Group:          Development/Libraries/C and C++

%description devel
OSSP uuid is a ISO C99 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE 1.1,
ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique Identifier (UUID).
It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3
(name based, MD5), version 4 (random number based) and version 5 (name based,
SHA-1). Additional API bindings are provided for the languages ISO C++98,
Perl 5 and PHP 4/5. Optional backward compatibility exists for the ISO-C
DCE-1.1 and Perl Data::UUID APIs.

UUIDs are 128-bit numbers which are intended to have a high likelihood of
uniqueness over space and time and are computationally difficult to guess. They
are globally unique identifiers which can be locally generated without
contacting a global registration authority. UUIDs are intended as unique
identifiers for both mass tagging objects with an extremely short lifetime and
to reliably identifying very persistent objects across a network.


This package contains the development files for OSSP uuid.

%if 0%{?with_perl}

%package -n perl-OSSP-uuid
%if 0%{?suse_version} > 1020
Requires:       perl-base = %{perl_version}
%else
Requires:       perl = %{perl_version}
%endif
Summary:        Perl bindings for OSSP uuid
Group:          Development/Libraries/Perl
Provides:       perl-Data-UUID = 1.217
Obsoletes:      perl-Data-UUID <= 1.217
Provides:       perl(Data::UUID) = 1.217

%description -n perl-OSSP-uuid
OSSP uuid is a ISO C99 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE 1.1,
ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique Identifier (UUID).
It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3
(name based, MD5), version 4 (random number based) and version 5 (name based,
SHA-1). Additional API bindings are provided for the languages ISO C++98,
Perl 5 and PHP 4/5. Optional backward compatibility exists for the ISO-C
DCE-1.1 and Perl Data::UUID APIs.

UUIDs are 128-bit numbers which are intended to have a high likelihood of
uniqueness over space and time and are computationally difficult to guess. They
are globally unique identifiers which can be locally generated without
contacting a global registration authority. UUIDs are intended as unique
identifiers for both mass tagging objects with an extremely short lifetime and
to reliably identifying very persistent objects across a network.


This package contains the Perl bindings for OSSP uuid.

%endif

%prep
%setup
%patch0
%patch1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure             \
    --includedir=%{_includedir}/ossp/ \
    --disable-static   \
    --with-cxx         \
    %if 0%{?with_php}
    --with-php         \
    %endif
    %if 0%{?with_perl}
    --with-perl        \
    --with-perl-compat \
    %endif
    --with-dce
make LD_RUN_PATH="" %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
%perl_process_packlist
rm -rv %{buildroot}%{_libdir}/*.la
mv -v %{buildroot}%{_libdir}/pkgconfig/{,ossp-}uuid.pc
mv -v %{buildroot}%{_mandir}/man3/uuid.3{,ossp}
mv -v %{buildroot}%{_mandir}/man3/uuid++.3{,ossp}

%check
%ifnarch %arm
LD_LIBRARY_PATH="$PWD/.libs/" make check
%endif

%post   -n %{pkg_libname} -p /sbin/ldconfig

%postun -n %{pkg_libname} -p /sbin/ldconfig

%post   -n %{pkg_dce_libname} -p /sbin/ldconfig

%postun -n %{pkg_dce_libname} -p /sbin/ldconfig

%post   -n %{pkg_cxx_libname} -p /sbin/ldconfig

%postun -n %{pkg_cxx_libname} -p /sbin/ldconfig

%files -n ossp-uuid
%defattr(-,root,root,-)
%doc AUTHORS BINDINGS ChangeLog HISTORY NEWS OVERVIEW README SEEALSO THANKS TODO USERS
%{_mandir}/man1/uuid.1*
%{_bindir}/uuid

%files -n %{pkg_libname}
%defattr(-,root,root,-)
%{_libdir}/libossp-uuid.so.*

%files -n %{pkg_dce_libname}
%defattr(-,root,root,-)
%{_libdir}/libossp-uuid_dce.so.*

%files -n %{pkg_cxx_libname}
%defattr(-,root,root,-)
%{_libdir}/libossp-uuid++.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/uuid-config
%dir %{_includedir}/ossp/
%{_includedir}/ossp/uuid.h
%{_includedir}/ossp/uuid_dce.h
%{_includedir}/ossp/uuid++.hh
%{_libdir}/pkgconfig/ossp-uuid.pc
%{_libdir}/libossp-uuid.so
%{_libdir}/libossp-uuid_dce.so
%{_libdir}/libossp-uuid++.so
%{_mandir}/man3/uuid.3*
%{_mandir}/man3/uuid++.3*
%{_mandir}/man1/uuid-config.1*

%if 0%{?with_perl}

%files -n perl-OSSP-uuid
%defattr(-,root,root,-)
%{perl_vendorarch}/auto/OSSP/
%{perl_vendorarch}/OSSP/
#
%dir %{perl_vendorarch}/Data/
%{perl_vendorarch}/Data/UUID.pm
%{perl_vendorarch}/Data/UUID.pod
#
%{_mandir}/man3/OSSP::uuid.3*
%{_mandir}/man3/Data::UUID.3*
%if 0%{?suse_version} && 0%{?suse_version} < 1140
/var/adm/perl-modules/uuid
%endif
%endif

%changelog
