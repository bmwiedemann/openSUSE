#
# spec file for package voms
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2015 mischa.salle@gmail.com
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


Name:           voms
Version:        2.1.0~rc3
%define upstream_version 2.1.0-rc3
Release:        0
Summary:        The Virtual Organisation Membership Service
License:        Apache-2.0
URL:            https://wiki.italiangrid.it/VOMS
Source:         https://github.com/italiangrid/voms/archive/v%{upstream_version}.tar.gz#/%{name}-%{upstream_version}.tar.gz
Patch0:         voms-gcc14.patch

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

%package -n libvomsapi1
Summary:        The Virtual Organisation Membership Service C++ APIs
Group:          System/Libraries
BuildRequires:  gcc-c++

BuildRequires:  bison
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libexpat-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
# Needed for macro fdupes
BuildRequires:  fdupes

%description -n libvomsapi1
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides libraries that applications using the VOMS functionality
will bind to.

%package devel
Summary:        Virtual Organization Membership Service Development Files
Group:          Development/Libraries/C and C++
Requires:       automake
Requires:       libopenssl-devel
Requires:       libvomsapi1%{?_isa} = %{version}-%{release}

%description devel
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides header files for programming with the VOMS libraries.

%package doc
Summary:        Virtual Organization Membership Service Documentation
Group:          Documentation
BuildArch:      noarch

%description doc
Documentation for the Virtual Organization Membership Service APIs.

%package clients
Summary:        Virtual Organization Membership Service Clients
Group:          Applications/Internet
Requires:       libvomsapi1%{?_isa} = %{version}-%{release}

%description clients
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides command line applications to access the VOMS services.

%prep
%autosetup -p1 -n voms-%{upstream_version}

# Fix bad permissions (which otherwise end up in the debuginfo package)
find . '(' -name '*.h' -o -name '*.c' -o -name '*.cpp' -o \
        -name '*.cc' -o -name '*.java' ')' -exec chmod a-x {} +
./autogen.sh

%build
%configure --without-server --disable-static --enable-docs --disable-parser-gen
%make_build

%install
%make_install

# Remove la files
rm %{buildroot}%{_libdir}/*.la

# Remove server specific files
rm \
    %{buildroot}%{_datadir}/%{name}/mysql2oracle \
    %{buildroot}%{_datadir}/%{name}/upgrade1to2 \
    %{buildroot}%{_datadir}/%{name}/voms.data \
    %{buildroot}%{_datadir}/%{name}/voms_install_db \
    %{buildroot}%{_datadir}/%{name}/voms-ping

# Create custom dirs
mkdir -p %{buildroot}%{_sysconfdir}/grid-security/vomsdir
mkdir -p %{buildroot}%{_sysconfdir}/grid-security/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

# Create documentation directory
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m 644 -p LICENSE AUTHORS %{buildroot}%{_docdir}/%{name}-%{version}

# move vomses.template to doc
mv %{buildroot}%{_datadir}/%{name}/vomses.template \
   %{buildroot}%{_docdir}/%{name}-%{version}

## C API documentation
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/VOMS_C_API
cp -pr  doc/apidoc/api/VOMS_C_API/html \
	%{buildroot}%{_docdir}/%{name}-%{version}/VOMS_C_API
rm -f %{buildroot}%{_docdir}/%{name}-%{version}/VOMS_C_API/html/installdox

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/VOMS_CC_API
cp -pr  doc/apidoc/api/VOMS_CC_API/html \
	%{buildroot}%{_docdir}/%{name}-%{version}/VOMS_CC_API
rm -f %{buildroot}%{_docdir}/%{name}-%{version}/VOMS_CC_API/html/installdox

# Handle duplicate files
%fdupes %{buildroot}%{_docdir}

%check
make check

%ldconfig_scriptlets -n libvomsapi1

%posttrans
# Recover /etc/vomses...
if [ -r %{_sysconfdir}/vomses.rpmsave -a ! -r %{_sysconfdir}/vomses ] ; then
   mv %{_sysconfdir}/vomses.rpmsave %{_sysconfdir}/vomses
fi

%files -n libvomsapi1
%{_libdir}/libvomsapi.so.1*
%dir %{_sysconfdir}/grid-security
%dir %{_sysconfdir}/grid-security/vomsdir
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/vomses.template
%doc %{_docdir}/%{name}-%{version}/AUTHORS
%doc %{_docdir}/%{name}-%{version}/LICENSE

%files devel
%{_libdir}/libvomsapi.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}-2.0.pc
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man3/*

%files doc
%doc %{_docdir}/%{name}-%{version}/VOMS_C_API
%doc %{_docdir}/%{name}-%{version}/VOMS_CC_API

%files clients
%{_bindir}/voms-proxy-destroy
%{_bindir}/voms-proxy-fake
%{_bindir}/voms-proxy-info
%{_bindir}/voms-proxy-init
%{_bindir}/voms-proxy-list
%{_bindir}/voms-verify

%{_mandir}/man1/voms-proxy-destroy.1.gz
%{_mandir}/man1/voms-proxy-fake.1.gz
%{_mandir}/man1/voms-proxy-info.1.gz
%{_mandir}/man1/voms-proxy-init.1.gz
%{_mandir}/man1/voms-proxy-list.1.gz

%changelog
