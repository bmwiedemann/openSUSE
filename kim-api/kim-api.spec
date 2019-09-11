#
# spec file for package kim-api
#
# Copyright (c) 2018--2019 Christoph Junghans, Ryan S. Elliott
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

Name:           kim-api
Version:        2.0.2
Release:        0
Summary:        Open Knowledgebase of Interatomic Models KIM API
License:        CDDL-1.0
Group:          Productivity/Scientific/Chemistry
Url:            https://openkim.org
Source0:        https://s3.openkim.org/kim-api/kim-api-%{version}.txz
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  pkg-config
BuildRequires:  cmake >= 3.4
BuildRequires:  vim
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libkim-api2 = %{version}

%description
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package can be used to load all the files (libraries, headers, and
documentation) for the KIM-API.


%package -n libkim-api2
Summary:        The kim-api library
Group:          System/Libraries

%description -n libkim-api2
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package contains the kim-api library.

%package devel
Summary:    Development headers and libraries for kim-api
Group:      Development/Libraries/C and C++
Requires:   vim
Requires:   libkim-api2 = %{version}
Requires:   %{name} = %{version}

%description devel
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package contains the development files (headers and documentation) for the
KIM-API.

%package examples
Summary:    Example models for kim-api
Group:      Productivity/Scientific/Chemistry

%description examples
OpenKIM is an online framework for making molecular simulations reliable,
reproducible, and portable.  Models conforming to the KIM application
programming interface work seamlessly with major simulation codes that have
adopted the KIM-API standard.

This package contains the example models for the KIM-API.

%prep
%setup -q -n %{name}-%{version}

%build
%{cmake} -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} ..
%make_jobs

%install
%cmake_install
mkdir -p %{buildroot}/usr/share/bash-completion/completions
mv %{buildroot}/etc/bash_completion.d/kim-api-collections-management.bash %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}/usr/share/emacs/site-lisp
mv %{buildroot}/usr/share/emacs/site-lisp/kim-api/kim-api-c-style.el %{buildroot}%{_datadir}/emacs/site-lisp/kim-api-c-style.el
mkdir -p %{buildroot}/usr/share/cmake/kim-api
mv %{buildroot}%{_libdir}/kim-api/cmake/kim-api-config.cmake %{buildroot}%{_datadir}/cmake/kim-api/kim-api-config.cmake
mv %{buildroot}%{_libdir}/kim-api/cmake/kim-api-config-version.cmake %{buildroot}%{_datadir}/cmake/kim-api/kim-api-config-version.cmake
mkdir -p %{buildroot}/usr/share/cmake/Modules
mv %{buildroot}%{_libdir}/kim-api/cmake/Modules/FindKIM-API.cmake %{buildroot}%{_datadir}/cmake/Modules/FindKIM-API.cmake


%post -n libkim-api2 -p /sbin/ldconfig
%postun -n libkim-api2 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md LICENSE.CDDL
%{_bindir}/kim-api-*
%{_libexecdir}/kim-api/kim-api-collections-info
%{_libexecdir}/kim-api/kim-api-simulator-model
%{_libexecdir}/kim-api/kim-api-shared-library-test
%ifnarch i686
%dir %{_libexecdir}/kim-api
%endif
%{_datadir}/bash-completion/completions/kim-api-collections-management.bash
%{_datadir}/emacs/site-lisp/kim-api-c-style.el

%files -n libkim-api2
%defattr(-,root,root,-)
%{_libdir}/libkim-api.so.*

%files devel
%defattr(-,root,root)
%doc LICENSE.CDDL
%{_includedir}/kim-api/
%{_libdir}/kim-api/mod/
%{_libdir}/kim-api/cmake/
%{_datadir}/cmake/
%dir %{_libdir}/kim-api/
%{_libdir}/libkim-api.so
%{_libdir}/pkgconfig/libkim-api.pc

%files examples
%{_libdir}/kim-api/model-drivers/
%{_libdir}/kim-api/models/
%{_libdir}/kim-api/simulator-models/

%changelog
