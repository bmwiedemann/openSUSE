#
# spec file for package codelite
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012-2019 Mariusz Fik <fisiu@opensuse.org>.
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


%define short_ver 16.0
# Only available on x86_64 and %%arm (see lldb package)
  %ifarch %{arm} x86_64
    %bcond_without lldb
  %endif
# Not available on ppc
  %ifnarch ppc
    %bcond_without clang
  %endif
Name:           codelite
Version:        16.0.0
Release:        0
Summary:        Code editor for C, C++, PHP and Node.js
# parts of package contain LGPL-3.0 licenced code thus license needs to be
# GPL-3.0
License:        GPL-3.0-only
Group:          Development/Tools/IDE
URL:            http://codelite.org/
Source0:        https://github.com/eranif/codelite/archive/refs/tags/%{version}.tar.gz
# Template files are identified by RPMLint as Development-Files --> Ignore this errors
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM  wxStl.patch conrad@quisquis.de -- Fix problem when wxWidgets was compile with wxUSE_STL=1
Patch0:         wxStl.patch
# PATCH-FIX-OPENSUSE  fix_node_env-script-interpreter.patch andythe_great@pm.me -- Fix RPMLINT warning env-script-interpreter.
Patch1:         fix_node_env-script-interpreter.patch
# PATCH-FIX-UPSTREAM  wxStl.patch conrad@quisquis.de -- Fix problem with wx version 3.1.0 and 3.1.1
Patch2:         wxVersion.patch
# PATCH-FIX-UPSTREAM codelite_wxwidgets_3_1_7.patch -- Fix build issues with wx >= 3.1.7
Patch3:         codelite_wxwidgets_3_1_7.patch
BuildRequires:  cmake
BuildRequires:  ctags
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-3_2-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(sqlite3)
Requires:       ctags
Requires:       hicolor-icon-theme
Requires:       xterm-bin
%if %{with lldb}
BuildRequires:  lldb-devel
%endif
%if %{with clang}
BuildRequires:  llvm-clang-devel
%endif

%description
CodeLite is a code editor for the C, C++, PHP and Node.js programming languages.
It uses an interface with which users can create, build and debug projects.

%prep
%autosetup -p1

%build
%cmake \
   %if %{with clang}
  -DENABLE_CLANG=1 \
  %endif
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_EXE_LINKER_FLAGS="-pie"

%cmake_build

%install
%cmake_install
%__rm %{buildroot}%{_bindir}/ctagsd-tests
%__ln_s -f ctags %{buildroot}%{_bindir}/codelite-ctags
%find_lang %{name}
### Add mime types
mkdir -p %{buildroot}%{_datadir}/mime/packages/
cp -p %{name}.xml %{buildroot}%{_datadir}/mime/packages/
%fdupes %{buildroot}%{_prefix}
### Update translation in desktop menu entry and add IDE as category
%suse_update_desktop_file %{name} IDE

%files -f %{name}.lang
%license COPYING
%doc about.html AUTHORS
%{_bindir}/%{name}*
%{_bindir}/ctagsd
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%exclude %{_datadir}/icons/hicolor/128x128@2x/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%exclude %{_datadir}/icons/hicolor/256x256@2x/apps/%{name}.png
%exclude %{_datadir}/icons/hicolor/32x32@2x/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%exclude %{_datadir}/icons/hicolor/64x64@2x/apps/%{name}.png
%{_mandir}/man1/%{name}*.1%{?ext_man}
%{_datadir}/mime/packages/%{name}.xml

%changelog
