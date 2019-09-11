#
# spec file for package libisofs
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define so_ver 6
Name:           libisofs
Version:        1.5.0
Release:        0
Summary:        Library for Creating ISO-9660 Filesystems
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Record
Url:            http://libburnia-project.org/
Source0:        http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libacl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if 0%{?suse_version} > 1320 || (0%{?is_opensuse} && 0%{?sle_version} >= 120300)
BuildRequires:  libjte-devel
%endif

%description
Libisofs is a library for creating ISO-9660 filesystems with extensions like
RockRidge or Joliet. It is also a full featured ISO-9660 editor, allowing you
to modify an ISO image or multisession disc, including file addition/removal,
change of file names and attributes, etc.

ISO-9660 images can be made bootable from CD, DVD, or BD via an El Torito boot
record and appropriate boot image files from boot managers like GRUB, ISOLINUX,
or system specific boot loaders. It is also possible to install a Master Boot
Record for hard-disk-like media, e.g. USB memory sticks.

Libisofs supports the extension AAIP which allows to store ACLs and xattr in
ISO-9660 filesystems and zisofs compression which is transparently uncompressed
by some Linux kernels. It is possible to have data file content compressed to
gzip format or to have it filtered by an external process.

%package devel
Summary:        Development Files for libisofs
Group:          Development/Libraries/C and C++
Requires:       libisofs%{so_ver} = %{version}

%description devel
Development files for developing applications using libisofs.

%package -n libisofs%{so_ver}
Summary:        Library for Creating ISO-9660 Filesystems
Group:          System/Libraries

%description -n libisofs%{so_ver}
Libisofs is a library for creating ISO-9660 filesystems with extensions like
RockRidge or Joliet. It is also a full featured ISO-9660 editor, allowing you
to modify an ISO image or multisession disc, including file addition/removal,
change of file names and attributes, etc.

ISO-9660 images can be made bootable from CD, DVD, or BD via an El Torito boot
record and appropriate boot image files from boot managers like GRUB, ISOLINUX,
or system specific boot loaders. It is also possible to install a Master Boot
Record for hard-disk-like media, e.g. USB memory sticks.

Libisofs supports the extension AAIP which allows to store ACLs and xattr in
ISO-9660 filesystems and zisofs compression which is transparently uncompressed
by some Linux kernels. It is possible to have data file content compressed to
gzip format or to have it filtered by an external process.

%prep
%setup -q

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> doc/doxygen.conf.in

# Fix rpmlint error "spurious-executable-perm"
chmod 644 doc/Tutorial

%build
%configure --disable-static
make %{?_smp_mflags}
doxygen doc/doxygen.conf

%install
%make_install

# Remove libtool config files
find %{buildroot} -type f -name "*.la" -delete -print

# Remove documentation (will be added in /usr/share/doc/packages/)
rm -rf %{buildroot}%{_datadir}/doc/%{name}-*

# Install devel docs
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
cp -a doc/html/ %{buildroot}%{_docdir}/%{name}-devel/

%fdupes -s %{buildroot}%{_docdir}/%{name}-devel/

%post -n libisofs%{so_ver} -p /sbin/ldconfig
%postun -n libisofs%{so_ver} -p /sbin/ldconfig

%files devel
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README Roadmap TODO
%doc doc/{Tutorial,checksums.txt,susp_aaip_2_0.txt,susp_aaip_isofs_names.txt,zisofs_format.txt}
%doc %{_docdir}/%{name}-devel/html/
%{_includedir}/libisofs/
%{_libdir}/pkgconfig/libisofs-1.pc
%{_libdir}/libisofs.so

%files -n libisofs%{so_ver}
%{_libdir}/libisofs.so.%{so_ver}*

%changelog
