#
# spec file for package dar
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dar
Version:        2.5.14
Release:        0
Summary:        Backup and Restore Application
License:        SUSE-GPL-2.0+-with-openssl-exception
Group:          System/Filesystems
Url:            http://dar.linux.free.fr/
Source0:        http://sourceforge.net/projects/dar/files/dar/%{version}/%{name}-%{version}.tar.gz
Source1:        http://dar.linux.free.fr/sign/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        %{name}.changes
Patch2:         dar-use-libc-xattr.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  groff
BuildRequires:  libattr-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libtool
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
Recommends:     par
%ifarch %{ix86} x86_64 ppc
BuildRequires:  upx
%endif

%description
Dar (Disk Archive) is a hardware-independent backup solution. Dar uses
catalogs (unlike tar),which it makes it possible to extract a single
file without having to read the entire archive. It is also possible to
create incremental backups. Dar archives can also be created or used
with the libdar library (for example, with KDar, a KDE application).
This package contains the command line tools and documentation.

%package -n libdar5000
Summary:        Backup and Restore Application
# We recommend the -lang pack from the library, as the lib itself is also gettextized. The main pack does
# not need the Recommends, as it requires the lib anyway (thus indirectyl Recommends the -lang package).
Group:          System/Libraries
Recommends:     %{name}-lang
Provides:       libdar = 2.3.10
Obsoletes:      libdar < 2.3.10
# Package renamed to libdar4, according the shared library policy (2012-07-06) during openSUSE 12.2 cycle.
Provides:       libdar-4 = 2.3.10
Obsoletes:      libdar-4 < 2.3.10
# Package renamed to libdar5000, following so name change
Provides:       libdar4 = %{version}
Obsoletes:      libdar4 < %{version}

%description -n libdar5000
Dar stands for Disk ARchive and is a hardware independent backup
solution. Dar uses catalogs (unlike tar), so it is possible to extract
a single file without having to read the whole archive, and it is also
possible to create incremental backups.

Dar archives can also be created, or used, via the libdar library (for
example with KDar, a KDE application).

This package contains the library used by Dar and KDar.

%package -n libdar-devel
Summary:        Backup and Restore Application
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libdar5000 = %{version}
Requires:       openssl-devel
Requires:       pkgconfig(bzip2)
Requires:       pkgconfig(zlib)

%description -n libdar-devel
Dar stands for Disk ARchive and is a hardware independent backup
solution. Dar uses catalogs (unlike tar), so it is possible to extract
a single file without having to read the whole archive, and it is also
possible to create incremental backups.

Dar archives can also be created, or used, via the libdar library (with
KDar, a KDE application, for example).

This package contains the library used by Dar and KDar.

%lang_package

%prep
%setup -q
%patch2
sed -i -e 's,^AM_GNU_GETTEXT_VERSION.*,-AM_GNU_GETTEXT_VERSION(0.18),' configure.ac
# remove _DATE_ and _TIME_ macros
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE3}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.?pp' |\
    xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
autoreconf -fiv
%configure \
  --with-pic \
  --datadir=%{_defaultdocdir} \
  --disable-static \
  --enable-largefile \
  --disable-dar-static
make %{?_smp_mflags}

%check
# ensure that dynamic linked binaries get installed
file %{buildroot}%{_bindir}/* | grep -q dynamic || exit 1
file %{buildroot}%{_bindir}/* | grep static && exit 1
exit 0

%install
%make_install
# libtool make executables static during installation
# overwrite them with original dynamic linked binaries
install -m 0755 src/dar_suite/.libs/* %{buildroot}%{_bindir}/
find %{buildroot} -type f -name "*.la" -delete -print

# Move the sample scripts to the correct location (otherwise rpmlint will error due to these scripts having execute perms)
mkdir %{buildroot}/%{_defaultdocdir}/%{name}/examples/
mv %{buildroot}/%{_defaultdocdir}/%{name}/samples/* %{buildroot}/%{_defaultdocdir}/%{name}/examples
%fdupes %{buildroot}%{_defaultdocdir}/%{name}
%find_lang %{name}

%post -n libdar5000 -p /sbin/ldconfig
%postun -n libdar5000 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS TODO ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
%{_docdir}/%{name}

%files lang -f %{name}.lang
%defattr(-,root,root)

%files -n libdar5000
%defattr(-,root,root)
%{_libdir}/libdar.so.*
%config(noreplace) %{_sysconfdir}/darrc

%files -n libdar-devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/libdar.so
%{_libdir}/pkgconfig/libdar*.pc

%changelog
