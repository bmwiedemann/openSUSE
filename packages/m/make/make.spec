#
# spec file for package make
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


Name:           make
Version:        4.4
Release:        0
Summary:        GNU make
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://www.gnu.org/software/make/make.html
Source:         https://ftp.gnu.org/gnu/make/make-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/make/make-%{version}.tar.gz.sig
# keyring downloaded from https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=make&download=1
Source2:        %{name}.keyring
Patch:          sigpipe-fatal.patch
Patch64:        make-library-search-path.diff
BuildRequires:  pkgconfig
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
Provides:       gmake

%description
The GNU make command with extensive documentation.

%lang_package

%prep
%setup -q
%patch -p1
if [ %{_lib} = lib64 ]; then
%patch64 -p1
fi

%build
%configure
%make_build

%check
%make_build check || {
  for f in tests/work/*/*.diff*; do
    test -f "$f" || continue
    printf "++++++++++++++ %s ++++++++++++++\n" "${f##*/}"
    cat "$f"
  done
}

%install
%make_install
ln -s make %{buildroot}%{_bindir}/gmake
%find_lang %{name}
# gnumake.h was introduced in 4.0, looks useless
rm %{buildroot}%{_includedir}/gnumake.h

%files
%{_bindir}/make
%{_bindir}/gmake
%{_infodir}/make.info-*%{ext_info}
%{_infodir}/make.info%{ext_info}
%{_mandir}/man1/make.1%{ext_man}

%files lang -f %{name}.lang

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%changelog
