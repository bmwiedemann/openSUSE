#
# spec file for package codelite
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# Only available on x86_64 and %%arm (see lldb package)
  %ifarch %{arm} x86_64
    %bcond_without lldb
  %endif
# Not available on ppc
  %ifnarch ppc
    %bcond_without clang
  %endif
Name:           codelite
Version:        12.0
Release:        0
Summary:        Code editor for C, C++, PHP and Node.js
# parts of package contain LGPL-3.0 licenced code thus license needs to be
# GPL-3.0
License:        GPL-3.0-only
Group:          Development/Tools/IDE
URL:            http://codelite.org/
Source0:        https://github.com/eranif/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Template files are identified by RPMLint as Development-Files --> Ignore this errors
Source1:        %{name}-rpmlintrc
# PATCH-FEATURE-OPENSUSE codelite-disable-new-version-check.patch fisiu@opensuse.org -- Disable 'new version' check on startup
Patch0:         %{name}-disable-new-version-check.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel >= 3.0.0
BuildRequires:  wxWidgets-devel >= 3.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(sqlite3)
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
%setup -q
%patch0

%build
%cmake \
   %if %{with clang}
  -DENABLE_CLANG=1 \
  %endif
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_SKIP_RPATH=OFF
%make_jobs

%install
%cmake_install
%find_lang %{name}
### Add mime types
mkdir -p %{buildroot}%{_datadir}/mime/packages/
cp -p %{name}.xml %{buildroot}%{_datadir}/mime/packages/
%fdupes %{buildroot}%{_prefix}
### Update translation in desktop menu entry and add IDE as category
%suse_update_desktop_file %{name} IDE

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}.lang
%license COPYING
%doc about.html AUTHORS
%{_bindir}/%{name}*
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
