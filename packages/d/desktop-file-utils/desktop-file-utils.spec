#
# spec file for package desktop-file-utils
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           desktop-file-utils
Version:        0.24
Release:        0
Summary:        Utilities for Manipulating Desktop Files
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            http://www.freedesktop.org/wiki/Software/desktop-file-utils
Source0:        http://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
Source1:        suse-update-mime-defaults
Source2:        macros.desktop-file-utils
# PATCH-FEATURE-OPENSUSE desktop-file-utils-suse-keys.patch vuntz@opensuse.org -- Handle SUSE-specific keys in validator. This is not strictly necessary, since they are prefixed with X-, but we can verify that the value has the right type.
Patch0:         desktop-file-utils-suse-keys.patch

BuildRequires:  glib2-devel
BuildRequires:  pkg-config
#!BuildIgnore:  dbus-1-x11
# We need explicit requirement here, as these are required by
# %%filetriggerin that could be started early during the installation
# process.
Requires:       aaa_base
Requires:       awk
Requires:       coreutils

%description
This packages contains a couple of command line utilities for
working with desktop files.

More information about desktop files can be found at:
http://freedesktop.org/wiki/Specifications/desktop-entry-spec

%prep
%autosetup -p0

%build
%configure \
	--with-lispdir=%{_datadir}/emacs/site-lisp
%make_build

%install
%make_install
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
%defattr(-, root, root)
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/desktop-file-edit
%{_bindir}/desktop-file-install
%{_bindir}/desktop-file-validate
%{_bindir}/suse-update-mime-defaults
%{_bindir}/update-desktop-database
%ghost %{_datadir}/applications/mimeinfo.cache
%{_mandir}/man1/desktop-file-edit.1*
%{_mandir}/man1/desktop-file-install.1*
%{_mandir}/man1/desktop-file-validate.1*
%{_mandir}/man1/update-desktop-database.1*
# Own directories to not require emacs installed.
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*.el*
%{_rpmmacrodir}/macros.desktop-file-utils

%changelog
