#
# spec file for package ssdeep
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


Name:           ssdeep
Version:        2.14.1
Release:        0
Summary:        Context Triggered Piecewise Hashing values
License:        GPL-2.0 AND GPL-2.0+
Group:          Development/Tools/Other
Url:            http://ssdeep.sourceforge.net/
Source0:        https://github.com/ssdeep-project/ssdeep/releases/download/release-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
Requires(pre):  %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ssdeep is a program for computing and matching Context Triggered Piecewise
Hashing values. It is based on a spam detector called spamsum by Andrews
Trigdell

%package -n libfuzzy2
Summary:        API for ssdeep
Group:          Development/Libraries/C and C++

%description -n libfuzzy2
Libraries for ssdeep, the primary library is libfuzzy.*

%package -n libfuzzy-devel
Summary:        API for ssdeep
Group:          Development/Libraries/C and C++
Requires:       libfuzzy2 = %{version}

%description -n libfuzzy-devel
Devel API for ssdeep, the primary library is libfuzzy.*

%prep
%setup -q

%build
%configure --disable-static
# rpath removal
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%post -n libfuzzy2 -p /sbin/ldconfig
%postun -n libfuzzy2 -p /sbin/ldconfig

%install
%make_install
# Clean up *.a and *.la files
find %{buildroot} -type f -name "*.la" -delete -print

%files
%defattr(-,root,root)
%doc README COPYING TODO FILEFORMAT AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man1/*

%files -n libfuzzy2
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/libfuzzy.so.*

%files -n libfuzzy-devel
%defattr(-,root,root)
%doc README COPYING FILEFORMAT NEWS ChangeLog
%{_includedir}/fuzzy.h
%{_includedir}/edit_dist.h
%{_libdir}/libfuzzy.so

%changelog
