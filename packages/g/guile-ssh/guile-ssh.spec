#
# spec file for package guile-ssh
#
# Copyright (c) 2024 SUSE LLC
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


%define         libsoname lib%{name}18

Name:           guile-ssh
Version:        0.18.0
Release:        0
Summary:        SSH protocol access from Guile
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://github.com/artyom-poptsov/guile-ssh
Source0:        https://github.com/artyom-poptsov/%{name}/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-devel
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssh) >= 0.8.0
Requires:       guile >= 2.0.9
Requires:       libssh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Guile-SSH is a library that provides access to the SSH protocol for programs written in GNU Guile interpreter.

%package -n %{libsoname}
Summary:        SSH protocol access from Guile
Group:          System/Libraries

%description -n %{libsoname}
The shared libraries for guile-ssh, which let you access the SSH protocol from
Guile.

%package devel
Summary:        Development files for Guile-SSH
Group:          Development/Libraries/Other
Requires:       %{libsoname} = %{version}-%{release}

%description devel
The libraries and header files for developing applications that use guile-ssh.

%prep
%setup -q

%build
autoreconf -vfi
%configure \
	   --disable-silent-rules \
     --disable-static

make %{?_smp_mflags}

%install
%make_install
# install executable examples to /usr/share/guile-ssh/examples
install -t %{buildroot}%{_datadir}/guile-ssh/examples examples/sssh*.scm
rm -rvf %{buildroot}%{_bindir}
# remove static library
find %{buildroot} -name '*.la' -delete

%post   -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/guile-ssh.info.gz

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/guile-ssh.info.gz

%files -n %{libsoname}
%defattr(-,root,root)
%{_libdir}/libguile-ssh.so.*

%files devel
%defattr(-,root,root)
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/guile
%{_libdir}/libguile-ssh.so
%{_datadir}/guile
%{_datadir}/guile-ssh
%{_infodir}/guile-ssh.info.gz
# make example scripts executable
%attr(755,root,root) %{_datadir}/guile-ssh/examples/*.scm
%attr(755,root,root) %{_datadir}/guile-ssh/examples/echo/*.scm
%attr(755,root,root) %{_datadir}/guile-ssh/examples/rpc/*.scm

%changelog
