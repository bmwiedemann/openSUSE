#
# spec file for package emacs-libgit2
#
# Copyright (c) 2023 SUSE LLC
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


Name:           emacs-libgit2
Version:        467.ab1a53a
Release:        0
Summary:        An experimental module for libgit2 bindings to Emacs
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/magit/libegit2
Source0:        libegit2-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM load libegit from load-path PR 126
Patch1:         0001-libgit.el-Be-able-to-load-libegit2-from-load-path-if.patch
# PATCH-FEATURE-UPSTREAM install targets PR 126
Patch2:         0002-Add-install-targets-for-libgit-and-libegit2.patch
# PATCH-FEATURE-UPSTREAM Don't rebuild libgit even if it already has been build PR 126
Patch3:         0003-Don-t-mark-libgit2-target-as-phony-don-t-rebuild-it-.patch
BuildRequires:  cmake
BuildRequires:  emacs-nox
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(openssl)
Requires:       emacs

%description
This is an experimental module for libgit2 bindings to Emacs, intended to boost the performance of magit.

%prep
%autosetup -p1 -n libegit2-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr \
       -DUSE_SYSTEM_LIBGIT2=ON
%cmake_build

cd ..

%make_build USE_SYSTEM_LIBGIT2=1 loaddefs libgit.elc

%install
%make_install USE_SYSTEM_LIBGIT2=1 LIBDIR=%{_libdir}

%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/libgit.el*
%{_emacs_sitelispdir}/libgit-autoloads.el
%dir %{_libdir}/emacs
%dir %{_libdir}/emacs/site-lisp/
%{_emacs_archsitelispdir}/libegit2.so

%changelog
