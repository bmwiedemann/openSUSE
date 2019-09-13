#
# spec file for package fcitx-fbterm 
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fcitx-fbterm
Version:	0.2.0
Release:	0
License:	GPL-2.0+
Summary:	Fbterm Support for Fcitx
Url:		https://github.com/fcitx/fcitx-fbterm
Group:		System/I18n/Chinese
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	fcitx-devel
BuildRequires:	gettext
%if 0%{?suse_version}
BuildRequires:	dbus-1-glib-devel
BuildRequires:	pkg-config
%else
BuildRequires:	dbus-glib-devel
BuildRequires:	pkgconfig
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       locale(fbterm:ko;zh_CN;zh_SG)

%description
Fcitx-fbterm is a Wrapper for Fcitx in fbterm, a fast Framebuffer based terminal emulator.

%prep
%setup -q

%build
%{__mkdir} -pv build
pushd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_lib} ..
make %{?_smp_mflags}

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}-helper

%changelog
