#
# spec file for package desktop-file-utils
#
# Copyright (c) 2024 SUSE LLC
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


Name:           desktop-file-utils
Version:        0.28
Release:        0
Summary:        Utilities for Manipulating Desktop Files
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://www.freedesktop.org/wiki/Software/desktop-file-utils
Source0:        http://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
Source1:        suse-update-mime-defaults
Source2:        macros.desktop-file-utils
Source3:        install_man.py
# PATCH-FEATURE-OPENSUSE desktop-file-utils-suse-keys.patch vuntz@opensuse.org -- Handle SUSE-specific keys in validator. This is not strictly necessary, since they are prefixed with X-, but we can verify that the value has the right type.
Patch0:         desktop-file-utils-suse-keys.patch
# PATCH-FIX-OPENSUSE install_man_desktop-file-edit_as_symlink.patch -- With Source3 makes manual page "desktop-file-edit.1" a symlink instead of a copy.
Patch1:         install_man_desktop-file-edit_as_symlink.patch
BuildRequires:  glib2-devel
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
#!BuildIgnore:  dbus-1-x11
# We need explicit requirement here, as these are required by
# %%filetriggerin that could be started early during the installation
# process.
%if 0%{?suse_version}
Requires:       aaa_base
Requires:       awk
%else
Requires:       gawk
%endif
Requires:       coreutils

%description
This packages contains a couple of command line utilities for
working with desktop files.

More information about desktop files can be found at:
http://freedesktop.org/wiki/Specifications/desktop-entry-spec

%prep
%autosetup -p1
cp %{SOURCE3} man/install_man.py

%build
%meson
%meson_build

%install
%meson_install
# Install suse-update-mime-defaults
install -m0755 %{SOURCE1} %{buildroot}%{_bindir}/suse-update-mime-defaults
# Install rpm macros
install -D -m644 %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.desktop-file-utils
# Create ghosts based on default $XDG_DATA_DIRS:
mkdir -p %{buildroot}%{_datadir}/applications
touch %{buildroot}%{_datadir}/applications/mimeinfo.cache

%filetriggerin -- %{_datadir}/applications
%{_bindir}/update-desktop-database --quiet %{_datadir}/applications || true
%{_bindir}/suse-update-mime-defaults || true

%filetriggerpostun -- %{_datadir}/applications
if test -x %{_bindir}/update-desktop-database ; then
    %{_bindir}/update-desktop-database --quiet %{_datadir}/applications || true
    %{_bindir}/suse-update-mime-defaults || true
fi

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/desktop-file-edit
%{_bindir}/desktop-file-install
%{_bindir}/desktop-file-validate
%{_bindir}/suse-update-mime-defaults
%{_bindir}/update-desktop-database
%ghost %{_datadir}/applications/mimeinfo.cache
%{_mandir}/man1/desktop-file-edit.1%{?ext_man}
%{_mandir}/man1/desktop-file-install.1%{?ext_man}
%{_mandir}/man1/desktop-file-validate.1%{?ext_man}
%{_mandir}/man1/update-desktop-database.1%{?ext_man}
# Own directories to not require emacs installed.
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*.el*
%{_rpmmacrodir}/macros.desktop-file-utils

%changelog
