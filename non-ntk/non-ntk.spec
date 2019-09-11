#
# spec file for package non-ntk
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           non-ntk
Version:        1.3.0
Release:        0
Summary:        A fork of FLTK for the non audio suite

Group:          Applications/Multimedia
# some codes are in GPLv2+ while FLTK derived code is LGPLv2+ (SUSE-FLTK)
# since linking to the same binary together, restricted solely to GPL-2.0+
License:        GPL-2.0+
URL:            http://non.tuxfamily.org/
Source0:        non-ntk-%{version}-git5719b00.tar.bz2
# script to create source tarball from git
# sh non-snapshot.sh $(rev)
Source1:        non-ntk-snapshot.sh
# no desktop file in tarball
Source2:        non-ntk-1.3.0-fluid.desktop
# sent upstream via email
Patch1:         non-ntk-1.3.0-fsf.patch
Patch2:         non-ntk-unused-shlib.patch

%if %{defined fedora}
BuildRequires:  desktop-file-utils
%endif
%if 0%{?suse_version}
BuildRequires: update-desktop-files
BuildRequires: gcc-c++
%endif
BuildRequires:  python
BuildRequires:  cairo-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xft)

%description
The Non Tool Kit (NTK) is a fork of the Fast Light ToolKit library, adding 
improved graphics rendering via Cairo, a streamlined and enhanced widget set, 
and other features designed to improve the appearance and performance of the 
Non applications. NTK is included in the Non distribution.

%package -n libntk1
Summary:        Development files for %{name}.
Group:          Development/Libraries

%description -n libntk1
This package contains shared libraries for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       libntk1 = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package fluid
Summary: Fast Light User Interface Designer
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel

%description fluid
%{summary}, an interactive GUI designer for %{name}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

sed -i -e "s|append_value('C\(.*\)FLAGS', CFLAGS|append_value('C\1FLAGS','%{optflags}'.split(' ')|" \
 wscript

%build
LDFLAGS="%{?__global_ldflags}" ./waf -v configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --enable-gl
./waf -v %{?_smp_mflags} 

%install 
./waf -v install --destdir=%{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/ntk-fluid.desktop
rm %{buildroot}%{_libdir}/libntk*.a*

%if 0%{?suse_version}
 %suse_update_desktop_file -i ntk-fluid Development GUIDesigner
%endif

%post -n libntk1 -p /sbin/ldconfig

%postun -n libntk1 -p /sbin/ldconfig

%postun fluid
update-desktop-database -q &> /dev/null

%post fluid 
update-desktop-database -q &> /dev/null 
 
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ntk-fluid.desktop

%files
%defattr(-,root,root)
%doc COPYING

%files -n libntk1
%defattr(-,root,root)
%{_libdir}/libntk*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libntk.so
%{_libdir}/libntk_images.so
%{_libdir}/libntk_gl.so
%{_includedir}/ntk
%{_libdir}/pkgconfig/*

%files fluid
%defattr(-,root,root)
%{_datadir}/applications/ntk-fluid.desktop
%{_bindir}/ntk-*

%changelog
