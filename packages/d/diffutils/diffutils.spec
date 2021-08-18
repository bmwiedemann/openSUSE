#
# spec file for package diffutils
#
# Copyright (c) 2021 SUSE LLC
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


Name:           diffutils
Version:        3.8
Release:        0
Summary:        GNU diff Utilities
License:        GFDL-1.2-only AND GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.gnu.org/software/diffutils/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Provides:       diff = %{version}
Obsoletes:      diff < %{version}

%description
The GNU diff utilities find differences between files. diff is used to
make source code patches, for instance.

%lang_package

%prep
%autosetup -p1

%build
%configure \
  --with-packager="openSUSE" \
  --with-packager-bug-reports="http://bugs.opensuse.org/"
%make_build

%check
%make_build check

%install
%make_install
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS NEWS README THANKS
%{_bindir}/*
%{_infodir}/diffutils.info%{?ext_info}
%{_mandir}/man1/*.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
