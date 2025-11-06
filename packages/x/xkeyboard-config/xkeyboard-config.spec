#
# spec file for package xkeyboard-config
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           xkeyboard-config
Version:        2.46
Release:        0
Summary:        The X Keyboard Extension
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/X11/Utilities
URL:            https://www.freedesktop.org/Software/XKeyboardConfig
Source:         https://xorg.freedesktop.org/archive/individual/data/%{name}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE disable-2xalt_2xctrl-toggle.diff fdo#4927 -- This is just a workaround until fdo#4927 is fixed
Patch109:       n_disable-2xalt_2xctrl-toggle.diff
Patch110:       n_fi-kotoistus-metainfo.patch
%if 0%{?suse_version} < 1550
Patch0:         python-3.11.patch
%endif
Patch1:         U_Make-ua-winkeysenhanced-compatible-with-ckbcomp.patch
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
%if 0%{?suse_version} < 1550
BuildRequires:  python311-base
%else
BuildRequires:  python3-base
%endif
BuildRequires:  xsltproc
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
Requires(post): coreutils
BuildArch:      noarch

%description
The X Keyboard Extension essentially replaces the core protocol
definition of keyboard. The extension makes possible to clearly and
explicitly specify most aspects of keyboard behaviour on per-key basis
and to more closely track the logical and physical state of the
keyboard. It also includes a number of keyboard controls designed to
make keyboards more accessible to people with physical impairments.

%lang_package

%prep
%autosetup -p1

%build
%{meson} \
    -Dcompat-rules=true \
    -Dxorg-rules-symlinks=true
%{meson_build}

%install
%{meson_install}
mkdir -p %{buildroot}%{_localstatedir}/lib/xkb
# Bug 335553
mkdir -p %{buildroot}%{_localstatedir}/lib/xkb/compiled/
ln -snf %{_localstatedir}/lib/xkb/compiled/ %{buildroot}%{_datadir}/xkeyboard-config-2/compiled
%find_lang %{name}
%fdupes -s %{buildroot}%{_datadir}/X11/xkb

# migration to 2.45 (boo#1246516)
%pretrans -p <lua>
local path = "%{_datadir}/X11/xkb"
local stat = posix.stat(path)

if stat and stat.type == "directory" then
  local target = path .. ".rpmmoved"
  local suffix = 0

  while posix.stat(target) do
    suffix = suffix + 1
    target = path .. ".rpmmoved." .. suffix
  end

  local ok, err = os.rename(path, target)
  if not ok then
    io.stderr:write("Rename failed: " .. tostring(err) .. "\n")
    io.stderr:write("Trying Copy and Remove instead\n")
    local ok, kind, exit_code = os.execute("cp -a '" .. path .. "' '" .. target .. "' && rm -rf '" .. path .. "'")
    if not ok or exit_code ~= 0 then
      io.stderr:write("Copy and Remove failed (" .. tostring(kind) .. "): exit code " .. tostring(exit_code) .. "\n")
    end
  end
end

%post
rm -rf %{_localstatedir}/lib/xkb/compiled/server*.xkm

%files
%license COPYING
%doc AUTHORS docs/HOWTO.* docs/README.*
%dir %{_localstatedir}/lib/xkb
%dir %{_localstatedir}/lib/xkb/compiled
%dir %{_datadir}/X11
%{_datadir}/xkeyboard-config-2
%{_datadir}/X11/xkb
%ghost %attr(0755, root, root) %dir %{_datadir}/X11/xkb.rpmmoved
%{_datadir}/pkgconfig/*.pc
%{_mandir}/man7/*

%files lang -f %{name}.lang
%license COPYING
%{_datadir}/locale/*/LC_MESSAGES/xkeyboard-config-2.mo

%changelog
