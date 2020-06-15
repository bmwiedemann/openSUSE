#
# spec file for package howl
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           howl
Version:        0.6
Release:        0
Summary:        Editor with keyboard-centric minimalistic interface
License:        MIT
Group:          Productivity/Text/Editors
Url:            https://howl.io/
Source0:        https://github.com/howl-editor/howl/releases/download/%{version}/%{name}-%{version}.tgz
Source1:        howl-rpmlintrc
Patch0:         howl-respect-cflags.patch
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
Requires:       luajit
# Bundled LuaJIT-2.1.0-beta3 failed to compile with this architectures
ExcludeArch:    aarch64 ppc64 ppc64le s390x

%description
Howl is a general purpose editor that is customizable. It is built on
top of the LuaJIT runtime, and can be extended in either Lua or
Moonscript. It has a minimalistic UI, driven mainly using the
keyboard.

%prep
%setup -q
%patch0 -p1
find . -name '*.rb' -exec sed -i "s/#! \/usr\/bin\/env ruby/#!\/usr\/bin\/ruby/" {} +

%build
export CFLAGS="%{optflags}"
cd src
make %{?_smp_mflags}

%install
pushd src
%make_install PREFIX=%{_prefix}
popd

cp -R share/ %{buildroot}%{_prefix}/

%suse_update_desktop_file -r howl Utility TextEditor

%fdupes %{buildroot}%{_prefix}

%files
%license LICENSE.md
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_bindir}/%{name}
%{_bindir}/%{name}-spec

%changelog
