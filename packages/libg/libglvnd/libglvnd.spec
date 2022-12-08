#
# spec file for package libglvnd
#
# Copyright (c) 2022 SUSE LLC
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
Name:           libglvnd
Version:        1.6.0
Release:        0
Summary:        The GL Vendor-Neutral Dispatch library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/NVIDIA/libglvnd
Source:         https://github.com/NVIDIA/libglvnd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        libglvnd.rpmlintrc
Patch1:         disable-glx-tests.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Provides:       libglvnd0 = %{version}-%{release}
Obsoletes:      libglvnd0 <= %{version}-%{release}
Provides:       Mesa-libGLESv1_CM1
Obsoletes:      Mesa-libGLESv1_CM1
Provides:       Mesa-libGLESv2-2
Obsoletes:      Mesa-libGLESv2-2
Requires:       Mesa-dri

%description
Vendor-neutral dispatch layer for arbitrating OpenGL API calls between
multiple vendors on a per-screen basis, as described by Andy Ritger's
OpenGL ABI proposal.

%package devel
Summary:        Development files for libglvnd
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Vendor-neutral dispatch layer for arbitrating OpenGL API calls between
multiple vendors on a per-screen basis, as described by Andy Ritger's
OpenGL ABI proposal. This package contains the required files for
development.

%prep
%autosetup -p1
# fix env shebang to call py3 directly
sed -i -e "1s|#!.*|#!%{_bindir}/python3|" src/generate/*.py

%build
./autogen.sh
%configure \
%if 0%{?suse_version} < 1330
    --libdir=%{_prefix}/X11R6/%{_lib} \
%endif
    --disable-static \
    --disable-headers \
    --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
>%{_builddir}/%{name}-%{version}/filelist.rpm
%if 0%{?suse_version} < 1330
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
mv %{buildroot}%{_prefix}/X11R6/%{_lib}/pkgconfig/*.pc %{buildroot}/%{_libdir}/pkgconfig
if [ "%{_lib}" == "lib64" ]; then
  mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
  cat > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf << EOF
%{_prefix}/X11R6/%{_lib}
%{_prefix}/X11R6/lib
EOF
  echo "%config %{_sysconfdir}/ld.so.conf.d/%{name}.conf" >%{_builddir}/%{name}-%{version}/filelist.rpm
fi
%endif
mkdir -p %{buildroot}%{_docdir}/%{name}/pkgconfig
mv %{buildroot}/%{_libdir}/pkgconfig/{gl,egl,glesv1_cm,glesv2}.pc \
   %{buildroot}%{_docdir}/%{name}/pkgconfig

%check
%make_build check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f filelist.rpm
%doc README.md
%{_docdir}/%{name}/pkgconfig
%if 0%{?suse_version} < 1330
%dir %{_prefix}/X11R6
%dir %{_prefix}/X11R6/%{_lib}
%{_prefix}/X11R6/%{_lib}/lib*.so.*
%else
%{_libdir}/lib*.so.*
%endif

%files devel
%if 0%{?suse_version} < 1330
%dir %{_prefix}/X11R6
%dir %{_prefix}/X11R6/%{_lib}
%{_prefix}/X11R6/%{_lib}/lib*.so
%else
%{_libdir}/lib*.so
%endif
%{_libdir}/pkgconfig/*.pc
%{_includedir}/glvnd/

%changelog
