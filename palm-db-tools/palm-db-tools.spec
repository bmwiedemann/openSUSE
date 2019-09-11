#
# spec file for package palm-db-tools
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


Name:           palm-db-tools
BuildRequires:  gcc-c++
BuildRequires:  libtool
Version:        0.3.6
Release:        0
Source:         %{name}-%{version}.tar.bz2
Patch:          %{name}.dif
Patch1:         %{name}-%{version}-type-fix.diff
Patch2:         %{name}-%{version}-gcc.diff
Patch3:         gcc46_build_fix.patch
Url:            http://pilot-db.sourceforge.net//
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        convert text files into several PalmOS database formats
License:        GPL-2.0+
Group:          Hardware/Palm

%description
The palm-db-tools package convert text files to several flat-file
database formats. The currently supported formats are: DB	
http://pilot-db.sourceforge.net/ MobileDB 
http://www.mobilegeneration.com/products/mobiledb/ List     
http://www.magma.ca/~roo/list/list.html JFile v3.x (v4.x will be
supported later) http://www.land-j.com/jfile.html

%prep
%setup -n %{name}
%patch
%patch1
%patch2
%patch3
#convert dos2unix file format 
cat configure.in | tr -d '\015' >configure.in.new && mv -f configure.in.new configure.in

%build
libtoolize --force
autoreconf --install --force
chmod a+x configure
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS -Wno-deprecated -fPIC" \
./configure --prefix=/usr \
	    --exec_prefix=/usr \
	    --bindir=/usr/bin \
	    --sysconfdir=%{_sysconfdir} \
	    --mandir=%{_mandir} \
	    --infodir=%{_infodir} \
	    --libdir=/usr/%_lib
make %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README NEWS  ChangeLog   TODO  docs/manual.txt
/usr/%_lib/libpdbtools.so
/usr/bin/csv2pdb
/usr/bin/pdb2csv

%changelog
