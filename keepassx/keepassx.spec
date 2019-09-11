#
# spec file for package keepassx
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


Name:           keepassx
Version:        2.0.3
Release:        0
Summary:        Cross Platform Password Manager
License:        GPL-2.0 and LGPL-2.1 and LGPL-3.0+
Group:          Productivity/Security
Url:            https://www.keepassx.org/
Source0:        https://www.keepassx.org/releases/%{version}/keepassx-%{version}.tar.gz
Source1:        https://www.keepassx.org/releases/%{version}/keepassx-%{version}.tar.gz.sig
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM keepassx-fix-undefined-libraries.patch
# https://www.keepassx.org/dev/issues/389
Patch0:         keepassx-fix-undefined-libraries.patch
# PATCH-FEATURE-UPSTREAM https://github.com/keepassx/keepassx/pull/196
Patch1:         appdata.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libXtst-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libqt4-devel >= 4.6
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A free/open-source password manager or safe which helps you to
manage your passwords in a secure way. You can put all your passwords in one
database, which is locked with one master key or a key-disk. So you only have
to remember one single master password or insert the key-disk to unlock the
whole database. The databases are encrypted using the best and most secure
encryption algorithms currently known (AES and Twofish).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake \
  -DWITH_CXX11=ON
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file %{name} X-SuSE-DesktopUtility

%fdupes -s %{buildroot}/%{_prefix}

%check
make %{?_smp_mflags} -C build test

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc COPYING LICENSE*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/keepassx.desktop
%{_libdir}/%{name}/
%{_datadir}/icons/hicolor
%{_datadir}/mime/packages/keepassx.xml
%dir %{_datadir}/appdata/
%{_datadir}/appdata/keepassx.appdata.xml

%changelog
