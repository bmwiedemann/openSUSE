#
# spec file for package rpm-plugin-imaevmsign
#
# Copyright (c) 2026 SUSE LLC
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


# Enable Python build sourced from rpm spec
%global with_imaevm 1
Name:           rpm-plugin-imaevmsign
Version:        4.20.1
Release:        0
Summary:        IMA EVM file signing plugin
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://rpm.org/
#Git-Clone:     https://github.com/rpm-software-management/rpm
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  ima-evm-utils-devel
BuildRequires:  libacl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcap-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsemanage-devel
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  ncurses-devel
BuildRequires:  popt-devel
BuildRequires:  python-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libzstd)
Requires:       rpm = %{version}
Provides:       rpm-imaevmsign < 4.20.1
Obsoletes:      rpm-imaevmsign < 4.20.1
%{expand:%(sed -n -e '/^Source:/,/^BuildRoot:/p' <%{_sourcedir}/rpm.spec)}
Source99:       rpm.spec

%description
Rpm plugin for IMA EVM file signing support.

%prep
%{expand:%(sed -n -e '/^%%prep/,/^%%install/p' <%{_sourcedir}/rpm.spec | sed -e '1d' -e '$d')}

%install
cd _build
make DESTDIR=%{buildroot} -C sign install
# we just need the plugin
rm -rf %{buildroot}/%{_libdir}/lib*

mkdir -p %{buildroot}/usr/lib/rpm/macros.d
echo "%%__sign_imaevm %%{__plugindir}/imaevmsign.so" > %{buildroot}/usr/lib/rpm/macros.d/macros.imaevmsign

%files
%{_libdir}/rpm-plugins/imaevmsign.so
/usr/lib/rpm/macros.d/macros.imaevmsign

%changelog
