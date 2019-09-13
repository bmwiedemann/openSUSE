#
# spec file for package jimtcl
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

%define libjim_name libjim0_75

Name:           jimtcl
Version:        0.75
Release:        0
Summary:        A small embeddable Tcl interpreter
License:        BSD-2-Clause
Group:          Development/Languages/Tcl
Url:            http://jim.tcl.tk
Source:         jimtcl-%{version}.tar.gz
Patch0:         jimtcl-fix_doc_paths.patch
BuildRequires:  asciidoc

%description
Jim is an opensource small-footprint implementation of the Tcl programming
language. It implements a large subset of Tcl and adds new features like
references with garbage collection, closures, built-in Object Oriented
Programming system, Functional Programming commands, first-class arrays and
UTF-8 support.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Tcl
Requires:       %{name} = %{version}
Requires:       %{libjim_name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{libjim_name}
Summary:        A small embeddable Tcl interpreter
Group:          System/Libraries

%description -n %{libjim_name}
Jim is an opensource small-footprint implementation of the Tcl programming language.

%prep
%setup -q -n %{name}-%{version}
%patch0
iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new ; mv AUTHORS.new AUTHORS
iconv --from=ISO-8859-1 --to=UTF-8 LICENSE > LICENSE.new ; mv LICENSE.new LICENSE

%build
#configure is not able to locate the needed binaries, so specify it manualy
export CC=gcc
export LD=ld
export AR=ar
export RANLIB=ranlib
export STRIP=true
%configure --full --shared --disable-option-checking
make %{?_smp_mflags}

%check
make test

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/%{name}
pushd %{buildroot}%{_libdir}/
ln -s libjim.so.* libjim.so
popd

%post -n %{libjim_name} -p /sbin/ldconfig

%postun -n %{libjim_name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE AUTHORS README Tcl.html
%{_bindir}/jimsh

%files -n %{libjim_name}
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/libjim.so.*

%files devel
%defattr(-,root,root,-)
%doc DEVELOPING README.extensions README.metakit README.namespaces README.oo README.utf-8 STYLE
%{_includedir}/*
%{_bindir}/build-jim-ext
%{_libdir}/libjim.so

%changelog
