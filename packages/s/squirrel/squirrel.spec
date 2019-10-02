#
# spec file for package squirrel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define tardir SQUIRREL3
%define tarver 3_0_7
Name:           squirrel
Version:        3.0.7
Release:        0
Summary:        A high level imperative/OO programming language
License:        MIT
Group:          Development/Languages/Other
URL:            http://squirrel-lang.org/
Source:         https://downloads.sourceforge.net/project/%{name}/squirrel3/%{name}%20%{version}%20stable/%{name}_%{tarver}_stable.tar.gz
Patch0:         squirrel-autoconfiscate.patch.bz2
Patch1:         squirrel-aliasing.patch
Patch2:         squirrel-ptr_conversion.patch
Patch3:         squirrel-rename_binary.patch
Patch4:         squirrel-gcc47.patch
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
Squirrel is a light weight programming language
featuring higher-order functions,classes/inheritance,
delegation,tail recursion,generators,cooperative
threads,exception handling, reference counting and
garbage collection on demand. C-like syntax.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains everything to embed the Squirrel engine in
your own application.

%package        devel-static
Summary:        Static squirrel libraries
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel-static
This package contains the static versions of the engine and
standard lbrary.

%package        doc
Summary:        Documentation for %{name}
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
Documentation files for squirrel.

%package        examples
Summary:        Example scripts for %{name}
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description examples
Example scripts to show squirrel usage.

%prep
%setup -q -n %{tardir}
dos2unix -q $(find . -type f)
%patch0
%patch1
%patch2 -p1
%patch3
%patch4 -p1
find . -type f -exec chmod -x {} \;
chmod +x configure config.guess config.sub depcomp install-sh ltmain.sh missing
autoreconf -fi

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CXXFLAGS="%{optflags} -std=gnu++0x"
export CFLAGS="%{optflags}"
%configure --enable-static
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}/%{_defaultdocdir}/%{name}
install -m 644 README HISTORY COPYRIGHT %{buildroot}/%{_defaultdocdir}/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,755)
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/README
%doc %{_defaultdocdir}/%{name}/HISTORY
%doc %{_defaultdocdir}/%{name}/COPYRIGHT
%{_bindir}/sqrl
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,755)
%{_includedir}/*
%{_libdir}/*.so

%files devel-static
%defattr(-,root,root,755)
%{_libdir}/*.a
%{_libdir}/*.la

%files doc
%exclude %{_defaultdocdir}/%{name}/README
%exclude %{_defaultdocdir}/%{name}/HISTORY
%exclude %{_defaultdocdir}/%{name}/COPYRIGHT
%{_defaultdocdir}/%{name}/*

%files examples
%defattr(644,root,root,755)
%{_datadir}/%{name}

%changelog
