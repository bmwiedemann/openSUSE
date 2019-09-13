#
# spec file for package libburn
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


%define so_ver 4
Name:           libburn
Version:        1.5.0
Release:        0
Summary:        Library for Writing Preformatted Data onto Optical Media
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Record
Url:            http://libburnia-project.org/
Source0:        http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig

%description
Libburn is a library for writing preformatted data onto optical media such as
CD, DVD, BD (Blu-Ray) and also offers a facility for reading data blocks from
its drives without using the normal block device I/O.

%package devel
Summary:        Development Files for libburn
Group:          Development/Libraries/C and C++
Requires:       libburn%{so_ver} = %{version}

%description devel
Development files for developing applications using libburn.

%package -n cdrskin
Summary:        Limited cdrecord Compatibility Wrapper
Group:          Productivity/Multimedia/CD/Record

%description -n cdrskin
cdrskin is a limited cdrecord compatibility wrapper which allows to use most of
the libburn features from the command line.

%package -n libburn%{so_ver}
Summary:        Library for Writing Preformatted Data onto Optical Media
Group:          System/Libraries

%description -n libburn%{so_ver}
Libburn is a library for writing preformatted data onto optical media such as
CD, DVD, BD (Blu-Ray) and also offers a facility for reading data blocks from
its drives without using the normal block device I/O.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}
doxygen doc/doxygen.conf

%install
%make_install

# Remove libtool config files
find %{buildroot} -type f -name "*.la" -delete -print

# Install devel docs
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
cp -a doc/html/ %{buildroot}%{_docdir}/%{name}-devel/

%fdupes -s %{buildroot}%{_docdir}/%{name}-devel/

%post -n libburn%{so_ver} -p /sbin/ldconfig
%postun -n libburn%{so_ver} -p /sbin/ldconfig

%files devel
%doc AUTHORS CONTRIBUTORS COPYING COPYRIGHT ChangeLog README
%doc doc/{cdtext.txt,cookbook.txt,mediainfo.txt}
%doc %{_docdir}/%{name}-devel/html/
%{_includedir}/libburn/
%{_libdir}/pkgconfig/libburn-1.pc
%{_libdir}/libburn.so

%files -n cdrskin
%doc COPYING COPYRIGHT
%doc cdrskin/{README,cdrskin_eng.html,changelog.txt,wiki_plain.txt}
%{_bindir}/cdrskin
%{_mandir}/man1/cdrskin.1*

%files -n libburn%{so_ver}
%{_libdir}/libburn.so.%{so_ver}*

%changelog
