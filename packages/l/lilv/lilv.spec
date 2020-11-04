#
# spec file for package lilv
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


%define sover 0
%define sordversion %(pkg-config --modversion sord-0)
%define serdversion %(pkg-config --modversion serd-0)
Name:           lilv
Version:        0.24.6
Release:        0
Summary:        C library to make use of LV2 plugins
License:        ISC
Group:          Development/Libraries/C and C++
URL:            http://drobilla.net/software/lilv/
Source0:        http://download.drobilla.net/lilv-%{version}.tar.bz2
Source98:       baselibs.conf
Source99:       lilv-rpmlintrc
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(lv2) >= 1.8.0
BuildRequires:  pkgconfig(serd-0) >= 0.30.0
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0) >= 0.13
BuildRequires:  pkgconfig(sratom-0) >= 0.4.0
# lilv 0.22 require new API of sord 0.13
# Since sord sover unchanged from 0.12, explicitly require here.
Requires(pre):  liblilv-0-%{sover} = %{version}

%description
Lilv is a C library to make use of LV2 plugins in applications.

%package        -n liblilv-0-%{sover}
Summary:        C library to make use of LV2 plugins
# NOTE: This is the only way to ensure that the correct version of sord and serd is installed.
# See boo#1158728
Group:          System/Libraries
Requires:       libserd-0-0 = %{serdversion}
Requires:       libsord-0-0 = %{sordversion}

%description    -n liblilv-0-%{sover}
Lilv is a C library to make use of LV2 plugins in applications.

%package        -n liblilv-0-devel
Summary:        Development files for liblilv
Group:          Development/Libraries/C and C++
Requires:       liblilv-0-%{sover} = %{version}

%description    -n liblilv-0-devel
Lilv is a C library to make use of LV2 plugins in applications.
This subpackage contains the development files for liblilv.

%package        -n python3-lilv
Summary:        Python 3 bindings for lilv
Group:          Development/Libraries/Python

%description    -n python3-lilv
Lilv is a C library to make use of LV2 plugins in applications.
This subpackage contains the Python 3 bindings for lilv.

%prep
%setup -q
echo %{sordversion}

%build
# TODO: The numpy path here is a hack. Check how to properly fix it.
export CFLAGS='%{optflags} -I%{python_sitearch}/numpy/core/include/'
export CXXFLAGS='%{optflags} -I%{python_sitearch}/numpy/core/include/'
python3 ./waf configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --docdir=%{_defaultdocdir} \
  --configdir=%{_sysconfdir} \
  --test \
  --docs
# waf only understands -j, so do not use smp_mflags
python3 ./waf build -v %{?_smp_mflags}

%install
python3 ./waf install --destdir=%{?buildroot}
if [ %{python3_sitelib} != %{python3_sitearch} ]; then
  mkdir -p %{buildroot}%{python3_sitearch}
  mv %{buildroot}%{python3_sitelib}/lilv.py %{buildroot}%{python3_sitearch}/
fi

%post -n liblilv-0-%{sover} -p /sbin/ldconfig
%postun -n liblilv-0-%{sover} -p /sbin/ldconfig

%files
%attr(0755,-,-) %{_bindir}/lilv-bench
%attr(0755,-,-) %{_bindir}/lv2bench
%attr(0755,-,-) %{_bindir}/lv2info
%attr(0755,-,-) %{_bindir}/lv2ls
%attr(0755,-,-) %{_bindir}/lv2apply
%doc AUTHORS NEWS README.md
%{_mandir}/man1/lv2info.1%{?ext_man}
%{_mandir}/man1/lv2ls.1%{?ext_man}
%{_mandir}/man1/lv2apply.1%{?ext_man}
%{_sysconfdir}/bash_completion.d/lilv

%files -n liblilv-0-%{sover}
%license COPYING
%{_libdir}/liblilv-0.so.%{sover}*

%files -n liblilv-0-devel
%{_libdir}/liblilv-0.so
%{_includedir}/lilv-0/
%{_libdir}/pkgconfig/lilv-0.pc
%{_defaultdocdir}/lilv-0/
%{_mandir}/man3/*

%files -n python3-lilv
%{python3_sitearch}/lilv.py

%changelog
